import torch
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, VecTransposeImage
from stable_baselines3.common.monitor import Monitor

import wandb
from wandb.integration.sb3 import WandbCallback

from vizdoom_sb3_env import VizDoomBasicEnv


wandb.init(
    project = "vizdoom-ppo",
    config = {
        "total_timesteps": 500_000,
        "learning_rate": 0.0001,
        "env_name": "VizdoomCacodemonRecognition-v0"
    }
)


def make_env():
    return Monitor(VizDoomBasicEnv())


def main():

    env = DummyVecEnv([make_env])

    # Transpose to CHW (SB3 CNN expects this)
    env = VecTransposeImage(env)

    model = PPO(
        policy="MultiInputPolicy",
        env=env,
        n_steps=2048,
        batch_size=64,
        learning_rate=3e-4,
        gamma=0.99,
        gae_lambda=0.95,
        clip_range=0.2,
        ent_coef=0.01,
        verbose=2,
        tensorboard_log=None,
    )

    print("Using device:", model.device)

    model.learn(total_timesteps=500_000,
                callback=WandbCallback(
                    gradient_save_freq=1000,
                    model_save_path="models/",
                    verbose = 2
                ))
    model.save("ppo_vizdoom_basic")

    env.close()


if __name__ == "__main__":
    main()
