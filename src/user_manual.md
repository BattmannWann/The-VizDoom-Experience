# User Guide

#### A guide to the [software_name_here] software, written by Rhys Stewart [date_here]

This is the markdown version for the [GitHub repository](url_here). On this link, a PDF copy can be found if preferred. 

---

## Contents

### 1. Introduction

### 2. Prerequisites

### 3. Running Project Files

---

## Introduction

Welcome to the user guide for `The ViZDoom Experience` project, a 4th year level project undertaken by Rhys Stewart as part of the Computing Science degree at Glasgow University. This file serves as the user guide for using this repository of code, to evaluate the project or expand on its goals. To find out more about this project and better understand its purpose, please consult the [Project Information Page](https://github.com/BattmannWann/The-VizDoom-Experience/wiki/Finalised-Project-Notes-and-Description) and the general information provided throughout the rest of the project GitHub repository. 

Covered in this guide are the following procedures:

#### Prerequisites

- How to build the project 

#### Running Project Files

- How to view and modify the `.wad` and `.acs` files
- How to train baseline and active vision models
- How to evaluate saved model performance

---

## Prerequisites

To build this project, it is assumed that you are using a Linux environment (either native or virtualised), and recommended is the use of a virtual environment to separate the project space from the global space. ViZDoom has been distributed onto other platforms and operating systems (OSs), but, as per the GitHub repository and documentation, testing and optimisation has not been perfected for these versions. Thus, **USE THESE AT YOUR OWN DISCRETION**. Specifically, this project was developed using the Ubuntu OS through the Windows Subsystem for Linux (WSL) but any Linux OS and host method are compatible. 

### Basic Environment Requirements

To obtain a copy of this repository (if you are viewing this online and haven't already), you MUST have `Git` installed on your machine. For an Ubuntu system, the command for this is as follows: 

```bash
$ sudo apt install git
```

For other OSs, see the [Git website](https://git-scm.com/).

<br>

Then, to obtain a local copy of the repository, issue the following command:

```bash
$ git clone https://github.com/BattmannWann/The-VizDoom-Experience.git
```

<br>

Once this has been completed, it is recommended that you create a virtual environment (venv) to gather and store all project dependencies. As this project is Python based, created is a Python venv. This means that your system MUST have a version of python installed. For this project, it is recommended to have AT LEAST Python version $>=$ [`3.12.x`](https://www.python.org/downloads/release/python-3123/), along with the newest version of PIP (this can normally be done when installing Python using the installation wizard by enabling a checkbox). ViZDoom does support newer and older versions, but to ensure that everything works accordingly, this version should be installed. 

Once you have the correct Python version, issue the following commands to create and activate a venv (OUTSIDE OF THE GIT LOCAL REPOSITORY):

```bash
$ python3 -m venv [venv_name_here] #Can just call this venv

$ source venv/bin/activate

```

<br>

Finally, to install project dependencies, change into the project directory and issue the following command:

```bash
$ cd The-VizDoom-Experience

$ pip install -r requirements.txt

```

> Instructions for this step can also be found in the project's `README.md`, but, for the sake of a comprehensive user guide, they will also be included here


---

## Viewing and Editing `.wad` and `.acs` Files

To view and edit these files, a `.wad` file editor IS REQUIRED. The one used in this project was the [Ultimate DoomBuilder Software](https://forum.zdoom.org/viewtopic.php?t=66745). However, other editors which can view `.wad` files are available and can be found on the repository [Wiki for this project](https://github.com/BattmannWann/The-VizDoom-Experience/wiki) and for the [ViZDoom project.](https://github.com/Farama-Foundation/ViZDoom#awesome-doom-toolsprojects)

Once one of these has been downloaded, simply open up the software, press the open file button at the top left, and navigate to the repository directory: `src/scenarios/CacodemonRecognition/wad_files/` and select the `.wad` file you wish to view.

To view the ACS script, press `F10` on your keyboard or navigate to the top topbar and search for the `Scripts` button. This opens up the scripts viewer and displays the ACS script that has been written for the scenario. On a new file, normally this section is blank.

On making a change, ensure to save the script file. First, this will attempt to compile the script and issue either a success or error message, indicating to you the line number and possible issue. On issues, be sure to rectify them and save again to recompile. Once compilation is successful, **BE SURE TO THEN SAVE THE WAD FILE ALSO** to save the script into it.

To test the created map, you MUST have some form of Doom port installed. This project used the GZDoom port, but others are available at the [ZDoom Downloads Page](https://zdoom.org/downloads). Once this has been installed, you must then point your map viewer to the installation directory. The instructions provided in the application should be clear, but there are very good resources online if further guidance is required. 

---

## Training Models

To train models using the provided files and or current directory structure, you must change into the training files directory:

```bash

$ cd src/scenarios/CacodemonRecognition/training_files/

```

Then, you have two options:

1. **Train a baseline model**: The files in the `baseline_model_training/` directory follow this structure: `baseline_training_lvl_N_.py` where `N` is a number. For example, lets say we want to train a level 1 baseline model:

    - Open the codebase in some form of IDE or code editor (e.g. VSCode) 
    - Navigate to the level 1 baseline training file and ensure to edit the three following lines$^{1}$:

       - **Line 15**: Keep `../models_baseline/` and select a name for the model directory that models will be saved to. For example: `../models/baseline/Cacodemon_Recognition_1`. This is responsible for naming the saved models directory

       - **Line 30**: Keep `base = Monitor(base, filename = os.path.join(f"{logs_directory}/env_monitors",` and change the last argument to the name you would like. For example: `env_monitor_Cacodemon_Recognition_1`. This is responsible for naming the env_monitor file (used for additional information gathering, may not be needed).

       - **Line 221**: Keep `model.learn(total_timesteps = timesteps, reset_num_timesteps = False, tb_log_name = f"` and change the name of the file in the f-string. For example: `Cacodemon_Recognition_1`. This is responsible for naming the log directory of the model as it trains. These logs can then be inspected using tensorboard (see []()). 

    - Then, run the following command to being training:

```bash

$ python -m baseline_model_training.baseline_training_lvl_1 

```

2. **Train an active vision model**: Do the same as part 1 but with under the `active_vision_model_training/` directory:

```bash

$ python -m active_vision_model_training.active_visual_model_training_lvl_1 

```

<br>

For different levels, the same rules apply, but the line numbers may be different. The code to modify will be around the same place. 

---
>
> ###### $^{1}$: These line numbers may change, but the rough location should remain the same. If this changes, these will be updated accordingly
>
---

## Model Evaluation

In the repository, there is a folder which contains a python script to load and run a chosen model. This can be found under: `src/scenarios/CacodemonRecognition/training_files/model_evaluation/run_model.py`.

To run a model, there are several available commands to use and depend entirely on what you desire. To see the list of commands, issue the following:

```bash
$ python -m model_evaluation.run_model --help

```

To run a model, you MUST have a saved model. As part of the project, you can find some under: `data/trained_models/`. You can either point the flag to there or copy a model to a closer directory to run from there. 

An example will be illustrated below:

```bash
$  python -m model_evaluation.run_model --in-model-path ../models_baseline/Level 1/model_2450000.zip --sleep 0.035 --config-path 0 --episodes 10
```

What this does:

- Loads model `model_2450000.zip`
- Loads `Cacodemon_Recognition_most_basic.cfg` which points to the wad file and sets up basic variables
- Sets the delay such that watching the model perform is reasonable (as otherwise it is too fast to understand)
- Sets the episodes to 10

<br><br>

Assuming you have downloaded the following [folders](), here are some evaluation commands for each type and each level within each type of model, for convenience:

## Active Models


### **Level 1**:

- **100%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_26_100/model_4700000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 0 --reduction 0 --episodes 10`

- **80%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_16_80/model_1575000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 0 --reduction 80 --episodes 10`


- **60%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_23_60/model_1950000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 0 --reduction 60 --episodes 10`


- **40%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_18_40/model_3025000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 0 --reduction 40 --episodes 10`

- **20%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_19_20/model_1975000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 0 --reduction 20 --episodes 10`

- **10%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_20_10/model_2000000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 0 --reduction 10 --episodes 10`

- **5%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_21_5/model_2100000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 0 --reduction 5 --episodes 10`

- **1%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_22_1/model_2100000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 0 --reduction 1 --episodes 10`

---

### **Level 2**:

- **100%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_26_100/model_4700000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 1 --reduction 0 --episodes 10`

- **80%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_19_80/model_6350000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 1 --reduction 80 --episodes 10`

- **60%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_20_60/model_6475000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 1 --reduction 60 --episodes 10`

- **40%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_21_40/model_3200000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 1 --reduction 40 --episodes 10`

- **20%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_22_20/model_6850000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 1 --reduction 20 --episodes 10`

- **10%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_23_10/model_7100000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 1 --reduction 10 --episodes 10`

- **5%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_24_5/model_7125000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 1 --reduction 5 --episodes 10`

- **1%**: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_27_1/model_4775000.zip --sleep 0.035 --active "true" --verbose "true" --config-path 1 --reduction 1 --episodes 10`

---

<br>

## Baseline Models

- **Level 1**: `python -m model_evaluation.run_model --in-model-path ../models_baseline/Level 1/model_2450000.zip --sleep 0.035 --verbose "true" --config-path 0 --episodes 10`

- **Level 2**: `python -m model_evaluation.run_model --in-model-path ../models_baseline/Level 2/model_3720000.zip --sleep 0.035 --verbose "true" --config-path 0 --episodes 10`


---