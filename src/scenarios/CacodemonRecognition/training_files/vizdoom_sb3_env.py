import gymnasium as gym
from gymnasium import spaces
import numpy as np
import vizdoom as vzd

import os

class VizDoomBasicEnv(gym.Env):
    metadata = {"render_modes": []}

    def __init__(self):
        super().__init__()

        self.game = vzd.DoomGame()
        self.game.set_doom_scenario_path(os.path.join(vzd.scenarios_path, "basic.wad"))
        self.game.set_doom_map("map01")

        self.game.set_screen_resolution(vzd.ScreenResolution.RES_160X120)
        self.game.set_screen_format(vzd.ScreenFormat.RGB24)

        self.game.set_depth_buffer_enabled(False)
        self.game.set_labels_buffer_enabled(False)
        self.game.set_automap_buffer_enabled(False)

        self.game.set_render_hud(False)
        self.game.set_render_weapon(True)
        self.game.set_render_decals(False)

        self.game.set_available_buttons(
            [vzd.Button.MOVE_LEFT, vzd.Button.MOVE_RIGHT, vzd.Button.ATTACK]
        )
        self.actions = [
            [True, False, False],
            [False, True, False],
            [False, False, True],
        ]

        self.game.set_available_game_variables([vzd.GameVariable.AMMO2])

        self.game.set_episode_timeout(200)
        self.game.set_episode_start_time(10)
        self.game.set_living_reward(-1)
        self.game.set_window_visible(False)

        self.game.set_mode(vzd.Mode.PLAYER)
        self.game.init()

        # Gym action space: Discrete(3)
        self.action_space = spaces.Discrete(len(self.actions))

        # Observation: image + gamevars
        self.observation_space = spaces.Dict({
            "image": spaces.Box(
                low=0, high=255, shape=(120, 160, 3), dtype=np.uint8
            ),
            "vars": spaces.Box(
                low=-np.inf, high=np.inf, shape=(1,), dtype=np.float32
            )
        })

    def _get_obs(self):
        state = self.game.get_state()
        screen = state.screen_buffer  # (H, W, C)
        #screen = np.transpose(screen, (2, 0, 1))  # (C, H, W)

        vars = np.array(state.game_variables, dtype=np.float32)

        return {
            "image": screen.astype(np.uint8),
            "vars": vars
        }

    def _get_info(self):
        return {}

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        self.game.new_episode()
        obs = self._get_obs()
        return obs, {}

    def step(self, action):
        reward = self.game.make_action(self.actions[action])
        terminated = self.game.is_episode_finished()

        if terminated:
            obs = self.observation_space.sample()   # dummy
        else:
            obs = self._get_obs()

        return obs, reward, terminated, False, self._get_info()

    def close(self):
        self.game.close()
