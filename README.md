[![ViZDoom CI](https://github.com/BattmannWann/The-VizDoom-Experience/actions/workflows/ci.yml/badge.svg)](https://github.com/BattmannWann/The-VizDoom-Experience/actions/workflows/ci.yml)

# The ViZDoom Experience
#### An Individual Project Completed by Rhys Stewart

---

## Introduction

Welcome to The ViZDoom Experience. This repository serves the basis for research and investigation for the fourth year individual project at the University of Glasgow Computing Science Degree. This project is worth 40 credits. For more information, visit the [course catalogue](https://www.gla.ac.uk/coursecatalogue/course/?code=COMPSCI4025P). 

---

*Side Note:*
>The end goal of this project will deliver a fully reproducible, tangible integration of ViZDoom, Gymnasium, and Stable-Baselines3, as current literature and documentation do not provide examples of these technologies implemented together. 
>
>The scenario developed here aims to evaluate the effects of active vision on model performance, but the underlying framework provides a strong, concrete implementation that can be easily utilised and modified for other scenarios. 

---

Before diving into the content, hypothesis, or the report (dissertation), it is important to understand what is being researched here. This will be discussed in the section below, but first some pre-requisites. 

### What is ViZDoom?

>A "Doom-based AI research platform for reinforcement learning from raw visual information" developed on top of [ZDOOM](https://zdoom.org/) an "enhanced port of the Doom engine for running on modern operating systems" - *[ViZDoom](https://ViZDoom.cs.put.edu.pl/)*

This will be the basis of the 3D engine used in this project. 


### What is Gymnasium?

>Gymnasium provides a standardised, interoperable API for reinforcement learning environments. It ensures that the underlying RL algorithms can interact with the custom DOOM scenarios in a reproducible manner through defining strict observation and action spaces.


### What is Stable-Baselines3?

>SB3 is an open-source library build on top of the RL framework PyTorch, that provides highly reliable, benchmarked implementations of modern Deep Reinforcement Learning (DRL) algorithms. 

---

## Purpose and Aims

The purpose of this project is to answer the following research question: "*Does the addition of an active visual sensor in a reinforcement learning agent trained in a 3D environment result in a significant improvement in task performance?*"

The aims can then be derived as follows:

- **Environment Development**: Design and develop custom, scalable 3D training scenarios utilising the ViZDoom research platform and the standardised Gymnasium API

- **Agent Training**: Implement and train a baseline (passive) model and an active vision model. 

- **Comparative Evaluation**: Evaluate and compare the efficacy of the active visual sensor against the baseline model across varied levels of environmental complexity, visual occlusion, and restricted fields of view.

- **Generalisation Analysis**: Assess the generalisability of the learned active vision policies in unseen, dynamic environments, addressing a core challenge in current DRL literature. 


### How Will this be Achieved?

The project is going to be developed in the following ways:

- Models will be trained using the `Stable-Baselines3 PPO` architecture. 

- To train models, [custom gymnasium environments](https://github.com/BattmannWann/The-VizDoom-Experience/tree/main/src/scenarios/CacodemonRecognition/training_files/envs) will be created for the custom task scenarios; one for the baseline and another for the active vision model.

- Training scripts will be developed to create the custom Gym environments and train PPO models independently (i.e. one model per level, trained from scratch)

- Custom DOOM Maps/configurations will be developed to present an environment to a model. This requires the creation of `.cfg` and `.wad` files. More information can be found in their respective directories (e.g. [`config_files/`](https://github.com/BattmannWann/The-VizDoom-Experience/tree/main/src/scenarios/CacodemonRecognition/config_files) and [`wad_files`](https://github.com/BattmannWann/The-VizDoom-Experience/tree/main/src/scenarios/CacodemonRecognition/wad_files) and on the [GitHub Wiki](https://github.com/BattmannWann/The-VizDoom-Experience/wiki)). 

- Model evaluation script(s) required to test the saved trained models during the training phase (models are saved at a 25,000 steps interval)

---

## File Structure and What to Expect

This project has the following directory structures:

```
The-ViZDoom-Experience/
├── data/
│   ├── Graphs
│   │   ├── Evaluations/                    # Graphs created on analysis of the evaluation logs
│   │   └── Training_Graphs/                # Graphs on model training (steps with cumulative reward)
│   │ 
│   ├── README.md                           # Description of data sources
│   ├── model_performance_data/             # Logs from model evaluation
│   ├── notebooks/                          # Jupyter Notebooks and Python Scripts used to visualise data from evaluations
│   │
│   ├── visualisations/                     # Figures providing additional visualisations 
│   │   ├── map_overviews/                  # In-game, 2D, and 3D overviews of each map in the Cacodemon Recognition scenario
│   │   ├── model_evals/                    # Frame-by-frame visualisations of model performances 
│   │   ├── original_pre-reduction_images/  # Images before they were reduced and rescaled 
│   │   └── reduction_rescaled_images/      # Images that have been reduced and rescaled to demonstrate the active vision FOVs 
│   │ 
│   └── trained_models/                     # Saved trained models (does not come by standard with a `git clone`)
│
├── meetings/
│   └── README.md                           # Weekly supervisor meeting minutes
│
├── presentation/
│   ├── slides/                             # PowerPoint and PDF presentations
│   ├── figures/                            # Images and diagrams
│   └── references.md                       # Slide bibliography
│
├── src/
│   ├── mods/                               # ViZDoom / Doom modifications
│   │   └── Pain_Elemental_Mod.pk3          # Mod that changes the death behaviour of the Pain Elemental enemy
│   │
│   ├── scenarios/
│   │   └── CacodemonRecognition/
│   │       ├── All_Logs/                                           # Logs generated during model training for all model types
│   │       │   ├── Active_Vision/
│   │       │   ├── Baseline/
│   │       │   └── logs_active_different_seeds/
│   │       │
│   │       ├── config_files/                                       # Scenario configuration files that handle WAD, pk3, and game variables
│   │       │   ├── Cacodemon_Recognition_most_basic.cfg
│   │       │   ├── Cacodemon_Recognition_basic.cfg
│   │       │   ├── Cacodemon_Recognition_Final.cfg
│   │       │   └── README.md
│   │       │
│   │       │
│   │       ├── training_files/                                     # Files used for model training
│   │       │   ├── active_vision_model_training/                   # Scripts for training the active vision models
│   │       │   │   ├── active_visual_model_training_lvl_1.py
│   │       │   │   └── active_visual_model_training_lvl_2.py
│   │       │   │
│   │       │   ├── baseline_model_training/                        # Scripts for training the baseline models
│   │       │   │   ├── baseline_training_lvl_1.py
│   │       │   │   └── baseline_training_lvl_2.py
│   │       │   │
│   │       │   ├── envs/                                           # Gymnasium environments for Active & Baseline
│   │       │   │   ├── Active_Visual_Cacodemon_Recognition_env.py
│   │       │   │   └── Baseline_Cacodemon_Recognition_env.py
│   │       │   │
│   │       │   ├── example_files/                                  # Primitive ViZDoom usage, using handcrafted rules (NO TRAINING)
│   │       |   │   ├── simple_random_action_model.py
│   │       |   │   └── simple_random_action_model_manual_rewards.py
|   |       |   |
│   │       |   └── model_evaluation/                               # Scripts used to evaluate trained models
│   │       │       ├── run_model.py                                # Loads PPO and environments and then runs a saved model
│   │       │       ├── evaluate_models.sh                          # Uses the run_model.py script to evaluate EVERY model
│   │       │       └── record_performance.sh                       # Records the evaluations of all models, up to 10 episodes
│   │       │
│   │       ├── wad_files/                                          # WAD Files for the different levels of the scenario
│   │       │   ├── ACS_Scripts/
│   │       │   │   ├── Cacodemon_Recognition_most_basic.acs
│   │       │   │   ├── Cacodemon_Recognition_basic.acs
│   │       │   │   └── Cacodemon_Recognition_Final.acs
│   │       │   │
│   │       │   ├── Cacodemon_Recognition_most_basic.wad
│   │       │   ├── Cacodemon_Recognition_basic.wad
│   │       │   └── Cacodemon_Recognition_Final.wad
│   │       │
│   │       ├── README.md
│   │       └── user_manual.md
│   │ 
│   ├── tests/                                  # Test directory for testing project aspects
│   │   ├── bash_scripts/                       # Scripts to be executed in the command line
│   │   │   ├── Cacodemon_Recognition_tests.sh  # Tests that the training of models can be carried out successfully on the system
│   │   │   └── Project_integrity_tests.sh      # Ensures that the project has been cloned/pulled correctly
│   │   │
│   │   └── Python_scripts/                     # Specific tests for Python files
│   │       ├── test_envs.py                    # Tests that the Gymnasium environments have been setup correctly
│   │       ├── test_model_training.py          # Tests for model training. More intricate than the broad bash script
│   │       └── test_run_model.py               # Ensures that the model evaluation python script works as intended, testing all features
│   │
│   └── README.md                               # Source-level overview
│
├── .coveragerc                                 # Exceptions for the PyTest coverage module (print statements and if main statements)
├── .gitignore                                  # Files that the VC system should ignore
├── plan.md                                     # Project plan / milestones
├── pytest.ini                                  # Sets up the PyTest module, pointing to directories and runtime instructions
├── README.md                                   # Project overview
├── requirements.txt                            # Dependencies list (pip)
├── setup_project.sh                            # Helper script; downloads trained models, creates virtual environments, and runs project tests
└── timelog.md                                     

```

This provides absolutely every directory within the project. For more information, most directories contain a further `README.md` to explain in-depth what can be found within. 

---

## Build Instructions

To build this project, creation of a virtual environment (venv) is strongly recommended and will be shown in the following `Build Steps` section. All dependencies are managed and handled by the `pip` installer and can be found in `requirements.txt`.

---

### Requirements

This project has been developed using a Linux environment. Versions of ViZDoom have been made available for MACOS and Windows but, there are no guarantees that this project will transfer over smoothly. Therefore, the recommendation is to use a Linux operating system or through WSL [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install). For more information about operating systems and ViZDoom, please consult the [GitHub repository.](https://github.com/Farama-Foundation/ViZDoom#python-quick-start)

Additionally, models have been trained using a GPU however, these [notes](https://github.com/BattmannWann/The-VizDoom-Experience/wiki/Saving-Models-in-PyTorch#using-a-gpu) provide a detailed explanation of how to transfer models saved and trained on a GPU to the CPU and vice versa if required. 

Specific requirements for packages and versions used can be found [here](requirements.txt). However, the following provides a quick summary:

- pip==25.2
- python==3.10.12
- stable_baselines3==2.7.1
- vizdoom==1.2.4
- tensorboard==2.20.0

Most of the other requirements are installed by these dependencies.

---

### Build Steps

The following assumes a **UNIX SYSTEM** (e.g. a Linux distribution or WSL). It can be done on **other systems** but a warning is issued as this has **NOT** been tested:

```bash

#Create a venv: Recommendation is to create this OUTSIDE of the git repository directory (i.e. one parent directory level up)
$ python3 -m venv [enter_venv_name_here]

#Activate the venv
$ source venv_name_here/bin/activate

#Clone the repository
$ git clone https://github.com/BattmannWann/The-VizDoom-Experience.git

#move into the git directory
$ cd The-VizDoom-Experience/

#Install the dependencies
$ pip install -r requirements.txt

```

And that is all that is needed to build and activate the project dependencies. 

See the following if more information is needed:

- [Installing WSL](https://learn.microsoft.com/en-us/windows/wsl/install#:~:text=Install%20WSL%20command,-You%20can%20now&text=Open%20PowerShell%20in%20administrator%20mode,command%2C%20then%20restart%20your%20machine.&text=This%20command%20will%20enable%20the,the%20Ubuntu%20distribution%20of%20Linux.)

- [Installing ViZDoom](https://github.com/Farama-Foundation/ViZDoom#python-quick-start)


<br>

#### Alternative Method

The `setup_project.sh` script, found in project root, has a function that will handle the creation of a virtual environment for you, installing dependencies and activating it.

---

### Test Steps

In this project are two types of tests:

1. Bash Script Testing: Ensures that the project has been setup properly and can run on the host system
2. Python Script Testing: Specific tests for the Python files used in this project

Assumptions:

- You are in the project root to start with
- Your virtual environment has been activated and dependencies installed correctly
- You have permission to change file permissions (if not, replace `./` with `source`)


Instructions to run these tests are as follows:

---

#### Bash Tests

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

#### Python Tests

```bash
#change into the Python_scripts/ directory
$ cd src/tests/Python_scripts/

#run the tests using the pytest module
$ python -m pytest

```

On running these tests, a coverage report will also be created and displayed on the terminal. It will also create an html page under `htmlcov/`.

---

All of these tests can also be run by the `setup_project.sh` script, on following the instructions presented on screen when running.

---

## Usage

Please consult the [`User Manual`](https://github.com/BattmannWann/The-VizDoom-Experience/blob/main/src/user_manual.md) for step-by-step instructions on how to use the files provided in this repository.

---

## Support

Please feel free to contact me regarding any queries, issues, or concerns using the [issues page](https://github.com/BattmannWann/The-VizDoom-Experience/issues) or through email: 2682261s@gmail.com

I am more than happy to discuss the project at any stage and provide demonstrations.

---

## Project Status

- Initiation stage has begun [week of 22/09/2025]
- Learning of technologies has finished [week of 03/11/2025]
- Gymnasium Environments Developed [week of 05/01/2026]
- Baseline model training completed [week of 19/01/2026]
- Active Vision model training completed [week of 13/02/2026]
- Trained all baseline models on all levels with different seeds [week of 26/02/2026]
- Trained all active vision models on all levels and conditions with different seeds [week of 09/03/2026]
- Finalised end project tests [week of 11/03/2026]
- Completed evaluations over all models, levels, and conditions [week of 16/03/2026]
- Dissertation has been written and source code in published state [week of 26/03/2026]

> **PROJECT HAS NOW FINISHED**

---

## Hardware Specifications

ViZDoom is a particularly versatile software that can run on a variety of hardware. The following lists the hardware used by my machine but, this does not mean that these are the only hardware that can run the project:

- **CPU**: AMD Ryzen 5 5600X (12 Core)
- **GPU**: NVIDIA GeForce RTX 3060
- **Installed RAM**: 16.0 GB
- **OS**: Windows 11 Home / WSL Ubuntu
