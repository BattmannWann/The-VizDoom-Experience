from vizdoom import *
import random
import time

TARGET = "Cacodemon"
REWARD_TARGET_KILL = 20
PENALTY_WRONG_KILL = -10
LIVING_REWARD = -0.01

game = DoomGame()
game.load_config("Cacodemon_Recognition.cfg")
game.init()

available_buttons = game.get_available_buttons()
if not available_buttons:
    raise RuntimeError("No available buttons found. Check your .cfg file!")

action = [False] * len(available_buttons)
action[random.randint(0, len(available_buttons)-1)] = True

print("Available buttons:", game.get_available_buttons())
print("Available actions:", len(game.get_available_buttons()))


def get_alive_enemies(state):
    """Return dict of alive enemies (id -> type)."""
    enemies = {}
    if state.labels_buffer is not None:
        for obj in state.labels:
            if obj.object_name not in ["DoomPlayer", "Clip", "Medikit"]:
                enemies[obj.object_id] = obj.object_name
    return enemies

episodes = 5

for ep in range(episodes):
    print(f"\n=== Episode {ep+1} ===")
    game.new_episode()
    prev_enemies = {}

    while not game.is_episode_finished():
        state = game.get_state()
        current_enemies = get_alive_enemies(state)

        # Find which enemies disappeared (killed)
        killed = [eid for eid in prev_enemies if eid not in current_enemies]

        reward = LIVING_REWARD
        for eid in killed:
            killed_type = prev_enemies[eid]
            if killed_type == TARGET:
                reward += REWARD_TARGET_KILL
                print(f"✅ Killed target: {killed_type} (+{REWARD_TARGET_KILL})")
            else:
                reward += PENALTY_WRONG_KILL
                print(f"❌ Killed wrong type: {killed_type} ({PENALTY_WRONG_KILL})")

        # Example random action (replace with your RL agent)
        action = [False] * len(game.get_available_buttons())
        action[random.randint(0, len(action)-1)] = True

        reward += game.make_action(action)

        prev_enemies = current_enemies.copy()

    print("Episode total reward:", game.get_total_reward())

game.close()
