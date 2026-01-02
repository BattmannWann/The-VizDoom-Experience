"""
                                                                   
"""

import os
from time import sleep

import vizdoom as vzd
from stable_baselines3 import PPO
from envs.Cacodemon_recognition_env import CacodemonRecognitionEnv

import argparse

def run(args):
    
    if args.help_me:
        
        print(
            
            """
            \n\n
            This file is for running trained models on the Cacodemon Recognition scenario task. Models run here ARE NOT trained any further.
            Demonstrations will run for 5 episodes, and an informative message on how well the model performed provided. 
            
            
            The arguments that can be passed in are as follows:
            
                --in-model-path: Specifies the path for the model that you want to run. For example, --in-model-path Cacodemon_Recognition_baseline.zip
                
                --sleep: Specifies a sleep time before each action (this would help to watch the model perform instead of it looking like a timelapse)
                
                --help: Returns the "docstring" for the file and specifies the arguments/flags that can be passed in
              
            """
        )
        
    env = CacodemonRecognitionEnv(
    config_path = 0,
    render = "human"
    ) 
        
    model = PPO.load(args.in_model_path, env = env)
    
    episodes = 5
    
    for ep in range(episodes):
        
        obs = env.reset()
        done = False
        
        while not done:
            
            env.render()
            action, _ = model.predict(obs)
            obs, reward, done, info = env.step(action)
            
    env.close()
    
    
    


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--in-model-path", type = str, required = True)
    parser.add_argument("--sleep", type = int, required = False)
    parser.add_argument("--help-me", action = "store_true")

    args = parser.parse_args()
    run(args)