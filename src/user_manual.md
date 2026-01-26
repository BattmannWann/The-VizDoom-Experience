# User Guide

#### A guide to the [software_name_here] software, written by Rhys Stewart [date_here]

This is the markdown version for the [GitHub repository](url_here). On this link, a PDF copy can be found if preferred. 

---

## Contents

### 1. Introduction

### 2. Prerequisites

### 3. ...

---

## Training Models

To train models using the provided files and or current directory structure, you must change into the training files directory:

```bash

$ cd src/scenarios/CacodemonRecognition/training_files/

```

Then, you have two options:

1. **Train a baseline model**: The files in the `baseline_model_training/` directory follow this structure: `baseline_training_lvl_N_.py` where `N` is a number. For example, lets say we want to train a level 1 baseline model:

    - Open the codebase in some form of IDE or code editor (e.g. VSCode) 
    - Navigate to the level 1 baseline training file and ensure to edit the three following lines:

       - **Line 15**: Keep `../models_baseline/` and select a name for the model directory that models will be saved to. For example: `../models/baseline/Cacodemon_Recognition_1`. This is responsible for naming the saved models directory

       - **Line 30**: Keep `base = Monitor(base, filename = os.path.join(f"{logs_directory}/env_monitors",` and change the last argument to the name you would like. For example: `env_monitor_Cacodemon_Recognition_1`. This is responsible for naming the env_monitor file (used for additional information gathering, may not be needed).

       - **Line 221**: Keep `model.learn(total_timesteps = timesteps, reset_num_timesteps = False, tb_log_name = f"` and change the name of the file in the f-string. For example: `Cacodemon_Recognition_1`. This is responsible for naming the log directory of the model as it trains. These logs can then be inspected using tensorboard (see []()). 

    - Then, run the following command to being training:

```bash

$ python -m baseline_model_training.baseline_training_lvl_1 

```

2. **Train an active vision model**: Do the same as part 1 but with under the `active_vision_model_training/` directory.

<br>

For different levels, the same rules apply, but the line numbers may be different. The code to modify will be around the same place. 
