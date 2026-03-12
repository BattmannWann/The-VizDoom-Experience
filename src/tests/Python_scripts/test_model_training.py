import pytest
from stable_baselines3.common.vec_env import VecFrameStack

from active_vision_model_training.active_visual_model_training_lvl_1 import linear_lr_schedule, make_env
from active_vision_model_training.active_visual_model_training_lvl_1 import main

import numpy as np

from unittest.mock import patch, MagicMock
from active_vision_model_training.active_visual_model_training_lvl_1 import main


"""
This test file tests the functions used during model training for both the baseline and active vision models.
The active vision file has been chosen for this, but the baseline uses identical function construction and usage. 
"""


## --- TEST 1: The Learning Rate Schedule --- ##

def test_linear_lr_schedule_warmup():
    
    """Test that the learning rate warms up correctly from 0."""
    
    initial = 0.01
    final = 0.001
    warmup = 0.1
    
    schedule = linear_lr_schedule(initial_value=initial, final_value=final, warmup_ratio=warmup)
    
    # In the beginning, progress_remaining == 1.0 and should start at 0.0
    assert schedule(1.0) == 0.0


def test_linear_lr_schedule_decay():
    
    """Test that the learning rate decays correctly after warmup."""
    
    schedule = linear_lr_schedule(initial_value=1.0, final_value=0.1, warmup_ratio=0.1)
    
    # If progress_remaining is 0.0, we are at the end, so it should equal final_value
    assert schedule(0.0) == 0.1


## --- TEST 2: Environment Creation and Manipulation--- ##

def test_make_env_structure():
    
    """Test that make_env returns the correctly wrapped environment."""
    
    env = make_env()
    
    # Check that it successfully stacked 4 frames
    assert isinstance(env, VecFrameStack)

    # check that the observation space is that of: (Channels, Height, Width)
    assert len(env.observation_space.shape) == 3 
    
    env.close()

 
def test_env_seed_setting():
    
    """Test that the environment correctly sets a new seed"""
    
    env = make_env()
    seed = env.seed(123)
    
    assert seed == [123]
    
    env.close()
    
    
def test_env_observation():
    
    """
    Test that the returned observation is a raw pixel array with correct wrapper shapes
    
    The make_env() function wraps the environment (CacodemonRecognitionActiveEnv) using 4 different wrappers:
        1. Monitor - does not change inherent observation shape
        2. DummyVecEnv - adds a batch dimension 
        3. VecTransposeImage - stacks 4 frames together
        4. VecFrameStack - rearranges the shape such that the channels are at the beginning
        
    This results in the following changes to observation:
        (Batch = 1, Channels = 12, Height, Width) = (BCHW) from (HWC)
    """
    
    env = make_env()
    env.seed(123)
    
    initial_obs = env.reset()
    action = [0] #defined for this env, 0 = ATTACK, but this isn't important
    
    obs, rewards, dones, infos = env.step(action)
    
    assert isinstance(obs, np.ndarray)
    assert obs.dtype == np.uint8
    
    assert len(obs.shape) == 4 #4 frames stacked
    assert obs.shape[0] == 1 #batch size 
    assert obs.shape[1] == 12 # 3 RGB channels stacked 4 times (3*4)
    
    env.close()


@patch('active_vision_model_training.active_visual_model_training_lvl_1.PPO')
@patch('active_vision_model_training.active_visual_model_training_lvl_1.make_env')
@patch('os.makedirs')
@patch('os.path.exists')
def test_training_main_clean_directories(mock_exists, mock_makedirs, mock_make_env, mock_ppo):
    
    """Test the training loop when no directories exist yet."""
    
    # 1. Simulate that neither the models nor logs directories exist yet
    mock_exists.return_value = False
    
    # 2. Fake the environment and model to prevent real training
    fake_env = MagicMock()
    mock_make_env.return_value = fake_env
    
    fake_model = MagicMock()
    mock_ppo.return_value = fake_model
    
    # 3. Run the main function
    main(test = "true")
    
    # 4. Assertions to prove coverage
    # Did it try to create the missing directories? (Should be called twice: models and logs)
    assert mock_makedirs.call_count == 2
    
    # Did it initialize PPO?
    mock_ppo.assert_called_once()
    
    # Did it run the training loop and save? (Based on training_repeats = 2)
    assert fake_model.learn.call_count == 1
    assert fake_model.save.call_count == 1
    
    # Did it safely close the environment?
    fake_env.close.assert_called_once()
    

@patch('active_vision_model_training.active_visual_model_training_lvl_1.PPO')
@patch('active_vision_model_training.active_visual_model_training_lvl_1.make_env')
@patch('builtins.input')
@patch('os.path.exists')
def test_training_main_directory_exists_and_user_continues(mock_exists, mock_input, mock_make_env, mock_ppo):
    
    """Test the user prompt when the models directory already exists."""
    
    # 1. Simulate that the directory ALREADY exists
    mock_exists.return_value = True
    
    # 2. Simulate the user typing 'y' to continue training
    mock_input.return_value = "y"
    
    # 3. Run the function
    main(test = "true")
    
    # 4. Assert that it actually asked the user
    mock_input.assert_called_once_with("Do you still want to continue? [Y/N]: ")
    mock_ppo.assert_called_once()
    
    
@patch('active_vision_model_training.active_visual_model_training_lvl_1.PPO')
@patch('active_vision_model_training.active_visual_model_training_lvl_1.make_env')
@patch('os.makedirs')
@patch('os.path.exists')
def test_active_training_main_clean_directories(mock_exists, mock_makedirs, mock_make_env, mock_ppo):
    
    """Test the training loop when no directories exist yet."""
    # Simulate that directories don't exist
    mock_exists.return_value = False
    
    # Fake the environment and model
    fake_env = MagicMock()
    mock_make_env.return_value = fake_env
    fake_model = MagicMock()
    mock_ppo.return_value = fake_model
    
    # Run the function in test mode
    main(test="true")
    
    # Assertions
    assert mock_makedirs.call_count == 2
    mock_ppo.assert_called_once()
    
    assert fake_model.learn.call_count == 1
    assert fake_model.save.call_count == 1
    fake_env.close.assert_called_once()
    

@patch('active_vision_model_training.active_visual_model_training_lvl_1.PPO')
@patch('active_vision_model_training.active_visual_model_training_lvl_1.make_env')
@patch('builtins.input')
@patch('os.path.exists')
def test_active_training_main_directory_exists_and_user_continues(mock_exists, mock_input, mock_make_env, mock_ppo):
    
    """Test the user prompt when the models directory already exists and they type 'y'."""
    
    # Simulate that the directory exists and user types 'y'
    mock_exists.return_value = True
    mock_input.return_value = "y"
    
    fake_env = MagicMock()
    mock_make_env.return_value = fake_env
    
    main(test="true")
    
    mock_input.assert_called_once_with("Do you still want to continue? [Y/N]: ")
    mock_ppo.assert_called_once()
    

@patch('builtins.input')
@patch('os.path.exists')
def test_active_training_main_user_aborts(mock_exists, mock_input):
    
    """Test that the script exits cleanly if the user types 'n'."""
    
    # Simulate directory exists and user types 'n'
    mock_exists.return_value = True
    mock_input.return_value = "n"
    
    # catch the SystemExit exception as code calls exit(0)
    with pytest.raises(SystemExit) as exit_code:
        main(test="true")
        
    assert exit_code.type == SystemExit
    assert exit_code.value.code == 0
    
    
@patch('active_vision_model_training.active_visual_model_training_lvl_1.PPO')
@patch('active_vision_model_training.active_visual_model_training_lvl_1.make_env')
@patch('os.makedirs')
@patch('os.path.exists')
def test_active_training_main_full_training_run(mock_exists, mock_makedirs, mock_make_env, mock_ppo):
    """Test the 'else' branches where test is false (the real training parameters)."""
    
    # Simulate fresh directories
    mock_exists.return_value = False
    
    fake_env = MagicMock()
    mock_make_env.return_value = fake_env
    fake_model = MagicMock()
    mock_ppo.return_value = fake_model
    
    # Let it rip! It will instantly loop 999 times over the fake model.
    main(test="false")
    
    # Assertions
    # Did it create the real (non-test) directories?
    mock_makedirs.assert_any_call("../models_active/Cacodemon_Recognition_")
    
    # Did it run the training 999 times? 
    assert fake_model.learn.call_count == 999
    
    