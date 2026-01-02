import vizdoom as vzd
import random
from time import sleep
from pprint import pformat


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
REWARD_TARGET_KILL = 20
PENALTY_WRONG_KILL = -10
LIVING_REWARD = -0.01

SLEEP_TIME = 0

learning_rate = 0.0001
accumulate_episodes = 16

scenario_configs = ["../config_files/Cacodemon_Recognition_most_basic.cfg", 
                    "../config_files/Cacodemon_Recognition_basic.cfg", 
                    "../config_files/Cacodemon_Recognition_Final.cfg"]



if __name__ == "__main__":

    #Initialise ViZDoom instance and set game variables
    game = vzd.DoomGame()

    game.set_screen_resolution(vzd.ScreenResolution.RES_800X450)
    game.set_objects_info_enabled(True)

    #game.load_config("/home/battmannwann/Projects/Individual Project/The-VizDoom-Experience/src/scenarios/CacodemonRecognition/config_files/Cacodemon_Recognition.cfg")
    game.load_config(scenario_configs[2])
    
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

            print(f" \n\n {'-' * 40} \nAvailable enemies are: \n {pformat(current_enemies)} ")

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
            
            if SLEEP_TIME > 0:
                    sleep(SLEEP_TIME)

            reward += game.make_action(action)

            successful_episodes += 1 if success == 2 else 0

        print(f"\n\n {'=' * 50}\n Episode total reward: {game.get_total_reward()}\n Enemies Available: \n{pformat(enemies_list)}\n")
        print(f"Enemies Killed IDs: {overall_killed}\n{'=' * 50}\n Successful Episodes: {successful_episodes}/{episodes}\n")

    game.close()
