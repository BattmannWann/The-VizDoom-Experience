"""
                                                                   
"""

from stable_baselines3 import PPO
from envs.Cacodemon_recognition_env import CacodemonRecognitionEnv
from time import sleep

import argparse

def run(args):
        
    env = CacodemonRecognitionEnv(
    config_path = 0,
    render = "human",
    ) 
        
    model = PPO.load(args.in_model_path, device = "cpu")
    
    
    for ep in range(args.episodes):
        
        obs, info = env.reset()
        done = False
        
        while not done:
            
            action, _ = model.predict(obs)
            obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
            
            if args.sleep > 0.0:
                
                sleep(args.sleep)
            
    env.close()
    
    
    


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description = """
            \n\n
            This file is for running trained models on the Cacodemon Recognition scenario task. Models run here ARE NOT trained any further.
            Demonstrations will run for --episodes, and an informative message on how well the model performed provided. 
              
            """,
            
            epilog = "Example: python run_model.py --in-model-path ../models/Cacodemon_Recognition_10.zip --episodes 5 --sleep 0.038")
    
    
    parser.add_argument("--in-model-path", type = str, required = True)
    parser.add_argument("--episodes", type = int, required = False, default = 5, help = "Total number of episodes to run for. The default is 5")
    
    parser.add_argument("--sleep", type = float, required = False, default = 0.0, 
                        help = """how long the engine should pause for after every action. 
                        The default is 0, which will display a very fast running agent. To view it as though it was a person playing, set it to 0.038""")
    

    args = parser.parse_args()
    run(args)