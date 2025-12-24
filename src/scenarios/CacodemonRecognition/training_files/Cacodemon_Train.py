import os
import vizdoom as vzd
import random
from time import sleep
from pprint import pprint

import torch
from torch import nn, optim, distributions
import torch.nn.functional as F

import json
#from model import PPO - will need to see how to implement this


#STATIC VARIABLES

TARGET = "DeadCacodemon"
REWARD_TARGET_KILL = 20
PENALTY_WRONG_KILL = -10
LIVING_REWARD = -0.01

learning_rate = 0.0001
accumulate_episodes = 16



if __name__ == "__main__":

    #Initliase ViZDoom instance and set game variables
    game = vzd.DoomGame()

    game.set_screen_resolution(vzd.ScreenResolution.RES)
    game.set_objects_info_enabled(True)

    #game.load_config("/home/battmannwann/Projects/Individual Project/The-VizDoom-Experience/src/scenarios/CacodemonRecognition/config_files/Cacodemon_Recognition.cfg")
    game.load_config("../config_files/Cacodemon_Recognition_basic.cfg")
    game.init()

    available_buttons = game.get_available_buttons()

    if not available_buttons:
        raise RuntimeError("No available buttons found. Check your .cfg file!")

    action = [False] * len(available_buttons)
    action[random.randint(0, len(available_buttons)-1)] = True

    print("Available buttons:", game.get_available_buttons())
    print("Available actions:", len(game.get_available_buttons()))


    def get_enemies(state, verbose = False):
        """Return dict of enemies (id -> name, position)."""
        enemies = {}

        if state.objects is not None:
            for obj in state.objects:

                if obj.name not in ["DoomPlayer", "BulletPuff", "GreenTorch"]:

                    id = obj.id
                    name = obj.name
                    position = (obj.position_x, obj.position_y, obj.position_z)

                    enemies[id] = {"Name": name, "position": position}

                    if verbose == True:

                        print("-" * 50)
                        print(f"ID: {obj.id}")
                        print(f"Name: {obj.name}")
                        print(f"Position: ({obj.position_x}, {obj.position_y}, {obj.position_z})")
                        print("-" * 50)

        
        else:
            print("No enemies information available.")
                
        
        return enemies

    episodes = 5
    overall_killed = []
    enemies_list = []

    #If the agent kills the n required cacodemons, counts as a 'successful episode'
    successful_episodes = 0

    for ep in range(episodes):
        
        print(f"\n=== Episode {ep+1} ===")
        game.new_episode()

        success = 0

        while not game.is_episode_finished():

            state = game.get_state()
            current_enemies = get_enemies(state, False)

            enemies_list = current_enemies if len(enemies_list) == 0 and current_enemies != None else enemies_list

            print(f"\n\n{"-" * 40}\nAvailable enemies are: \n {pprint(current_enemies)}")

            # Find which enemies have been killed (game replaces enemy name with "Dead" + "NameHere")
            killed = [ID for ID in current_enemies if "Dead" in current_enemies[ID]["Name"]]

            for eid in killed:

                if eid not in overall_killed:
                    overall_killed.append(eid)

            reward = LIVING_REWARD

            for eid in killed:
                killed_name = current_enemies[eid]["Name"]

                if killed_name == TARGET:
                    reward += REWARD_TARGET_KILL
                    print(f"Killed target: {killed_name[4:]}_{eid} (+{REWARD_TARGET_KILL})")

                    success += 1
                    

                else:
                    reward += PENALTY_WRONG_KILL
                    print(f"Killed wrong type: {killed_name[4:]}_{eid} ({PENALTY_WRONG_KILL})")

            # Example random action (replace with your RL agent)
            action = [False] * len(game.get_available_buttons())
            action[random.randint(0, len(action)-1)] = True
            
            if sleep_time > 0:
                    sleep(sleep_time)

            reward += game.make_action(action)

            successful_episodes += 1 if success == 2 else 0

        print(f"\n\n {"=" * 50}\n Episode total reward: {game.get_total_reward()}\n Enemies Available: {pprint(enemies_list)}\n Enemies Killed IDs: {overall_killed}\n{"=" * 50}\n Successful Episodes: {successful_episodes}/{episodes}\n")

    game.close()
