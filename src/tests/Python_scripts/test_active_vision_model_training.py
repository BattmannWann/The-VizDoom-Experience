import pytest
from stable_baselines3.common.vec_env import VecFrameStack

from active_vision_model_training.active_visual_model_training_lvl_1 import linear_lr_schedule, make_env


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


## --- TEST 2: Environment Creation --- ##

def test_make_env_structure():
    """Test that make_env returns the correctly wrapped environment."""
    env = make_env()
    
    # Check that it successfully stacked 4 frames
    assert isinstance(env, VecFrameStack)
    
    # We can also check if the observation space is what we expect for a CnnPolicy (Box)
    assert len(env.observation_space.shape) == 3 # Should be (Channels, Height, Width)
    
    # Clean up the environment after testing
    env.close()