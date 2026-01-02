import gymnasium as gym
from gymnasium import spaces
import numpy as np
import vizdoom as vzd
from time import sleep


class CacodemonRecognitionEnv(gym.Env):
    
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 35}
    
    def __init__(self, config_path, render = "human"):
        
        """
        Constructor for the Cacodemon Recognition Scenario Environment.
        
        Parameters:
            config_path: Integer that corresponds to config index in the `scenario_configs` list. This will be explained on using flag `--help`
            render: Selects the render mode; i.e. human (displays game window), rgb_array (raw pixel input passed to model)...

        """
        
        super().__init__()
        
        scenario_configs = [
            "../config_files/Cacodemon_Recognition_most_basic.cfg", 
            "../config_files/Cacodemon_Recognition_basic.cfg", 
            "../config_files/Cacodemon_Recognition_Final.cfg"
        ]
        
        #passed parameters checks...
        
        #assert type(config_path) == int and 0 <= config_path < len(scenario_configs), f"\n\nconfig_path NEEDS to be an integer as you accessing a list. Range is within 0-{len(scenario_configs)}\n\n" 
        #assert render in self.metadata["render_modes"], f"\n\nIncorrect render mode provided, needs to be: {self.metadata["render_modes"]}\n\n"
        
        
        #Game initialisation
        
        self.game = vzd.DoomGame()
        self.game.load_config(scenario_configs[config_path])
        
        #This section could be used to define game settings, but this is handled by the config file(s)
        #To maintain this separation, conditions will NOT be set here unless strictly necessary
        
        #Should be set by the config, using these print statements to test 
        print(f"\n\nAvailable buttons: {[b.name for b in self.game.get_available_buttons()]}\n\n")  
        
        print(f"\n\nAvailable game variables: {[v.name for v in self.game.get_available_game_variables()]}\n\n") 
        
        # Sets the living reward (for each move) to -1; this may need altered or removed depending on how training goes
        #self.game.set_living_reward(-0.1)
        
        self.game.init()
        
        
        # Gym initiation
        
        # Action Space
        available_actions = len(self.game.get_available_buttons())
        self.action_space = spaces.Discrete(available_actions)
        
        #Observation space
        
        screen_width = self.game.get_screen_width()
        screen_height = self.game.get_screen_height()
        
        self.observation_space = spaces.Box(
            
            low = 0,
            high = 255,
            shape = (screen_height, screen_width, 3),
            dtype = np.uint8
        )
        
        
    def _get_obs(self):
        return self.game.get_state().screen_buffer
    
    
    def step(self, action):
        
        # Convert a discrete action into a ViZDoom format for buttons
        action_vector = [False] * self.action_space.n
        action_vector[action] = True
        
        _ = self.game.make_action(action_vector)
        done = self.game.is_episode_finished()
        
        print(f"\n\n Action reward: {reward}, Total reward: {self.game.get_total_reward()}\n\n")
        
        state = self.game.get_state()
        current_user_reward = 0
        
        current_user_reward = state.game_variables[0] if state else 0
        reward = current_user_reward - self.last_user_reward
        self.last_user_reward = current_user_reward
        
        print(f"\n\nUSER1 Total: {current_user_reward}, \nStep Reward: {reward}\n\n")

        
        
        if not done:
            obs = self._get_obs()
            
        else:
            obs = np.zeros(self.observation_space.shape, dtype = np.uint8)
        
        #Extra information can be added here. E.g. info for debugging...
        info = {}
        
        #returns the observation, the given reward, if the episode has finished, if truncation, and the information dictionary
        return obs, reward, done, False, info
    
    
    def reset(self, seed = None, options = None):
        
        super().reset(seed = seed)
        
        self.last_user_reward = 0
        
        self.game.new_episode()
        obs = self._get_obs()
        
        return obs, {}
        
        
        
        


    