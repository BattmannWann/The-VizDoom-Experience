from stable_baselines3 import PPO
import gymnasium as gym
import os
import sys
import numpy as np
from stable_baselines3.common.vec_env import DummyVecEnv, VecNormalize, VecFrameStack, VecTransposeImage
from stable_baselines3.common.monitor import Monitor
from typing import Callable
from envs.Baseline_Cacodemon_recognition_env import CacodemonRecognitionEnv

## Directory Checks and Creation

sys.path.append("../envs")

models_directory = "../models_baseline/CacodemonRecognition_30"
logs_directory = "../logs"

if not os.path.exists(models_directory):
    os.makedirs(models_directory)
    
else:
    
    contin = False
    
    while contin != True:
        
        print(f"There is already a directory with the name: {models_directory}")
        contin = True if input("Do you still want to continue? [Y/N]: ").lower() == "y" else exit(0)
        
    
if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)   


##Functions

def make_env():
    
    base = CacodemonRecognitionEnv(config_path = 1, render = "rgb_array")
    base = Monitor(base, filename = os.path.join(f"{logs_directory}/env_monitors", "env_monitor_30.csv")) 
    
    env = DummyVecEnv([lambda: base])
    env = VecTransposeImage(env)
    env = VecFrameStack(env, n_stack = 4)
    
    return env


def linear_lr_schedule(initial_value: float, final_value: float = 1e-6, warmup_ratio: float = 0.05) -> Callable[[float], float]:
    
    """
    Function for producing a linear learning rate (lr) schedule from initial_value to final_value. 
    
    The method used uses a warmup and steady decay sequence to ensure the model isn't disadvantaged.
    
    Parameters:
        initial_value -> The initial learning rate value
        
    Returns:
        A schedule that computes the current learning rate given remaining progress
    """
    
    assert 0.0 <= warmup_ratio < 1.0, "LR must be NON negative and less than 1.0"
    
    def schedule(progress_remaining: float) -> float:
        
        """
        Progress starts at 1.0 and decays to 0.0
        """
        progress_done = 1.0 - progress_remaining
        
        if progress_done < warmup_ratio:
            return initial_value * (progress_done / warmup_ratio)
        
        decay_done = (progress_done - warmup_ratio) / max(1e-8, (1.0 - warmup_ratio))
        
        return final_value + (initial_value - final_value) * (1.0 - decay_done)
    
    return schedule

# Hyperparameters

"""

SB3 Default values:

    self,
    policy: str | type[ActorCriticPolicy],
    env: GymEnv | str,
    learning_rate: float | Schedule = 3e-4,
    n_steps: int = 2048,
    batch_size: int = 64,
    n_epochs: int = 10,
    gamma: float = 0.99,
    gae_lambda: float = 0.95,
    clip_range: float | Schedule = 0.2,
    clip_range_vf: None | float | Schedule = None,
    normalize_advantage: bool = True,
    ent_coef: float = 0.0,
    vf_coef: float = 0.5,
    max_grad_norm: float = 0.5,
    use_sde: bool = False,
    sde_sample_freq: int = -1,
    rollout_buffer_class: type[RolloutBuffer] | None = None,
    rollout_buffer_kwargs: dict[str, Any] | None = None,
    target_kl: float | None = None,
    stats_window_size: int = 100,
    tensorboard_log: str | None = None,
    policy_kwargs: dict[str, Any] | None = None,
    verbose: int = 0,
    seed: int | None = None,
    device: th.device | str = "auto",
    _init_setup_model: bool = True,

Recommended Value Ranges for all Hyperparameters:
    
    - Horizon range (n_steps): 32 - 5000
    - Minibatch range: 4 - 4096
    - Epoch range: 3 - 30
    
    - Clipping range: 0.1, 0.2, 0.3 
    - KL Target range: 0.003 - 0.03
    - KL Initiation range: 0.3 - 1 
    - Discount Factor Gamma range: 0.99 (Most Common), or 0.8 - 0.9997
    - GAE (Generalised Advantage Estimator) Lambda range: 0.9 to 1
    
    - Value Function Coefficient (c1) range: 0.5, 1
    - Entropy Coefficient range (c2): 0 - 0.01
    
    - Learning Rate range: 0.003 - 5e-6 
 
"""


learning_rate = 3e-4  #3e-4 #Adam optimiser default # 0.0001
steps = 2048
batch_size = 32 #512
epochs = 15
timesteps = 25000 #100000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5, warmup_ratio = 0.1)
#lr_schedule = linear_lr_schedule(initial_value = 7.5e-5, final_value = 3e-5, warmup_ratio = 0.1)

env = make_env()

env.seed(123)
env.reset()


"""
Model Parameters:

    Small note: Policies have been 'abused' here in terms of meaning and aren't used in the same way as in RL. See here for more info:
    https://stable-baselines3.readthedocs.io/en/master/guide/custom_policy.html

    Policy: Policies that SB3 offer are as follows:

            - MlpPolicy: Suitable for low-dimensional vectors. It is a fully connected neural network with no convolution and no spatial inductive bias. 
                         An example observation space for this policy is as follows: 
                         
                         `observation_space = Box(shape = (N,), dtype = float)`
                         
                         Use cases:
                         
                            - State vectors (positions, velocities, angles)
                            - Game variables only (for ViZDoom e.g. health, ammo)
                            - Classical control tasks
            
            
            - CnnPolicy: Convolutional Neural Network (as the name implies), which can learn spatial features. This works best for raw pixel inputs (images) since
                         the assumed observation space is of:

                        `observation_space = Box(shape = (H, W, C), dtype = uint8)`
                        
                        This is the best choice for this problem since the scenario requires the agent to learn visual appearance, relative positioning, 
                        and motion across frames. 
            
            
            - MultiInputPolicy: Combines multiple encoders, usually a CNN for images and MLP for vectors. Use cases derive from:
            
                                    - Pixels and game variables
                                    - Pixels and depth
                                    - Pixels and inventory
                                    - ...
                                    
                                

"""

model = PPO.load(
    
    path = "../models_baseline/CacodemonRecognition_5/model_5700000.zip",
    env = env,
    seed = 123,
    verbose = 1,
    tensorboard_log = logs_directory,
    
    custom_objects = {
        "learning_rate":lr_schedule,
        "n_steps": steps,
        "batch_size": batch_size,
        "gamma": gamma,
        "gae_lambda": gae_lambda,
        "clip_range": clip_range,
        "ent_coef": ent_coef,
        "vf_coef": vf_coef,
        "max_grad_norm": max_grad_norm,
        "target_kl": target_kl
    
    }
)





# training loop, model saves every `timesteps` and is trained `training_repeats` times...
# to make sure that the model is NOT reset after `timesteps`, we need to pass in `reset_num_timesteps = False`
# and to make sure we don't save model at 0 timesteps, have the range start from 1



print("\n\nBeginning training for Cacodemon Recognition scenario...\n\n")

print("n_steps:", model.n_steps, "batch_size:", model.batch_size)
print("num_envs:", model.get_env().num_envs)


for i in range(1, training_repeats):
    
    print(f"{'=' * 40}")
    print(f"Training iteration {i}:\n\n")

    model.learn(total_timesteps = timesteps, reset_num_timesteps = False, tb_log_name = f"Cacodemon_Recognition_30")
    model.save(f"{models_directory}/model_{timesteps * i}")
    

print(f"{'=' * 40}\n\n")

print(f"Training has completed. \nRan for: {training_repeats * timesteps} timesteps")

env.close()