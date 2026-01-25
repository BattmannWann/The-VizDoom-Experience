"""
                                                                   
"""

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, VecFrameStack, VecTransposeImage
from envs.Baseline_Cacodemon_recognition_env import CacodemonRecognitionEnv
from envs.Active_Visual_Cacodemon_Recognition_env import CacodemonRecognitionActiveEnv
from time import sleep
from pprint import pformat
import os
import argparse

def write_to_file(file_path, write_mode, content):
    
    try:
    
        with open(file_path, write_mode) as f:
            
            f.write(content)
            
        print("Successfully written to file!")
            
    except Exception as e:
        
        print(f"ERROR WRITING TO FILE: {file_path},\nsee: {e}")
        
    
def make_env(base):
    
    env = DummyVecEnv([lambda: base])
    env = VecTransposeImage(env)
    env = VecFrameStack(env, n_stack = 4)
    
    return env


def run(args):
    
    if args.active.lower() == "true":
    
        env = CacodemonRecognitionActiveEnv( 
        config_path = args.config_path,
        render = "human",
        #seed = 123,
        verbose = args.verbose
        ) 
        
    else:
        
        env = CacodemonRecognitionEnv(
            config_path = args.config_path,
            render = "human",
            #seed = 123,
            verbose = args.verbose 
        )
        
    env = make_env(env)
    model = PPO.load(args.in_model_path)
    
    overall_rewards = []
    
    for ep in range(args.episodes):
        
        obs = env.reset()
        done = False
        
        while True:
            
            if done:
                
                print(f"\n{'=' * 40}\n Final reward for episode {ep} was: {infos[0]['reward']}\n{'=' * 40}\n")
                overall_rewards.append({f"Episode {ep}": infos[0]["reward"]})
                break
                
            action, _ = model.predict(obs, deterministic = True)
            obs, rewards, dones, infos = env.step(action)
            done = bool(dones)
            
            if args.sleep > 0.0:
                
                sleep(args.sleep)
            
    env.close()
    
    output_msg = f"\n\n{'=' * 40}\nOverall Rewards: \n{pformat(overall_rewards)}\n{'=' * 40}\n\n"
    print(output_msg)
    
    
    if args.output.lower() != "false":
        
        created = False
        write_mode = None
        
        file_name = args.output
        file_path = f"output_files/{file_name}.txt"
    
        if not os.path.exists(file_path):
            
            while created == False:
            
                try:
                
                    open(f"output_files/{file_name}.txt", "x")
                    created = True
                    write_mode = "w"
                    
                    final_file_path = f"output_files/{file_name}.txt"
                    
                except Exception as e:
                    
                    print(f"ERROR, Creating File: {file_path} was unsuccessful. See:\n{e}")
                    ans = input("Do you want to try again? [Y/N]: ")
                    
                    if ans.lower() == "n":
                        
                        exit(0)
                        
                    else:
                        
                        file_name = input("Please enter a name for the file: ").lower()
                        
            write_to_file(final_file_path, write_mode, output_msg.strip("\n"))
            
            
        else:
            
            while True:
                
                ans = input(f"File: {f'output_files/{args.output}.txt'} already exists. Would you like to continue? [Y/N]: ")
                
                if ans.lower() == "y": 
                    
                    write_to_file(file_path = file_path, write_mode = "a", content = output_msg.strip("\n"))
                    break
                            
                else:
                    exit(0)
    
    


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
    
    
    parser.add_argument("--active", type = str, required = False, help = "Should this be running an active or baseline model? Pass in True or False.", default = "False")
    
    parser.add_argument("--config-path", type = int, 
                        required = False, 
                        help = "Enter one of the following: 0 for `Cacodemon_Recognition_most_basic.cfg`  1 for `..._basic.cfg`  and 2 for `..._Final.cfg`. Default is 0.",
                        default = 0)
    
    parser.add_argument("--verbose", type = str, required = False, default = "false", help = "Set optional print messages during model evaluation.")
    
    parser.add_argument("--output", type = str, required = False, default = "false", help = "Provide a file to write the output of model performance to. Default: false")
    
    args = parser.parse_args()
    run(args)