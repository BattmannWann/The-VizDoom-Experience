import vizdoom as vzd
import random
from time import sleep
from pprint import pformat
import numpy as np


"""
This is a very simple file to quickly demonstrate the WAD files and what an agent would see.

This will be used as the base idea for implementation of the Gymnasium environment and model training using Stable Baselines 3.

To view different config files, simply change the index of the list inside the `game.load_config()` method. For ease of viewing, there has been a sleep time
established for during the episode. 

This short example shows what enemies are available, where they are, if they have been killed, and if an episode has been successful
(i.e. the agent managed to kill the n number of Cacodemon enemies present). 

"""




#STATIC VARIABLES

TARGET = "DeadCacodemon"
REWARD_TARGET_KILL = 250
PENALTY_WRONG_KILL = -100
LIVING_REWARD = 0
VISUAL_ALIGNMENT_SCALE = 0.02

SLEEP_TIME =  0.01 #0.028

scenario_configs = ["../config_files/Cacodemon_Recognition_most_basic.cfg", 
                    "../config_files/Cacodemon_Recognition_basic.cfg", 
                    "../config_files/Cacodemon_Recognition_Final.cfg"]



if __name__ == "__main__":

    #Initialise ViZDoom instance and set game variables
    game = vzd.DoomGame()

    game.set_screen_resolution(vzd.ScreenResolution.RES_800X450)
    game.set_objects_info_enabled(True)

    #game.load_config("/home/battmannwann/Projects/Individual Project/The-VizDoom-Experience/src/scenarios/CacodemonRecognition/config_files/Cacodemon_Recognition.cfg")
    game.load_config(scenario_configs[0])
    
    game.init()

    available_buttons = game.get_available_buttons()

    if not available_buttons:
        raise RuntimeError("No available buttons found. Check your .cfg file!")

    action = [False] * len(available_buttons)
    action[random.randint(0, len(available_buttons)-1)] = True
    
    print(f"\n\nVariables = {game.get_available_game_variables()}\n\n")

    print("Available buttons:", game.get_available_buttons())
    print("Available actions:", len(game.get_available_buttons()))


    def get_enemies(state, verbose = False):
        """Return dict of enemies (id -> name, position)."""
        enemies = {}

        if state:

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
    
    
    def _get_cacodemon_alignment_reward(game):
    
        state = game.get_state()
        
        width = game.get_screen_width()
        height = game.get_screen_height()
        
        screen_cx = width / 2
        screen_cy = height / 2
        
        if state is None or state.labels is None:
            return 0.0
        
        rewards = []
        
        for lab in state.labels:
            
            if lab.object_name.lower() in ["cacodemon", "cyberdemon", "lost soul", "pain elemental", "zombieman"]:
                
                cx = lab.x + lab.width / 2
                cy = lab.y + lab.height / 2
                
                dx = abs(cx - screen_cx) / screen_cx
                dy = abs(cy - screen_cy) / screen_cy
                
                distance = np.sqrt(dx * dx + dy * dy)
                alignment = max(0.0, 1.0 - distance)
                
                rewards.append(alignment)
                
        return max(rewards, default = 0.0)
        
        
    def get_game_variables():

        return game.get_game_variable(vzd.GameVariable.USER2), game.get_game_variable(vzd.GameVariable.USER3)

    

    episodes = 5
    overall_killed = []
    enemies_list = []
    
    overall_total_reward = 0

    #If the agent kills the n required cacodemons, counts as a 'successful episode'
    successful_episodes = 0

    for ep in range(episodes):
        
        print(f"\n=== Episode {ep+1} ===")
        game.new_episode()

        success = 0
        
        while not game.is_episode_finished(): 

            state = game.get_state()
            current_enemies = get_enemies(state, False)

            reward = LIVING_REWARD
            enemies_list = current_enemies if len(enemies_list) == 0 and current_enemies != None else enemies_list

            #print(f" \n\n {'-' * 40} \nAvailable enemies are: \n {pformat(current_enemies)} ")

            # Find which enemies have been killed (game replaces enemy name with "Dead" + "NameHere")
            killed = [ID for ID in current_enemies if "Dead" in current_enemies[ID]["Name"]]

            for eid in killed:

                if eid not in overall_killed:
                    overall_killed.append(eid)


            for eid in killed:
                killed_name = current_enemies[eid]["Name"]

                if killed_name == TARGET:
                    reward += REWARD_TARGET_KILL
                    #print(f"Killed target: {killed_name[4:]}_{eid} (+{REWARD_TARGET_KILL})")

                    success += 1
                    

                else:

                    reward += PENALTY_WRONG_KILL
                    #print(f"Killed wrong type: {killed_name[4:]}_{eid} ({PENALTY_WRONG_KILL})")
                    

            # Example random action (replace with your RL agent)
            action = [False] * len(game.get_available_buttons())
            action[random.randint(0, len(action)-1)] = True
            
            if SLEEP_TIME > 0:
                    sleep(SLEEP_TIME)

            _ = game.make_action(action)
            #print(f"Reward: {reward}")
            
            
            alignment = _get_cacodemon_alignment_reward(game)
            reward += 0.02 * alignment
            
            #print("Agent looked at a thing, reward added: ", 0.02 * alignment)

            successful_episodes += 1 if success == 2 else 0

        total_bullets, bullets_used = get_game_variables()
        bullets_delta = total_bullets - bullets_used

        if bullets_used > 0:
            reward -= 5 * bullets_used

        print(f"\n\n {'=' * 50}\n Episode total reward: {reward}\n Enemies Available: \n{pformat(enemies_list)}\n")
        print(f"Enemies Killed IDs: {overall_killed}\n{'=' * 50}\n Successful?: {'yes' if success else 'no'}")
        print(f"Bullets Used: {bullets_used}\n")

        overall_total_reward += reward


    game.close()

    print(f"\n\nOverall reward after {episodes} episodes was: {overall_total_reward}")
    print(f"Successful Episodes: {successful_episodes}/{episodes}\n")