# Logs Folder

Model logs during training for the active vision model follow the naming convention "Cacodemon_Recognition_..." where `...` is a number for the settings tuning and full training iteration. The rest of this file will detail the hyperparameter settings used and any reward value changes. 

This file has been included such that decisions/tunings can be tracked and a record taken so that if rollback to certain settings is required, this is made easy; without having to rely on git rollbacks etc...

Names follow this convention:

Cacodemon_Recognition (scenario) _ N (level number) _ N' (iteration number) _ Image_Reduction_%


###### Notes

- **ACS Scripts**: *Reward is divided by a constant as ACS cannot directly use floating point numbers so the reward is converted in the Python file*

- **Python Files**: *These detail the hyperparameter settings and any other relevant variables*

- **Configuration Files**: *A note of what config file was used (using indicies)*: See the active vision environment file's `scenario_configs` list for more info

---

## Base Structure

**Python File**: active_visual_model_training_lvl__.py

<br>

**Config File:**:

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +15
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_0

**Python File**: active_visual_model_training_lvl_1_.py

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +7.5
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_2_0

**Python File**: active_visual_model_training_lvl_1_.py

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +7.5
- **Other Enemy Kill Reward**: +10

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---


# PADDED ACTIVE VISION


## Cacodemon_Recognition_1_1_80

**Successful?**: No

**Python File**: active_visual_model_training_lvl_1_.py

```python
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.5

            # ...

self.width_crop, self.height_crop,  = 128, 96
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_2_80

**Successful?**: Yes

**Python File**: active_visual_model_training_lvl_1_.py

```python
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

# ...

self.width_crop, self.height_crop,  = 128, 96
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_3_60

**Successful?**: Yes

**Python File**: active_visual_model_training_lvl_1_.py

```python
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 96, 72
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_4_40

**Successful?**: No

**Python File**: active_visual_model_training_lvl_1_.py

```python
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 64, 48
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_5_20

**Successful?**: Yes

**Python File**: active_visual_model_training_lvl_1_.py

```python
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 32, 24
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_6_10

**Successful?**: No

**Python File**: active_visual_model_training_lvl_1_.py

```python
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 16, 12
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_7_5

**Successful?**: No

**Python File**: active_visual_model_training_lvl_1_.py

```python
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 8, 6
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_8_1

**Successful?**: Kind of

**Python File**: active_visual_model_training_lvl_1_.py

```python
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 1,1
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_9_40

**Successful?**: No

**Python File**: active_visual_model_training_lvl_1_.py

```python
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 64, 48
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_10_10

**Successful?**: No

**Python File**: active_visual_model_training_lvl_1_.py

```python
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 16, 12
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_11_5

**Successful?**: No

**Python File**: active_visual_model_training_lvl_1_.py

```python
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 8, 6
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_12_1

**Successful?**: No

**Python File**: active_visual_model_training_lvl_1_.py

```python
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 1, 1
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_13_40

**Successful?**: No

**Python File**: active_visual_model_training_lvl_1_.py

```python
learning_rate = 3e-4
steps = 256
batch_size = 32
epochs = 5
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.01

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 64, 48
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_14_10

**Successful?**: No

**Python File**: active_visual_model_training_lvl_1_.py

```python
learning_rate = 3e-4
steps = 256
batch_size = 32
epochs = 5
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.01

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 16, 12
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_15_5

**Successful?**: No

**Python File**: active_visual_model_training_lvl_1_.py

```python
learning_rate = 3e-4
steps = 256
batch_size = 32
epochs = 5
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.01

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 8, 6
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

<br><br>

# RESCALED ACTIVE VISION

## Cacodemon_Recognition_1_16_80

**Successful?**: Yes, model_1575000.zip 

**Python File**: active_visual_model_training_lvl_1_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 128, 96
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_17_60

**Successful?**: No, retrain required as this is out of the ordinary. Will try to encourage more exploration with a higher entropy coefficient. Model defaults to spinning.

**Python File**: active_visual_model_training_lvl_1_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 96, 72
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_18_40

**Successful?**: Yes, model_3025000.zip 

**Python File**: active_visual_model_training_lvl_1_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 64, 48
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_19_20

**Successful?**: Yes, model_1975000.zip

**Python File**: active_visual_model_training_lvl_1_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 32, 24
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_20_10

**Successful?**: Yes, model_2000000.zip

**Python File**: active_visual_model_training_lvl_1_.py

```python
learning_rate = 3e-4
steps = 1024
batch_size = 128
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.05
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 16, 12
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_21_5

**Successful?**: Yes, model_2100000.zip

**Python File**: active_visual_model_training_lvl_1_.py

```python
learning_rate = 3e-4
steps = 1024
batch_size = 128
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.05
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 8, 6
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_22_1

**Successful?**: Yes, model_2100000.zip

**Python File**: active_visual_model_training_lvl_1_.py

```python
learning_rate = 3e-4
steps = 1024
batch_size = 56
epochs = 5
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.05
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 1, 1
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_1_23_60

**Successful?**: Yes, adjusting the hyperparameters to induce further 3exploration from the model helped encourage it to learn, unlike `Cacodemon_Recognition_17_60`: model_2100000.zip

**Python File**: active_visual_model_training_lvl_1_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.05
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 96, 72
```

<br>

**Config File:**: 0

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_2_1_80

**Successful?**: No, can identify the Cacodemon but won't kill it. Need to adjust the entropy coefficient and see

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 128, 96
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: -100 / 1000 = 0.1

---

## Cacodemon_Recognition_2_2_60

**Successful?**: No, can identify the Cacodemon but won't kill it. Need to adjust the entropy coefficient and see

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 96, 72
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: -100 / 1000 = 0.1

---

## Cacodemon_Recognition_2_3_40

**Successful?**: No, can identify the Cacodemon but won't kill it. Need to adjust the entropy coefficient and see

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 64, 48
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: -100 / 1000 = 0.1

---

## Cacodemon_Recognition_2_4_20

**Successful?**: No, can identify the Cacodemon but won't kill it. Need to adjust the entropy coefficient and see

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 32, 24
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_2_5_10

**Successful?**: 

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 1024
batch_size = 128
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.05
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 16, 12
```

<br>

**Config File:**: 1

<br>

**ACS Script**: No, can identify the Cacodemon but won't kill it. Entropy coefficient was adjusted, will need to now consider reward differences. Perhaps bullet penalty alongside the living and wrong enemy reward is too harsh. Will try reducing the bullet penalty

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_2_6_5

**Successful?**: No, can identify the Cacodemon but won't kill it. Entropy coefficient was adjusted, will need to now consider reward differences. Perhaps bullet penalty alongside the living and wrong enemy reward is too harsh. Will try reducing the bullet penalty

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 1024
batch_size = 128
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.05
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 8, 6
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_2_7_1

**Successful?**: 

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 1024
batch_size = 56
epochs = 5
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.05
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 1, 1
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: None

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_2_8_80

**Successful?**: No, can identify the Cacodemon but won't kill it. Bullet reward was adjusted. Maybe need to consider removing bullet reward

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 128, 96
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: -10 / 1000 = 0.01

---

## Cacodemon_Recognition_2_9_60

**Successful?**: No, can identify the Cacodemon but won't kill it. Bullet reward was adjusted. Maybe need to consider removing bullet reward

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 96, 72
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: -10 / 1000 = 0.01

---

## Cacodemon_Recognition_2_10_40

**Successful?**: No, can identify the Cacodemon but won't kill it. Bullet reward was adjusted. Maybe need to consider removing bullet reward

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 64, 48
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: -10 / 1000 = 0.01

---

## Cacodemon_Recognition_2_11_20

**Successful?**: No, can identify the Cacodemon but won't kill it. Bullet reward was adjusted. Maybe need to consider removing bullet reward

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 32, 24
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: -10 / 1000 = 0.01

---

## Cacodemon_Recognition_2_12_10

**Successful?**: No, can identify the Cacodemon but won't kill it. Bullet reward was adjusted. Maybe need to consider removing bullet reward

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 16, 12
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: -10 / 1000 = 0.01

---

## Cacodemon_Recognition_2_13_5

**Successful?**: No, can identify the Cacodemon but won't kill it. Bullet reward was adjusted. Maybe need to consider removing bullet reward

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 8, 6
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: -10 / 1000 = 0.01

---

## Cacodemon_Recognition_2_14_80

**Successful?**: No, can identify the Cacodemon but won't kill it. Bullet reward was adjusted. Maybe need to consider removing bullet reward

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 128, 96
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: -10 / 1000 = 0.01

---

## Cacodemon_Recognition_2_15_60

**Successful?**: No, can identify the Cacodemon but won't kill it. Bullet reward was adjusted. Maybe need to consider removing bullet reward

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 96, 72
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: -10 / 1000 = 0.01

---

## Cacodemon_Recognition_2_17_80

**Successful?**: Yes, can identify the Cacodemon and sometimes kill it, but sometimes gets stuck. Bullet reward was removed. Not enough

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 128, 96
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: -10 / 1000 = 0.01

---

## Cacodemon_Recognition_2_18_60

**Successful?**: Yes, can identify the Cacodemon and sometimes kill it, but sometimes gets stuck. Bullet reward was removed. Not enough 

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.01
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 96, 72
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -20

- **Living Reward**: -10 / 1000 = 0.01
- **Bullets Shot Reward**: -10 / 1000 = 0.01

---

## Cacodemon_Recognition_2_19_80

**Notes**: Previous attempts have been very unfruitful. Will try the following:

- Increase the entropy coefficient to 0.05
- Remove the bullet negative reward
- Increase the living reward to encourage shooting and not spinning/"turn-maxing"
- Decrease, slightly, the negative reward of killing the wrong enemy from -20 to -15, still enough to deter

**Successful?**: Yes, performs excellently, identifying and moving towards the Cacodemon before killing it: `model_6350000.zip`

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.05
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 128, 96
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -15

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None

---

## Cacodemon_Recognition_2_20_60

**Successful?**: Yes, performs excellently, identifying and moving towards the Cacodemon before killing it: `model_6475000.zip`

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.05
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 96, 72
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -15

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None


---

## Cacodemon_Recognition_2_21_40

**Successful?**: 

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.05
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 64, 48
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -15

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None


---

## Cacodemon_Recognition_2_22_20

**Successful?**: 

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 2048
batch_size = 256
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.05
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 32, 24
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -15

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None


---

## Cacodemon_Recognition_2_23_10

**Notes**: From 10 onwards the hyperparameters have been reduced to deal with a much lesser frame of input in the sense of how much the model actually gets to see. This is conformative with level 1 training, as otherwise steps and updates are too long and as such too unmeaningful to the model, need much lesser steps and batch size.

**Successful?**: 

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 1024
batch_size = 128
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.05
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 6, 12
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -15

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None


---

## Cacodemon_Recognition_2_24_5

**Successful?**: 

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 1024
batch_size = 128
epochs = 10
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.05
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03
training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 8, 6
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -15

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None


---

## Cacodemon_Recognition_2_25_1

**Notes**: Since the model is only seeing a single pixel, steps, batch size, and epochs should be relatively tiny in comparison to the other reductions, not much need for it to take such a large sample before updating weights. This is only for research purposes anyways.
 
**Successful?**: 

**Python File**: active_visual_model_training_lvl_2_.py

```python
learning_rate = 3e-4
steps = 1024
batch_size = 56
epochs = 5
timesteps = 25000 #how often do we want the model to be saved? 
gamma = 0.99
gae_lambda = 0.95 ##
clip_range = 0.2
ent_coef = 0.05
vf_coef = 0.5
max_grad_norm = 0.5
target_kl = 0.03

training_repeats = 1000

lr_schedule = linear_lr_schedule(initial_value = 3e-4, final_value = 1e-5)
```

**Python File**: Active_Visual_Cacodemon_Recognition_env.py

```python
if action in [5, 6]:
            reward += 0.05

    #...

self.width_crop, self.height_crop,  = 1, 1
```

<br>

**Config File:**: 1

<br>

**ACS Script**:

- **Cacodemon Kill Reward**: +10
- **Other Enemy Kill Reward**: -15

- **Living Reward**: -100 / 1000 = 0.1
- **Bullets Shot Reward**: None


---

