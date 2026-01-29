import gymnasium as gym
from gymnasium import spaces
import numpy as np
import vizdoom as vzd
from time import sleep
import cv2


class CacodemonRecognitionActiveEnv(gym.Env):
    
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
        #self.game.set_window_visible(False)
        
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
        
        self.screen_width = self.game.get_screen_width() #160
        self.screen_height = self.game.get_screen_height() #120
        
        if verbose == "true":
            print(f"Screen dimensions, Height: {self.screen_height}, Width: {self.screen_width}")
            

        """
        SCALE REDUCTIONS
        
        Original (100%): 160x120
        80%            : 128x96
        60%            : 96x72
        40%            : 64x48
        20%            : 32x24
        10%            : 16x12
        5%             : 8x6
        1%             : 1x1
        
        """
        

        
        self.width_crop, self.height_crop,  = 64, 48
        
        self.observation_space = spaces.Box(
            
            low = 0,
            high = 255,
            shape = (self.screen_height, self.screen_width, 3),
            dtype = np.uint8
        )
        
        self.action_space.seed(None)
        self.observation_space.seed(None)


    def _get_crop_image(self, frame):

        height, width, channels = frame.shape

        y1 = (height - self.height_crop) // 2
        y2 = y1 + self.height_crop

        x1 = (width - self.width_crop) // 2
        x2 = x1 + self.width_crop

        #crop = frame[y1:y2, x1:x2]
        crop = frame[y1:y1+self.height_crop, x1:x1+self.width_crop] #(16,16,3)
        
        pad_top = (self.screen_height - crop.shape[0]) // 2
        pad_bottom = (self.screen_height - crop.shape[0] - pad_top)
        pad_left = (self.screen_width - crop.shape[1]) // 2
        pad_right = (self.screen_width - crop.shape[1] - pad_left)
        
        padded = cv2.copyMakeBorder(crop, pad_top, pad_bottom, pad_left, pad_right,
                                    borderType = cv2.BORDER_CONSTANT, value = (0, 0, 0)) #black padding
        
        return padded
        
        
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
            
            if lab.object_name.lower() == "cacodemon":

                print("Looked at a Cacodemon")
                
                cx = lab.x + lab.width / 2
                cy = lab.y + lab.height / 2
                
                dx = abs(cx - screen_cx) / screen_cx
                dy = abs(cy - screen_cy) / screen_cy
                
                distance = np.sqrt(dx * dx + dy * dy)
                alignment = max(0.0, 1.0 - distance)
                
                rewards.append(alignment)
                
        return max(rewards, default = 0.0)
        
    
    def step(self, action):
        
        
        # | Action Index | Action Name     | Action Vector                                   |
        # |--------------|-----------------|-------------------------------------------------|
        # | 0            | ATTACK          | [True, False, False, False, False, False, False] |
        # | 1            | MOVE_LEFT       | [False, True, False, False, False, False, False] |
        # | 2            | MOVE_RIGHT      | [False, False, True, False, False, False, False] |
        # | 3            | MOVE_FORWARD    | [False, False, False, True, False, False, False] |
        # | 4            | MOVE_BACKWARD   | [False, False, False, False, True, False, False] |
        # | 5            | TURN_LEFT       | [False, False, False, False, False, True, False] |
        # | 6            | TURN_RIGHT      | [False, False, False, False, False, False, True] |
        
        actions = {
            
            0: "ATTACK",
            1: "MOVE_LEFT",
            2: "MOVE_RIGHT",
            3: "MOVE_FORWARD",
            4: "MOVE_BACKWARD",
            5: "TURN_LEFT",
            6: "TURN_RIGHT"
        }
        
        #Extra information can be added here. E.g. info for debugging...
        info = {}

        # Convert a discrete action into a ViZDoom format for buttons
        action_vector = [False] * self.action_space.n
        action_vector[action] = True
        
        _ = self.game.make_action(action_vector, 4)

        reward = self.game.get_game_variable(vzd.GameVariable.USER1) / self.reward_scale

        alignment = self._get_cacodemon_alignment_reward() #i.e. did the agent look at the cacodemon?
        reward += 0.05 * alignment
        
        if action in [5, 6]:
            reward += 0.05

        done = self.game.is_episode_finished()
        
        #sleep(0.035)
        
        if self.verbose == "true":
            print(f"\n\n Action reward: {reward}, reward_scale = {self.reward_scale}, action taken: {actions[action]}")      
        
        print(f"\n\n Action reward: {reward}, reward_scale = {self.reward_scale}, action taken: {actions[action]}")      
        
        
        if not done:
            frame = self._get_obs()
            obs = self._get_crop_image(frame)
            
            if self.verbose == "true":
                cv2.imshow("Cropped image", obs)
                cv2.waitKey(1)
            
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
        
        self._seed = seed
        
        super().reset(seed = seed)
        
        if seed is not None:
            
            self.action_space.seed(seed)
            self.observation_space.seed(seed)
            self.game.set_seed(seed)
        
        self.game.new_episode()

        frame = self._get_obs()
        obs = self._get_crop_image(frame)
        
        return obs, {}
        
        
        
        


    