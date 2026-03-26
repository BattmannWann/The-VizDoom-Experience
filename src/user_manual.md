# User Guide

#### A guide to The ViZDoom Experience, written by Rhys Stewart 26/03/2026

##### This is the User Guide for the source code, which can be found in the [GitHub repository](https://github.com/BattmannWann/The-VizDoom-Experience/tree/main).
---

## Contents

### 1. Introduction

### 2. Prerequisites
    2.1 Basic Environment Requirements
        2.1.1 Alternative Installation Method

### 3. Viewing and Editing `.wad` and `.acs` Files

### 4. Training Models

### 5. Training Evaluation

### 6. Model Evaluation
    6.1 Baseline Evaluation 
    6.2 Active Vision Evaluation

### 7. Testing
    7.1 Bash Scripts
    7.2 Python Scripts

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


#### Alternative Installation Method

Alternatively, once you have cloned or pulled the repository, the `setup_project.sh` script can be used to create a virtual environment in the correct place, automatically install the dependencies, and active the virtual environment for you. 

To use this script, simply supply the following command into your terminal:

`$ source setup_project.sh`


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

       - **Line ~74**: Keep `../models_baseline/` and select a name for the model directory that models will be saved to. For example: `../models/baseline/Cacodemon_Recognition_1`. This is responsible for naming the saved models directory. Do the same for the logs directory.

       - **Line ~28**: Keep `base = Monitor(base, filename = os.path.join(f"{logs_directory}/env_monitors",` and change the last argument to the name you would like. For example: `env_monitor_Cacodemon_Recognition_1`. This is responsible for naming the env_monitor file (used for additional information gathering, may not be needed).

       - **Line ~171**: Change the name of the file in the f-string. For example: `Cacodemon_Recognition_1`. This is responsible for naming the log directory of the model as it trains. These logs can then be inspected using tensorboard (see the Training Evaluation section below). 

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
In a future, ideal version, these would be handled by `argparse`, passed into the Python file as arguments.

---
>
> ###### $^{1}$: These line numbers may change, but the rough location should remain the same. If this changes, these will be updated accordingly
>
---

## Training Evaluation

Installed in the dependencies is `Tensorboard`, an excellent tool used to monitor the progress of model training, looking at the cumulative reward, number of steps, entropy, and numerous other metrics. 

To use tensorboard, issue the following commands into your terminal:

```bash
#change into the directory that contains the logs directory; for example, the project comes with logs already
$ cd src/scenarios/CacodemonRecognition/

#Note that you will not be able to run the whole All_Logs directory, as there are too many files
$ tensorboard --logdir All_Logs/Baseline/

```

---

## Model Evaluation

In the repository, there is a folder which contains a python script to load and run a chosen model. This can be found under: `src/scenarios/CacodemonRecognition/training_files/model_evaluation/run_model.py`.

To run a model, there are several available commands to use and depend entirely on what you desire. To see the list of commands, issue the following:

```bash
#change into the training_files/ directory of the Cacodemon Recognition scenario
$ cd src/scenarios/CacodemonRecognition/training_files/

#run the model_evaluation script run_model.py
$ python -m model_evaluation.run_model --help

```

To run a model, you MUST have a saved model. As part of the project, you can find some under: `data/trained_models/`. You can either point the flag to there or copy a model to a closer directory to run from there. 

An example will be illustrated below:

```bash

#without the line breaks. For convenience, during development, you can copy/move the models into the training_files/ directory

$  python -m model_evaluation.run_model --in-model-path 
    /home/username/projects/The-VizDoom-Experience/data/trained_models/
    Cacodemon_Recognition_baseline_models/Level 1/model_2450000.zip 
    --sleep 0.035 --config-path 0 --episodes 10
```

What this does:

- Loads model `model_2450000.zip`
- Loads `Cacodemon_Recognition_most_basic.cfg` which points to the wad file and sets up basic variables
- Sets the delay such that watching the model perform is reasonable (as otherwise it is too fast to understand)
- Sets the episodes to 10

<br><br>

Assuming you have downloaded the following [folders](https://gla-my.sharepoint.com/:u:/g/personal/2682261s_student_gla_ac_uk/IQBTzkvv-PcJSJIbJOtvm-m2AcHyHoK17hxcoV74BWWKldQ?e=C1feka), here are some evaluation commands for each type and each level within each type of model, for convenience:

> in your terminal, you can create variables to avoid typing out the full model directories
> using `$ export BASELINE_DIR="/home/username/projects/The-VizDoom-Experience/data/trained_models/Cacodemon_Recognition_baseline_models"`

### Baseline Evaluation

**LEVEL 1**
`python -m model_evaluation.run_model --in-model-path "${BASELINE_DIR}/Level 1/model_2450000.zip" --config-path 0 --episodes 100 --output baseline_lvl_1_model`

**LEVEL 2**
`python -m model_evaluation.run_model --in-model-path "${BASELINE_DIR}/Level 2/model_3720000.zip" --config-path 1 --episodes 100 --output baseline_lvl_2_model`

---

### Active Vision Evaluation

**LEVEL 1**

- $100$%:
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/100_model_1275000.zip" --active "true" --config-path 0 --reduction 0 --episodes 100 --output active_lvl_1_100_model`

- $80$%: 
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/80_model_1575000.zip" --active "true" --config-path 0 --reduction 80 --episodes 100 --output active_lvl_1_80_model`

- $60$%: 
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/60_model_1950000.zip" --active "true" --config-path 0 --reduction 60 --episodes 100 --output active_lvl_1_60_model`

- $40$%: 
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/40_model_3025000.zip" --active "true" --config-path 0 --reduction 40 --episodes 100 --output active_lvl_1_40_model`

- $20$%:
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/20_model_1975000.zip" --active "true" --config-path 0 --reduction 20 --episodes 100 --output active_lvl_1_20_model`

- $10$%:
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/10_model_2000000.zip" --active "true" --config-path 0 --reduction 10 --episodes 100 --output active_lvl_1_10_model`

- $5$%:
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/5_model_2100000.zip" --active "true" --config-path 0 --reduction 5 --episodes 100 --output active_lvl_1_5_model`

- $1$%:
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/1_model_2100000.zip" --active "true" --config-path 0 --reduction 1 --episodes 100 --output active_lvl_1_1_model`

---

**LEVEL 2**:

- $100$%:
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/100_model_4700000.zip" --active "true" --config-path 1 --reduction 0 --episodes 100 --output active_lvl_2_100_model.txt`

- $80$%:
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/80_model_6350000.zip" --active "true" --config-path 1 --reduction 80 --episodes 100 --output active_lvl_2_80_model`

- $60$%:
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/60_model_6475000.zip" --active "true" --config-path 1 --reduction 60 --episodes 100 --output active_lvl_2_60_model`

- $40$%:
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/40_model_3000000.zip" --active "true" --config-path 1 --reduction 40 --episodes 100 --output active_lvl_2_40_model`

- $20$%:
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/20_model_6850000.zip" --active "true" --config-path 1 --reduction 20 --episodes 100 --output active_lvl_2_20_model`

- $10$%:
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/10_model_2650000.zip" --active "true" --config-path 1 --reduction 10 --episodes 100 --output active_lvl_2_10_model`

- $5$%:
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/5_model_2800000.zip" --active "true" --config-path 1 --reduction 5 --episodes 100 --output active_lvl_2_5_model`

- $1$%:
`python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/1_model_4775000.zip" --active "true" --config-path 1 --reduction 1 --episodes 100 --output active_lvl_2_1_model`

---

## Testing

To test the various aspects of this project, two test suites have been created:

1. `bash_scripts`: A directory containing bash scripts used for testing running commands and project integrity
    - `Cacodemon_Recognition_tests.sh`: Actually runs the training and evaluation Python scripts, rather than mock tests
    - `Project_integrity_tests.sh`: Ensures that the project has been successfully cloned/pulled

2. `Python_scripts`: Used to test the various Python files used throughout this project. Explicitly, these are 
    - `test_envs`: Tests for the Gymnasium environments
    - `test_model_training.py`: Granular tests for the model training files, testing all the methods and overall functionality
    - `test_run_model`: Tests the argument passing and general functionalities of the run_model file


There are two methods to run these tests:

1. Automatically using the `setup_project.sh` script, which runs all project tests
2. Manually running each test 

As instructions are provided by the `setup_project.sh` script, the following will detail running tests manually:


### Bash Tests

```bash

#change into the bash_scripts/ directory
$ cd src/tests/bash_scripts/  

#provide the scripts with execution privileges
$ chmod +x Cacodemon_Recognition_tests.sh Project_integrity_tests.sh

#run the Cacodemon Recognition tests
$ ./Cacodemon_Recognition_tests.sh

#run the project integrity tests
$ ./Project_integrity_tests.sh

```

---

### Python Tests

```bash
#change into the Python_scripts/ directory
$ cd src/tests/Python_scripts/

#run the tests using the pytest module
$ python -m pytest

```

On running these tests, a coverage report will also be created and displayed on the terminal. It will also create an html page under `htmlcov/`.

---

