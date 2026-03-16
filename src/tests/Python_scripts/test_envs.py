import pytest
import numpy as np
import gymnasium as gym
from unittest.mock import MagicMock

# Adjust these imports if your folder structure requires it based on your pytest.ini
from envs.Active_Visual_Cacodemon_Recognition_env import CacodemonRecognitionActiveEnv
from envs.Baseline_Cacodemon_recognition_env import CacodemonRecognitionEnv

# --- FIXTURES ---
# Fixtures automatically set up and tear down environments for each test.
# The 'yield' keyword passes the env to the test, and the code after 'yield' runs when the test finishes.

@pytest.fixture
def baseline_env():
    
    """Creates a standard baseline environment."""
    
    env = CacodemonRecognitionEnv(config_path=0, verbose="false")
    yield env
    env.close()


@pytest.fixture
def active_env_standard():
    
    """Creates an active environment with no reduction."""
    
    env = CacodemonRecognitionActiveEnv(config_path=0, verbose="false", reduction=0)
    yield env
    env.close()


@pytest.fixture
def active_env_reduced_padded():
    
    """Creates an active environment with 50% reduction and padding."""
    
    env = CacodemonRecognitionActiveEnv(config_path=0, verbose="false", reduction=50, padded="true")
    yield env
    env.close()


# --- BASELINE ENVIRONMENT TESTS ---

def test_baseline_env_initialisation(baseline_env):
    
    """Test that spaces are properly defined in the baseline env."""
    
    assert isinstance(baseline_env.action_space, gym.spaces.Discrete)
    assert isinstance(baseline_env.observation_space, gym.spaces.Box)
    assert baseline_env.observation_space.dtype == np.uint8


def test_baseline_env_reset_and_step(baseline_env):
    
    """Test the core reset and step loop for the baseline env."""
    
    obs, info = baseline_env.reset(seed=42)
    
    # Check reset observation
    assert isinstance(obs, np.ndarray)
    assert obs.shape == baseline_env.observation_space.shape
    assert isinstance(info, dict)
    
    # Take a step
    action = baseline_env.action_space.sample() # Pick a random valid action
    next_obs, reward, done, truncated, step_info = baseline_env.step(action)
    
    # Check step outputs
    assert isinstance(next_obs, np.ndarray)
    assert next_obs.shape == baseline_env.observation_space.shape
    
    assert isinstance(reward, float)
    assert isinstance(done, bool)
    
    assert isinstance(truncated, bool)
    assert isinstance(step_info, dict)
    
    
def test_env_render_rgb_array_baseline():
    
    """Test that the render method correctly returns a numpy array when in rgb_array mode."""
    
    env = CacodemonRecognitionEnv(config_path=0, render="rgb_array", verbose="false")
    env.reset()
    
    frame = env.render()
    
    # 1. Assert it returns an array
    assert isinstance(frame, np.ndarray)
    
    # 2. Assert the shape matches the observation space (Height, Width, Channels)
    assert frame.shape == env.observation_space.shape
    
    # 3. Assert the data type is correct for image pixels
    assert frame.dtype == np.uint8
    
    env.close()


# --- ACTIVE ENVIRONMENT TESTS ---

def test_active_env_initialisation(active_env_standard):
    
    """Test that spaces are properly defined in the active env."""
    
    assert isinstance(active_env_standard.action_space, gym.spaces.Discrete)
    assert isinstance(active_env_standard.observation_space, gym.spaces.Box)


def test_active_env_reset_and_step(active_env_standard):
    
    """Test the core reset and step loop for the active env."""
    
    obs, info = active_env_standard.reset(seed=123)
    
    assert isinstance(obs, np.ndarray)
    assert obs.shape == active_env_standard.observation_space.shape
    
    action = 0  # 0 corresponds to 'ATTACK' 
    next_obs, reward, done, truncated, step_info = active_env_standard.step(action)
    
    assert isinstance(next_obs, np.ndarray)
    assert next_obs.shape == active_env_standard.observation_space.shape
    assert isinstance(reward, float)


def test_active_env_reduction_and_padding_logic(active_env_reduced_padded):
    
    """
    Test that even with 50% reduction and padding, the cv2 logic successfully
    returns an image that matches the expected observation space shape.
    """
    
    obs, _ = active_env_reduced_padded.reset()
    
    # Because the _get_crop_image function either uses cv2.copyMakeBorder 
    # or cv2.resize to push the image back to the original screen dimensions,
    # the output shape should perfectly match the observation space.
    assert obs.shape == active_env_reduced_padded.observation_space.shape
    assert obs.dtype == np.uint8


# --- CACODEMON ALIGNMENT FUNCTION TESTS ---

@pytest.mark.parametrize("env_name", ["active_env_standard", "baseline_env"])
def test_no_cacodemon_alignment_reward(env_name, request):
    
    """Test that the alignment reward is exactly 0.0 when no Cacodemon is visible."""
    
    # This magic line grabs the actual environment object using the string name!
    env = request.getfixturevalue(env_name)
    
    env.reset()
    
    fake_state = MagicMock()
    fake_state.labels = []
    
    fake_game = MagicMock()
    fake_game.get_state.return_value = fake_state
    fake_game.get_screen_width.return_value = 160
    fake_game.get_screen_height.return_value = 120
    
    env.game = fake_game
    
    reward = env._get_cacodemon_alignment_reward()
    assert reward == 0.0


@pytest.mark.parametrize("env_name", ["active_env_standard", "baseline_env"])
def test_perfect_cacodemon_alignment_reward(env_name, request):
    
    """Test that the alignment reward is 1.0 when a Cacodemon is perfectly centered."""
    
    env = request.getfixturevalue(env_name)
    env.reset()
    
    width = 160
    height = 120
    
    fake_label = MagicMock()
    fake_label.object_name = "Cacodemon"
    fake_label.width = 20
    fake_label.height = 20
    fake_label.x = (width / 2) - (fake_label.width / 2)
    fake_label.y = (height / 2) - (fake_label.height / 2)
    
    fake_state = MagicMock()
    fake_state.labels = [fake_label]
    
    fake_game = MagicMock()
    fake_game.get_state.return_value = fake_state
    fake_game.get_screen_width.return_value = width
    fake_game.get_screen_height.return_value = height
    
    env.game = fake_game
    
    reward = env._get_cacodemon_alignment_reward()
    assert reward == 1.0


@pytest.mark.parametrize("env_name", ["active_env_standard", "baseline_env"])
def test_multiple_cacodemon_alignment_reward(env_name, request):
    
    """Test that the highest alignment reward is returned when multiple Cacodemons are visible."""
    
    env = request.getfixturevalue(env_name)
    env.reset()
    
    width = 160
    height = 120
    
    # Far Cacodemon
    far_label = MagicMock()
    far_label.object_name = "Cacodemon"
    far_label.width = 20
    far_label.height = 20
    far_label.x = 0
    far_label.y = 0
    
    # Centered Cacodemon
    centered_label = MagicMock()
    centered_label.object_name = "Cacodemon"
    centered_label.width = 20
    centered_label.height = 20
    centered_label.x = (width / 2) - (centered_label.width / 2)
    centered_label.y = (height / 2) - (centered_label.height / 2)
    
    fake_state = MagicMock()
    fake_state.labels = [far_label, centered_label]
    
    fake_game = MagicMock()
    fake_game.get_state.return_value = fake_state
    fake_game.get_screen_width.return_value = width
    fake_game.get_screen_height.return_value = height
    
    env.game = fake_game
    
    reward = env._get_cacodemon_alignment_reward()
    assert reward == 1.0
    
    
def test_env_render_rgb_array_active():
    
    """Test that the render method correctly returns a numpy array when in rgb_array mode."""
    
    env = CacodemonRecognitionActiveEnv(config_path=0, render="rgb_array", verbose="false")
    env.reset()
    
    frame = env.render()
    
    # 1. Assert it returns an array
    assert isinstance(frame, np.ndarray)
    
    # 2. Assert the shape matches the observation space (Height, Width, Channels)
    assert frame.shape == env.observation_space.shape
    
    # 3. Assert the data type is correct for image pixels
    assert frame.dtype == np.uint8
    
    env.close()