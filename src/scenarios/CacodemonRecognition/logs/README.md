# Logs Folder Baseline

Model logs during training for the baseline follow the naming convention "Cacodemon_Recognition_..." where `...` is a number for the settings tuning and full training iteration. The rest of this file will detail the hyperparameter settings used and any reward value changes. 

This file has been included such that decisions/tunings can be tracked and a record taken so that if rollback to certain settings is required, this is made easy; without having to rely on git rollbacks etc...


###### Notes

- **ACS Scripts**: *Reward is divided by a constant as ACS cannot directly use floating point numbers so the reward is converted in the Python file*

- **Python Files**: *These detail the hyperparameter settings and any other relevant variables*

- **Configuration Files**: *A note of what config file was used (using indicies)*: See the baseline environment file's `scenario_configs` list for more info

- **Maths for Working out Reward Structures**:

    - Timeout = `episode_timout` * `living_penalty` (e.g. 1200 * -0.01 = -12)

    - Shooting = `%chance of hitting an enemy` * `reward` (e.g. 1 (+10) cacodemon and 3 (-3 per enemy) non-cacodemon = 25:75 split, = (0.25 * 10) + (0.75 * -3) = 2.5 + -2.25  = +0.25)

    - Alignment = `alignment_reward` - `living_reward` (e.g. 0.05 - 0.01 = +0.04 per step)

---

## Base Structure

**Python File**:

<br>

**Config File:**:

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +15
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

### Cacodemon_Recognition_5_0 & Cacodemon_Recognition_6_0

**Python File**:

```python
learning_rate = 3e-4  #3e-4 #Adam optimiser default # 0.0001
steps = 2048
batch_size = 256 #32
epochs = 10
timesteps = 100000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)

env = make_env()
env.seed(123)

#...

model = PPO(
    
    policy = "CnnPolicy",
    env = env,
    learning_rate = lr_schedule,
    n_steps = steps,
    batch_size = batch_size,
    gamma = gamma,
    gae_lambda = gae_lambda,
    clip_range = clip_range,
    ent_coef = ent_coef,
    vf_coef = vf_coef,
    max_grad_norm = max_grad_norm,
    target_kl = target_kl,
    verbose = 1,
    tensorboard_log = logs_directory,
    seed = 123,
)
```

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +15
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

<br>

**Config File**: 0


---

### Cacodemon_Recognition_7_0

**Python File**:

Same as Cacodemon_Recognition_5_0

<br>

**ACS Script**:

> **Why the change?** <br>
> On training models under Cacodemon_Recognition_5_0 & Cacodemon_Recognition_6_0, the agent didn't want to kill both Cacodemons which was a bit strange. I am hazarding a guess that maybe PPO clipped the reward for being too high. It finally settled around `12.44` so maybe setting the reward to half of 15 would help. 

- **Cacodemon Kill Reward**: +7.5
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None


<br>

**Config File**: 0

---

## Cacodemon_Recognition_20_0

**Python File**: baseline_training_lvl_2.py

```python
steps = 2048
batch_size = 256 #32
epochs = 10
timesteps = 100000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.015
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 1e-4, final_value = 5e-5, warmup_ratio = 0.02)
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +15
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: 10 / 1000 = 0.01

---
<br>
---

## Cacodemon_Recognition_21_0

**Python File**: baseline_training_lvl_2.py

```python
steps = 4096
batch_size = 512 #32
epochs = 6
timesteps = 100000 #how often do we want the model to be saved? 
gamma = 0.995
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.003
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 7.5e-5, final_value = 3e-5, warmup_ratio = 0.1)
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +15
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: 100 / 1000 = 0.1

---

<br>

## Cacodemon_Recognition_22_0

Notes: Model was still only killing one Cacodemon. Modified the following to try and convince it to kill the other:

- Added a longer timeout for episode length
- Added an extra bonus for killing the second Cacodemon

**Python File**: baseline_training_lvl_2.py

```python
steps = 4096
batch_size = 512 #32
epochs = 6
timesteps = 100000 #how often do we want the model to be saved? 
gamma = 0.995
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.003
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 7.5e-5, final_value = 3e-5, warmup_ratio = 0.1)
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Episode Timeout**: 2100

- **Cacodemon Kill Reward**: +15 for 1, +25 for 2
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: 100 / 1000 = 0.1

---

## Cacodemon_Recognition_23_0

Notes: Model was still only killing one Cacodemon. Modified the following to try and convince it to kill the other:

- Removed episode timeout to force it to end the episode another way
- Kept extra bonus for killing the second Cacodemon

**Python File**: baseline_training_lvl_2.py

```python
steps = 4096
batch_size = 512 #32
epochs = 6
timesteps = 100000 #how often do we want the model to be saved? 
gamma = 0.995
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.003
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 7.5e-5, final_value = 3e-5, warmup_ratio = 0.1)
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Episode Timeout**: None

- **Cacodemon Kill Reward**: +15 for 1, +25 for 2
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: 100 / 1000 = 0.1

---

## Cacodemon_Recognition_24_0

Notes: Model was still only killing one Cacodemon. Modified the following to try and convince it to kill the other:

- Kept extra bonus for killing the second Cacodemon

**Python File**: baseline_training_lvl_2.py

```python
steps = 4096
batch_size = 512 #32
epochs = 6
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.995
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.003
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 7.5e-5, final_value = 3e-5, warmup_ratio = 0.1)
```

**Python File**: ../envs/Baseline_Cacodemon_recognition_env.py

```python

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
            
            if lab.object_name.lower() in ["cacodemon"]: #, "cyberdemon", "lostsoul", "painelemental", "zombieman"]: #CHANGE MADE HERE
                
                cx = lab.x + lab.width / 2
                cy = lab.y + lab.height / 2
                
                dx = abs(cx - screen_cx) / screen_cx
                dy = abs(cy - screen_cy) / screen_cy
                
                distance = np.sqrt(dx * dx + dy * dy)
                alignment = max(0.0, 1.0 - distance)
                
                rewards.append(alignment)
                
        return max(rewards, default = 0.0)

```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Episode Timeout**: 10,000

- **Cacodemon Kill Reward**: +15 for 1, +25 for 2
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: 100 / 1000 = 0.1

---

## Cacodemon_Recognition_25_0

Notes: Model was still only killing one Cacodemon. Modified the following to try and convince it to kill the other:

- Kept extra bonus for killing the second Cacodemon

**Python File**: baseline_training_lvl_2.py

```python
steps = 4096
batch_size = 512 #32
epochs = 6
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.995
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.003
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 7.5e-5, final_value = 3e-5, warmup_ratio = 0.1)
```

**Python File**: ../envs/Baseline_Cacodemon_recognition_env.py

```python

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
            
            if lab.object_name.lower() in ["cacodemon"]: #, "cyberdemon", "lostsoul", "painelemental", "zombieman"]: #CHANGE MADE HERE
                
                cx = lab.x + lab.width / 2
                cy = lab.y + lab.height / 2
                
                dx = abs(cx - screen_cx) / screen_cx
                dy = abs(cy - screen_cy) / screen_cy
                
                distance = np.sqrt(dx * dx + dy * dy)
                alignment = max(0.0, 1.0 - distance)
                
                rewards.append(alignment)
                
        return max(rewards, default = 0.0)

```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Episode Timeout**: 2100

- **Cacodemon Kill Reward**: +15 for 1, +25 for 2
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: 100 / 1000 = 0.1

---

## Cacodemon_Recognition_26_0

Notes: Model was still only killing one Cacodemon. Modified the following to try and convince it to kill the other:

- Removed episode timeout to force it to end the episode another way
- Kept extra bonus for killing the second Cacodemon

**Python File**: baseline_training_lvl_2.py

```python
steps = 4096
batch_size = 512 #32
epochs = 6
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.995
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.003
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 7.5e-5, final_value = 3e-5, warmup_ratio = 0.1)
```

**Python File**: ../envs/Baseline_Cacodemon_recognition_env.py

```python

def _get_cacodemon_alignment_reward(self):
        
    same as Cacodemon_Recognition_24_0

```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Episode Timeout**: 2100

- **Cacodemon Kill Reward**: +5 for 1, +15 for 2
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: 100 / 1000 = 0.1

---

## Cacodemon_Recognition_27_0

Notes: Model was still only killing one Cacodemon. Modified the following to try and convince it to kill the other:

- Removed episode timeout to force it to end the episode another way
- Kept extra bonus for killing the second Cacodemon

**Python File**: baseline_training_lvl_2.py

```python

learning_rate = 3e-4  #3e-4 #Adam optimiser default # 0.0001
steps = 2048
batch_size = 32 #512
epochs = 15
timesteps = 25000 #100000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.92 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 7.5e-5, final_value = 3e-5, warmup_ratio = 0.1) # NOT USING
```

**Python File**: ../envs/Baseline_Cacodemon_recognition_env.py

```python

def _get_cacodemon_alignment_reward(self):
        
    same as Cacodemon_Recognition_24_0

```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Episode Timeout**: 2100

- **Cacodemon Kill Reward**: +5 for 1, +15 for 2
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: 100 / 1000 = 0.1

---

## Cacodemon_Recognition_28_0

Notes: Model was still only killing one Cacodemon. Modified the following to try and convince it to kill the other:

- Removed episode timeout to force it to end the episode another way
- Kept extra bonus for killing the second Cacodemon

**Python File**: baseline_training_lvl_2.py

```python

learning_rate = 3e-4  #3e-4 #Adam optimiser default # 0.0001
steps = 2048
batch_size = 32 #512
epochs = 15
timesteps = 25000 #100000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 1 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 7.5e-5, final_value = 3e-5, warmup_ratio = 0.1) #NOT USING
```

**Python File**: ../envs/Baseline_Cacodemon_recognition_env.py

```python

def _get_cacodemon_alignment_reward(self):
        
    same as Cacodemon_Recognition_24_0

```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Episode Timeout**: 2100

- **Cacodemon Kill Reward**: +5 for 1, +15 for 2
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: 100 / 1000 = 0.1

---

## Cacodemon_Recognition_29_0

Notes: Model was still only killing one Cacodemon. Modified the following to try and convince it to kill the other:

- Removed episode timeout to force it to end the episode another way
- Kept extra bonus for killing the second Cacodemon

**Python File**: baseline_training_lvl_2.py

```python

learning_rate = 3e-4  #3e-4 #Adam optimiser default # 0.0001
steps = 2048
batch_size = 32 #512
epochs = 15
timesteps = 25000 #100000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.92 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000


lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5, warmup_ratio = 0.1)
```

**Python File**: ../envs/Baseline_Cacodemon_recognition_env.py

```python

def _get_cacodemon_alignment_reward(self):
        
    same as Cacodemon_Recognition_24_0

```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Episode Timeout**: 2100

- **Cacodemon Kill Reward**: +5 for 1, +15 for 2
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: 100 / 1000 = 0.1

---


## Cacodemon_Recognition_30_0

Notes: Model was still only killing one Cacodemon. Modified the following to try and convince it to kill the other:

- Removed episode timeout to force it to end the episode another way
- Kept extra bonus for killing the second Cacodemon

**Python File**: baseline_training_lvl_2.py

```python

learning_rate = 3e-4  #3e-4 #Adam optimiser default # 0.0001
steps = 2048
batch_size = 32 #512
epochs = 15
timesteps = 25000 #100000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000


lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5, warmup_ratio = 0.1)
```

**Python File**: ../envs/Baseline_Cacodemon_recognition_env.py

```python

def _get_cacodemon_alignment_reward(self):
        
    same as Cacodemon_Recognition_24_0

```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Episode Timeout**: 2100

- **Cacodemon Kill Reward**: +5 for 1, +15 for 2
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: 100 / 1000 = 0.1

---

# PROJECT SCOPE AMENDMENT

As the models weren't able to learn to shoot both Cacodemons, the scenario has, from this point on, been adjusted to have the models learn just to kill ONE cacodemon. The naming convention will just stay the same, and the logs/models kept nonetheless. The names will just have an extra number (e.g. Cacodemon_Recognition_1_1 and so on...). However, this time, it will follow this order:

Cacodemon_Recognition (scenario) _ N (level number) _ N' (iteration number)

---

## Cacodemon_Recognition_1_1

**Successfully Trained?**: Yes, but not as refined as `1_3`.  Model pre-e,mptively shoots before actually getting the cacodemon in its sight.

**Python File**: baseline_training_lvl_1.py

learning_rate = 3e-4  #3e-4 #Adam optimiser default # 0.0001
steps = 2048
batch_size = 256 #32
epochs = 10
timesteps = 100000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)

env = make_env()
env.seed(123)

#...

model = PPO(
    
    policy = "CnnPolicy",
    env = env,
    learning_rate = lr_schedule,
    n_steps = steps,
    batch_size = batch_size,
    gamma = gamma,
    gae_lambda = gae_lambda,
    clip_range = clip_range,
    ent_coef = ent_coef,
    vf_coef = vf_coef,
    max_grad_norm = max_grad_norm,
    target_kl = target_kl,
    verbose = 1,
    tensorboard_log = logs_directory,
    seed = 123,
)

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

- **Episode Length**: 1000

---

## Cacodemon_Recognition_1_2

**Successfully Trained?**: Yes, but not as refined as `1_3`. The model pre-emptively shoots before the cacodemon is directly in its view.

Everything the same as `Cacodemon_Recognition_1_1` apart from the Baseline Gym Environment (`Baseline_Cacodemon_recognition_env.py`): Taken away the alignment bonus as there is only one cacodemon to worry about now. Sparse rewards effected the previous models since the task was to kill both. Now that only one needs to be killed, sparsity shouldn't be of issue. I will also try adding a bullets negative reward this early on as well to understand if that behaviour can now be learned in stage 1.

---

## Cacodemon_Recognition_1_3

Everything the same as `Cacodemon_Recognition_1_2` apart from the addition of a bullets shot negative reward.

**Successfully Trained?**: Yes. This model will be used for level 2 training, specifically `model_2450000.zip`. Scarce bullet use was not yet learned to its full, but this can be rectified in later training stages. 

---

## Cacodemon_Recognition_2_1

**Successfully Trained?**: No

**Python File**: baseline_training_lvl_2.py

learning_rate = 3e-4  #3e-4 #Adam optimiser default # 0.0001
steps = 2048
batch_size = 256 #32
epochs = 10
timesteps = 100000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)

env = make_env()
env.seed(123)

#...

model = PPO(
    
    policy = "CnnPolicy",
    env = env,
    learning_rate = lr_schedule,
    n_steps = steps,
    batch_size = batch_size,
    gamma = gamma,
    gae_lambda = gae_lambda,
    clip_range = clip_range,
    ent_coef = ent_coef,
    vf_coef = vf_coef,
    max_grad_norm = max_grad_norm,
    target_kl = target_kl,
    verbose = 1,
    tensorboard_log = logs_directory,
    seed = 123,
)

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -100 / 1000 = -0.1
- **Bullets Shot Reward**: -100/ 1000 = -0.1

- **Episode Length**: 1000

<br>

**Notes**: For the first iteration, I will load in the best model of `..._1_3` and keep all the other settings the same, except for the bullet penalty which I have increased to -0.1. Will investigate the effects and see if hyperparameters (more specifically the learning rate and entropy coefficient) need adjusted.

LEARNING COLLAPSED ALMOST IMMEDIATELY

---

## Cacodemon_Recognition_2_2

**Successfully Trained?**: No

Everything is the same as `..._2_1` except the learning rate has been significantly lowered to prevent policy collapse. Will try the following:

```python
lr_schedule = linear_lr_schedule(initial_value = 7.5e-5, final_value = 3e-5, warmup_ratio = 0.1)

```

May need to adjust the warmup ratio to 0.2.

---

## Cacodemon_Recognition_2_3

**Successfully Trained?**: No

The only things changed here are some hyperparameters to have the model add to its existing policies in smaller increments and in a way that corresponds with its previous learning rate which ended at 1e-5. 

**Python File**:

```python

steps = 1024
batch_size = 32  #256 #512
epochs = 10  #15
timesteps = 25000 #100000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

#lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5, warmup_ratio = 0.1)
lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5, warmup_ratio = 0.2)

```

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = -0.01
- **Bullets Shot Reward**: -100  /  1000 = -0.1

- **Episode Length**: 1200

---

## Cacodemon_Recognition_2_4

**Successfully Trained?**: Yes. This will be used for training of level 3, specifically `model_3720000.zip`

**Python File**: baseline_training_lvl_2.py

learning_rate = 3e-4  #3e-4 #Adam optimiser default # 0.0001
steps = 2048
batch_size = 32
epochs = 15
timesteps = 10000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.92 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5, warmup_ratio = 0.1)

env = make_env()
env.seed(123)


<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = -0.01
- **Bullets Shot Reward**: -100/ 1000 = -0.1

- **Episode Length**: 1000

---

## Cacodemon_Recognition_2_5

**Successfully Trained?**: Yes, but surprisingly not as good as 2_4, possibly due to the smaller batch size and prominent shorter term rewards over the long term that 2_4 has. 

**Python File**: baseline_training_lvl_2.py

steps = 2048
batch_size = 64 # or move to 128
epochs = 10
timesteps = 10000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.1
ent_coef = 0.005
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 5e-5, final_value = 1e-6, warmup_ratio = 0.05)

env = make_env()
env.seed(123)


<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = -0.01
- **Bullets Shot Reward**: -100/ 1000 = -0.1

- **Episode Length**: 1200

---

## Cacodemon_Recognition_2_6

**Successfully Trained?**: No, agent converges to doing nothing and opting for a small living rewards. 

Same as `..._2_5` except for:

**ACS Script**:

- **Cacodemon Kill Reward**: +15
- **Other Enemy Kill Reward**: -3

- **Living Reward**: -10 / 1000 = -0.01
- **Bullets Shot Reward**: -100/ 1000 = -0.1

- **Episode Length**: 1200

<br>

**Python File Gym Env**:

- **Alignment Reward**: 0.01 * Alignment

---

## Cacodemon_Recognition_2_7

As curriculum learning was a bad idea, this model will serve as the fresh training for level 2 for comparison with level 1 training. Will keep the trained model regardless, but will just make a clear disticntion.

**Successfully Trained?**: 

**Python File**: baseline_training_lvl_1.py

learning_rate = 3e-4  #3e-4 #Adam optimiser default # 0.0001
steps = 2048
batch_size = 256 #32
epochs = 10
timesteps = 100000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)

env = make_env()
env.seed(123)

#...

model = PPO(
    
    policy = "CnnPolicy",
    env = env,
    learning_rate = lr_schedule,
    n_steps = steps,
    batch_size = batch_size,
    gamma = gamma,
    gae_lambda = gae_lambda,
    clip_range = clip_range,
    ent_coef = ent_coef,
    vf_coef = vf_coef,
    max_grad_norm = max_grad_norm,
    target_kl = target_kl,
    verbose = 1,
    tensorboard_log = logs_directory,
    seed = 123,
)

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = -0.01
- **Bullets Shot Reward**: -100/ 1000 = -0.1

- **Episode Length**: 1000

---