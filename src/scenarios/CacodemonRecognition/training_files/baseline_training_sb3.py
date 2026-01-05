from stable_baselines3 import PPO
import gymnasium as gym
import os
import sys

sys.path.append("../envs")

from envs.Cacodemon_recognition_env import CacodemonRecognitionEnv

models_directory = "../models"
logs_directory = "../logs"

if not os.path.exists(models_directory):
    os.makedirs(models_directory)
    
if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)

# Hyperparameters
learning_rate = 3e-4 #Adam optimiser default
steps = 512
batch_size = 64
epochs = 4
timesteps = 10000 #how often do we want the model to be saved? 
gamma = 0.995
gae_lambda = 0.95
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5

training_repeats = 1000


env = CacodemonRecognitionEnv(
    config_path = 0,
    render = "human"
)


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

model = PPO(
    
    policy = "CnnPolicy",
    env = env,
    learning_rate = learning_rate,
    n_steps = steps,
    batch_size = batch_size,
    gamma = gamma,
    gae_lambda = gae_lambda,
    clip_range = clip_range,
    ent_coef = ent_coef,
    vf_coef = vf_coef,
    verbose = 1,
    tensorboard_log = logs_directory
)

# training loop, model saves every `timesteps` and is trained `training_repeats` times...
# to make sure that the model is NOT reset after `timesteps`, we need to pass in `reset_num_timesteps = False`
# and to make sure we don't save model at 0 timesteps, have the range start from 1

print("\n\nBeginning training for Cacodemon Recognition scenario...\n\n")

for i in range(1, training_repeats):
    
    print(f"{'=' * 40}")
    print(f"Training iteration {i}:\n\n")

    model.learn(total_timesteps = timesteps, reset_num_timesteps = False, tb_log_name = f"Cacodemon_Recognition_0_1")
    model.save(f"{models_directory}/model_{training_repeats * i}")
    

print(f"{'=' * 40}\n\n")

print(f"Training has completed. \nRan for: {training_repeats * timesteps} timesteps")