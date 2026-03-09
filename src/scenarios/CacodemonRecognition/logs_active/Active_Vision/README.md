# Logs Folder

Model logs during training for the active vision model follow the naming convention "Cacodemon_Recognition_..." where `...` is a number for the settings tuning and full training iteration. The rest of this file will detail the hyperparameter settings used and any reward value changes. 

This file has been included such that decisions/tunings can be tracked and a record taken so that if rollback to certain settings is required, this is made easy; without having to rely on git rollbacks etc...

Names follow this convention:

Cacodemon_Recognition (scenario) _ N (level number) _ N' (iteration number) _ Image_Reduction_%


###### Notes

- **ACS Scripts**: *Reward is divided by a constant as ACS cannot directly use floating point numbers so the reward is converted in the Python file*

- **Python Files**: *These detail the hyperparameter settings and any other relevant variables*

- **Configuration Files**: *A note of what config file was used (using indices)*: See the active vision environment file's `scenario_configs` list for more info

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

## Cacodemon_Recognition_1_24_100

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

self.width_crop, self.height_crop,  = 160, 120
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

---

# Level 2

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

**Successful?**: Yes, model_3000000.zip

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

**Successful?**: Yes, model_6850000.zip

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

**Successful?**: Yes, model_2650000.zip

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

**Successful?**: Yes, model_2800000.zip

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

---

# TESTING WITH DIFFERENT SEEDS

# LEVEL 1

The best trained models from level 1 active vision will be selected and retrained with different seeds to prove that they can indeed learn. All reductions will be checked.

Naming conventions will take the trained models and append a seed at the end of it. 

File configs will be listed in the first; assume that if it is not mentioned that this means that they have not changed.

---
## 100%

## Cacodemon_Recognition_1_24_100_6003

**Successful?**: Yes

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


## Cacodemon_Recognition_1_24_100_3713

**Successful?**: Yes


---


## Cacodemon_Recognition_1_24_100_9955

**Successful?**: Yes


---

---

## 80%

## Cacodemon_Recognition_1_16_80_580

**Successful?**: Yes, model_725000.zip

---

## Cacodemon_Recognition_1_16_80_333

**Successful?**: Yes, model_800000.zip

---

## Cacodemon_Recognition_1_16_80_666

**Successful?**: Yes, model_300000.zip

---

---

## 60%

## Cacodemon_Recognition_1_23_60_4687

**Successful?**: Yes

---

## Cacodemon_Recognition_1_23_60_9218

**Successful?**: Yes

---

## Cacodemon_Recognition_1_23_60_3419

**Successful?**: Yes

---

---

---
## 40%

## Cacodemon_Recognition_1_18_40_2530

**Successful?**: Yes

---

## Cacodemon_Recognition_1_18_40_2111

**Successful?**: Yes

---

## Cacodemon_Recognition_1_18_40_1220

**Successful?**: Yes


---

---

## 20%

## Cacodemon_Recognition_1_19_20_277

**Successful?**: Yes

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

## Cacodemon_Recognition_1_19_20_20899

**Successful?**: Yes

---

## Cacodemon_Recognition_1_19_20_2443

**Successful?**: Yes

---

---
## 10%

## Cacodemon_Recognition_1_20_10_7742

**Successful?**: Yes

---

## Cacodemon_Recognition_1_20_10_527

**Successful?**: Yes

---

## Cacodemon_Recognition_1_20_10_560

**Successful?**: Yes

---

---
## 5%

## Cacodemon_Recognition_1_21_5_5109

**Successful?**: Yes

---

## Cacodemon_Recognition_1_21_5_9717

**Successful?**: Yes

---

## Cacodemon_Recognition_1_21_5_4593

**Successful?**: Yes


---

---

## 1% 

## Cacodemon_Recognition_1_22_1_30

**Successful?**: Yes

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

## Cacodemon_Recognition_1_22_1_40

**Successful?**: Yes

---


## Cacodemon_Recognition_1_22_1

**Successful?**: Yes

---

---

# LEVEL 2

The best trained models from level 1 active vision will be selected and retrained with different seeds to prove that they can indeed learn. All levels of reduction were analysed. Assume that configs do not differ from the first listed unless stated otherwise. 

---
## 100%

## Cacodemon_Recognition_2_26_100_786

**Successful?**: Yes

---

## Cacodemon_Recognition_2_26_100_3809

**Successful?**: Yes

---

## Cacodemon_Recognition_2_26_100_2877

**Successful?**: Yes


---
## 80%

## Cacodemon_Recognition_2_19_80_8927

**Successful?**: Yes

---

## Cacodemon_Recognition_2_19_80_8727

**Successful?**: Yes

---

## Cacodemon_Recognition_2_19_80_7320

**Successful?**: Yes

---

---
## 60%

## Cacodemon_Recognition_2_20_60_5456

**Successful?**: Yes

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

## Cacodemon_Recognition_2_20_60_555555

**Successful?**: Yes

---

## Cacodemon_Recognition_2_20_60_776633

**Successful?**: Yes

---

---

## 40%

## Cacodemon_Recognition_2_21_40_4194

**Successful?**: Yes

---

## Cacodemon_Recognition_2_21_40_1356

**Successful?**: Yes

---

## Cacodemon_Recognition_2_21_40_6325

**Successful?**: Yes

---

---

---
## 20%


## Cacodemon_Recognition_2_22_20_8801

**Successful?**: Yes

---

## Cacodemon_Recognition_2_22_20_432

**Successful?**: Yes

---

## Cacodemon_Recognition_2_22_20_4223

**Successful?**: Yes

---

---

## 10%

## Cacodemon_Recognition_2_23_10_20000

**Successful?**: Yes

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

## Cacodemon_Recognition_2_23_10_4356

**Successful?**: Yes

---

## Cacodemon_Recognition_2_23_10_433356

**Successful?**: Yes

---

---
## 5%

## Cacodemon_Recognition_2_24_5_8840

**Successful?**: Yes

---

## Cacodemon_Recognition_2_24_5_1967

**Successful?**: Yes

---

## Cacodemon_Recognition_2_24_5_2209

**Successful?**: Yes

---

---
## 1%

## Cacodemon_Recognition_2_27_1_2564

**Successful?**:

---

## Cacodemon_Recognition_2_27_1_2141

**Successful?**:

---

## Cacodemon_Recognition_2_27_1_1856

**Successful?**:

---

---

