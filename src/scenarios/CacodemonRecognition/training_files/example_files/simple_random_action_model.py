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

#Variables

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


    def get_game_variables():

        return game.get_game_variable(vzd.GameVariable.USER1), game.get_game_variable(vzd.GameVariable.USER2), game.get_game_variable(vzd.GameVariable.USER3)


    episodes = 5
    overall_total_reward = 0

    for ep in range(episodes):
        
        print(f"\n=== Episode {ep+1} ===")
        game.new_episode()

        success = 0
        running_reward = 0

        while True: 

            if game.is_episode_finished() == True:

                actual_reward, _, _ = get_game_variables()
                running_reward += actual_reward

                overall_total_reward += actual_reward

                break

            # Example random action (replace with your RL agent)
            action = [False] * len(game.get_available_buttons())
            action[random.randint(0, len(action)-1)] = True
            
            if SLEEP_TIME > 0:
                    sleep(SLEEP_TIME)

            _ = game.make_action(action)

            #actual_reward, total_bullets, bullets_used = get_game_variables()
            #print(f"Actual reward = : {actual_reward}")

        print(f"\n\nEpisode total reward: {running_reward}\n")
        
        

    game.close()

    print(f"{'=' * 50}\n\nOverall reward after {episodes} episodes was: {overall_total_reward}")