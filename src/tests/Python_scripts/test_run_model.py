import pytest
from unittest.mock import patch, MagicMock, mock_open
from argparse import Namespace

from model_evaluation.run_model import run, write_to_file
from model_evaluation.run_model import get_proj_root, make_env

from pathlib import Path

# --- FIXTURES ---

@pytest.fixture
def default_args():
    
    """Provides a standard set of command-line arguments for the tests."""
    
    return Namespace(
        in_model_path="fake_path/fake_model.zip",
        episodes=2,         
        sleep=0.0,
        active="false",
        config_path=0,
        verbose="false",
        output="false",
        reduction=0,
        padded="false"
    )

# --- TESTS ---

# The @patch decorators replace the real classes/functions in the script with MagicMocks
@patch('model_evaluation.run_model.CacodemonRecognitionActiveEnv')
@patch('model_evaluation.run_model.CacodemonRecognitionEnv')
@patch('model_evaluation.run_model.PPO.load')
@patch('model_evaluation.run_model.make_env')
def test_run_baseline_model(mock_make_env, mock_ppo_load, mock_baseline_env, mock_active_env, default_args):
    
    """Test that the evaluation script successfully runs a baseline model."""
    
    # 1. Setup the fake Model
    fake_model = MagicMock()
    fake_model.predict.return_value = ([0], None) # Predict returns (action, state)
    mock_ppo_load.return_value = fake_model
    
    # 2. Setup the fake vectorised environment
    fake_vec_env = MagicMock()
    
    # Force the step function to instantly end the episode. 
    # Returns: obs, rewards, dones, infos
    # Note: infos is a list of dicts containing 'reward'; infos[0]['reward']
    fake_vec_env.step.return_value = (None, [1.0], [True], [{"reward": 42.0}])
    
    mock_make_env.return_value = fake_vec_env
    
    # 3. Run the evaluation script
    # will loop exactly twice (since default_args.episodes = 2) and then finish safely.
    run(default_args)
    
    # 4. Assertions
    # Did it load the baseline env instead of the active one?
    mock_baseline_env.assert_called_once()
    mock_active_env.assert_not_called()
    
    # Did it load the model passed in?
    mock_ppo_load.assert_called_once_with("fake_path/fake_model.zip")
    
    # Did it step the environment the correct number of times? 
    # (2 episodes * 1 step per episode = 2 steps total)
    assert fake_vec_env.step.call_count == 2
    
    # Did it safely close the environment at the end?
    fake_vec_env.close.assert_called_once()


@patch('model_evaluation.run_model.CacodemonRecognitionActiveEnv')
@patch('model_evaluation.run_model.CacodemonRecognitionEnv')
@patch('model_evaluation.run_model.PPO.load')
@patch('model_evaluation.run_model.make_env')
def test_run_active_model_verbose(mock_make_env, mock_ppo_load, mock_baseline_env, mock_active_env, default_args):
    
    """Test that the evaluation script successfully runs an active model with verbose printing."""
    
    # Modify default args for this specific test
    default_args.active = "true"
    default_args.verbose = "true"
    
    # Setup the fake Model with all the attributes needed for the verbose printout
    fake_model = MagicMock()
    fake_model.predict.return_value = ([0], None)
    fake_model.learning_rate = 0.0003
    fake_model.n_steps = 1024
    
    mock_ppo_load.return_value = fake_model
    
    # Setup the fake Environment
    fake_vec_env = MagicMock()
    fake_vec_env.step.return_value = (None, [1.0], [True], [{"reward": 99.9}])
    mock_make_env.return_value = fake_vec_env
    
    # Run the script
    run(default_args)
    
    # Assertions
    # This time, it should have loaded the ACTIVE env, not the baseline
    mock_active_env.assert_called_once()
    mock_baseline_env.assert_not_called()
    
    

@patch('builtins.open', new_callable=mock_open)
def test_write_to_file_success(mock_file):
    
    """Test that the helper function correctly appends .txt and writes data."""
    
    # Call the function with a filename that is MISSING the .txt extension
    write_to_file("results", "w", "REWARD: 10.0")
    
    # 1. Assert it intercepted the open() command and added the extension
    mock_file.assert_called_once_with("results.txt", "w")
    
    # 2. Assert it successfully wrote the exact string to the file
    mock_file().write.assert_called_once_with("REWARD: 10.0")


@patch('model_evaluation.run_model.CacodemonRecognitionEnv')
@patch('model_evaluation.run_model.PPO.load')
@patch('model_evaluation.run_model.make_env')
@patch('model_evaluation.run_model.get_proj_root')
@patch('os.path.exists')
@patch('builtins.input')
@patch('model_evaluation.run_model.write_to_file')
def test_run_output_file_already_exists(mock_write_to_file, mock_input, mock_exists, mock_root, mock_make_env, mock_ppo_load, mock_baseline_env, default_args):
    
    """Test the interactive prompt when a file already exists, and the user chooses to append."""
    
    # 1. Setup arguments to trigger the output logic
    default_args.output = "test_run_results"
    default_args.episodes = 1 
    
    fake_model = MagicMock()
    fake_model.predict.return_value = ([0], None)
    mock_ppo_load.return_value = fake_model
    
    # 2. Mock the environment so it instantly finishes 1 episode
    fake_vec_env = MagicMock()
    fake_vec_env.step.return_value = (None, [1.0], [True], [{"reward": 42.0}])
    mock_make_env.return_value = fake_vec_env
    
    # 3. Setup Fake File System
    mock_root.return_value = "/fake_root_dir"
    
    # Tell os.path.exists to return True (simulating that the file is already there)
    mock_exists.return_value = True 
    
    # 4. Simulate the user typing 'y' into the terminal prompt
    mock_input.return_value = "y"
    
    # 5. Run the script
    run(default_args)
    
    # 6. Assertions
    # Did it ask the user what to do?
    mock_input.assert_called_once()
    
    # Did it pass the correct arguments to your write_to_file function?
    # It should pass the full path, and "a" (for append mode)
    expected_path = "/fake_root_dir/data/model_performance_data/test_run_results.txt"
    
    mock_write_to_file.assert_called_once()
    args, _ = mock_write_to_file.call_args
    assert args[0] == expected_path
    assert args[1] == "a"  # 'a' for append


@patch('model_evaluation.run_model.CacodemonRecognitionEnv')
@patch('model_evaluation.run_model.PPO.load')
@patch('model_evaluation.run_model.make_env')
@patch('model_evaluation.run_model.get_proj_root')
@patch('os.path.exists')
@patch('builtins.input')
@patch('builtins.open', side_effect=Exception("Fake Permission Denied!"))
def test_run_output_file_creation_fails_and_user_aborts(mock_file, mock_input, mock_exists, mock_root, mock_make_env, mock_ppo_load, mock_baseline_env, default_args):
    
    """Test the error handling when file creation fails and the user chooses to abort."""
    
    default_args.output = "failing_file"
    default_args.episodes = 1
    
    fake_model = MagicMock()
    fake_model.predict.return_value = ([0], None)
    mock_ppo_load.return_value = fake_model
    
    fake_vec_env = MagicMock()
    fake_vec_env.step.return_value = (None, [1.0], [True], [{"reward": 42.0}])
    mock_make_env.return_value = fake_vec_env
    
    mock_root.return_value = "/fake_root_dir"
    
    # Tell os.path.exists to return False (simulating the file doesn't exist yet)
    mock_exists.return_value = False
    
    # Simulate the user typing 'n' to the "Do you want to try again?" prompt
    mock_input.return_value = "n"
    
    # must catch the SystemExit exception as script calls exit(0)
    import sys
    with pytest.raises(SystemExit) as exit_code:
        run(default_args)
        
    # Assert that the script gracefully exited with code 0
    assert exit_code.type == SystemExit
    assert exit_code.value.code == 0
    
    
    
def test_get_proj_root_success():
    
    """Test that it naturally finds the project root without any mocking."""
    root = get_proj_root()
    
    # It should return a valid pathlib.Path object
    assert isinstance(root, Path)
    # The directory it found should actually exist
    assert root.exists()


@patch('model_evaluation.run_model.Path')
def test_get_proj_root_failure(mock_path):
    
    """Test that it raises a FileNotFoundError if it reaches the top of the drive."""
    
    # 1. Create a fake Path object that has no parent directories
    fake_path = MagicMock()
    fake_path.parents = []
    
    # 2. When the function tries to append /".git", return a child path that DOES NOT exist
    fake_child = MagicMock()
    fake_child.exists.return_value = False
    fake_path.__truediv__.return_value = fake_child  # __truediv__ is the magic method for '/'
    
    mock_path.return_value.resolve.return_value = fake_path
    
    # 3. Assert that it panics and throws your exact error
    with pytest.raises(FileNotFoundError, match="Could not locate project root directory"):
        get_proj_root()


# --- TEST MAKE_ENV ---

@patch('model_evaluation.run_model.VecFrameStack')
@patch('model_evaluation.run_model.VecTransposeImage')
@patch('model_evaluation.run_model.DummyVecEnv')
def test_run_model_make_env(mock_dummy, mock_transpose, mock_stack):
    
    """Test that make_env correctly chains the Gym wrappers together."""
    
    # 1. Setup the chain of fake environments being passed along
    mock_dummy.return_value = "dummy_env"
    mock_transpose.return_value = "transposed_env"
    mock_stack.return_value = "final_stacked_env"
    
    base_env = MagicMock()
    
    # 2. Run the function
    result = make_env(base_env)
    
    # 3. Assertions
    mock_dummy.assert_called_once()
    mock_transpose.assert_called_once_with("dummy_env")
    mock_stack.assert_called_once_with("transposed_env", n_stack=4)
    
    # Did it return the final environment in the chain?
    assert result == "final_stacked_env"