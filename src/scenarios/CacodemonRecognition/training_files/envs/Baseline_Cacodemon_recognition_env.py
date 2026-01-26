import gymnasium as gym
from gymnasium import spaces
import numpy as np
import vizdoom as vzd
from time import sleep


class CacodemonRecognitionEnv(gym.Env):
    
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 35}
    
    def __init__(self, config_path, render = "human", reward_scale_factor = 1000.0, seed = None, verbose = "false"):
        
        """
        Constructor for the Cacodemon Recognition Scenario Environment.
        
        Parameters:
            config_path: Integer that corresponds to config index in the `scenario_configs` list. This will be explained on using flag `--help`
            render: Selects the render mode; i.e. human (displays game window), rgb_array (raw pixel input passed to model)...
            reward_scale_factor: How much should the reward be down-scaled by (this handles floats as ACS does not provide floating point arithmetic)

        """
        
        super().__init__()
        
        self.render_mode = render
        
        self.verbose = verbose.lower()
        
        self._seed = seed
        self.reward_scale = reward_scale_factor
        
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
        
        if self.verbose == "true":
            
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
        
        self.screen_width = self.game.get_screen_width()
        self.screen_height = self.game.get_screen_height()
        
        self.observation_space = spaces.Box(
            
            low = 0,
            high = 255,
            shape = (self.screen_height, self.screen_width, 3),
            dtype = np.uint8
        )
        
        self.action_space.seed(None)
        self.observation_space.seed(None)
        
        
    def _get_obs(self):
        return self.game.get_state().screen_buffer
    
    
    def _get_cacodemon_alignment_reward(self):
        
        """
        determines whether the agent is looking at a cacodemon or not. 
        
        Returns 1.0 for it being perfectly centred and 0.0 if it is far away or not visible
        """
    
        state = self.game.get_state()
        
        width = self.game.get_screen_width()
        height = self.game.get_screen_height()
        
        screen_cx = width / 2
        screen_cy = height / 2
        
        if state is None or state.labels is None:
            return 0.0
        
        rewards = []
        
        for lab in state.labels:
            
            if lab.object_name.lower() in ["cacodemon"]: #, "cyberdemon", "lostsoul", "painelemental", "zombieman"]:
                
                cx = lab.x + lab.width / 2
                cy = lab.y + lab.height / 2
                
                dx = abs(cx - screen_cx) / screen_cx
                dy = abs(cy - screen_cy) / screen_cy
                
                distance = np.sqrt(dx * dx + dy * dy)
                alignment = max(0.0, 1.0 - distance)
                
                rewards.append(alignment)
                
        return max(rewards, default = 0.0)
        
    
    def step(self, action):
        
        info = {}
        
        # Convert a discrete action into a ViZDoom format for buttons
        action_vector = [False] * self.action_space.n
        action_vector[action] = True
        
        _ = self.game.make_action(action_vector, 4)

        reward = self.game.get_game_variable(vzd.GameVariable.USER1) / self.reward_scale
        
        alignment = self._get_cacodemon_alignment_reward()
        reward += 0.01 * alignment
        
        done = self.game.is_episode_finished()
        
        if self.verbose == "true":
            print(f"\n\n Action reward: {reward}, reward_scale = {self.reward_scale}")    
            
        
        if not done:
            obs = self._get_obs()
            
        else:
            obs = np.zeros(self.observation_space.shape, dtype = np.uint8)
            info["reward"] = reward
        
        #returns the observation, the given reward, if the episode has finished, if truncation, and the information dictionary
        return obs, reward, done, False, info
    
    

    def render(self):
        
        if self.render_mode == "human":
            #Since the ViZDoom software already provides the ability to show the game window to monitor the agent
            pass 
        
        elif self.render_mode == "rgb_array":
            return self._get_obs()
    
    
    def reset(self, seed = None, options = None):
        
        seed = self._seed
        
        super().reset(seed = seed)
        
        if seed is not None:
            
            self.action_space.seed(seed)
            self.observation_space.seed(seed)
            self.game.set_seed(seed)
        
        self.game.new_episode()
        obs = self._get_obs()
        
        return obs, {}
        
        
        
        


    