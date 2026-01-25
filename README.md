# ViZDoom Visual Learning Environment
#### An Individual Project Completed by Rhys Stewart

---

## Introduction

Welcome to the ViZDoom Experience. This repository serves the basis for research and investigation for the fourth year individual project at the University of Glasgow Computing Science Degree. This project is worth 40 credits. For more information, visit the [course catalogue](https://www.gla.ac.uk/coursecatalogue/course/?code=COMPSCI4025P). 

Before diving into the content, hypotheses, or the report, it is important to understand what is being researched here. This will be discussed in the section below, but first some pre-requisite. 

### What is ViZDoom?

>A "Doom-based AI research platform for reinforcement learning from raw visual information" based off of [ZDOOM](https://zdoom.org/) an "enhanced port of the Doom engine for running on modern operating systems" - *[ViZDoom](https://ViZDoom.cs.put.edu.pl/)*

This will be the basis of the project, used to answer the proposed research question. 

---

## Purpose and Aims

The purpose of this project is to answer the following research question: "What effect does adding an active visual sensor have on model performance, where that model is trained using reinforcement learning using the ViZDoom software?"

The aims can then be derived as follows:

- **Create two model types**: Baseline and Active Vision

- **Train model types independently**: Thus, the baseline model and the active vision model will be trained on the proposed scenario(s) separately, where saved models are not used between these two types. 

- **Use statistical tests and plot figures to determine if the addition of a visual sensor adds significant improvement to model performance**


### How Will this be Achieved?

The project is going to be developed in the following ways:

- Models will be trained using the `Stable Baselines 3` reinforcement learning (RL) framework, which acts as a wrapper around the Gymnasium framework, to provide easy access to common RL models and streamline the training process. 

- To train models, custom gymnasium environments need to be created for the custom task scenarios; one for the baseline and another for the active vision model.

- Training scripts will be developed to create the custom Gym environments and train PPO models in a curriculum learning approach (see the README.md files under the scenario directory)

- Custom DOOM Maps/configurations need to be developed to present an environment to a model. This requires the creation of `.cfg` and `.wad` files. More information can be found in their respective directories (e.g. `config_files/` and `wad_files` and on the GitHub Wiki). 

- Model evaluation script(s) required to test the saved trained models during the training phase (models are saved at a 25,000 steps interval)

---

## File Structure and What to Expect

This project has the following directory structures:

```
The-ViZDoom-Experience/
├── data/
│   ├── README.md                       # Description of data sources
│   ├── model_performance_data/         # Evaluation metrics, logs, plots
│   └── trained_models/                 # Saved trained models
│
├── meetings/
│   └── README.md                       # Weekly supervisor meeting minutes
│
├── presentation/
│   ├── slides/                         # PowerPoint and PDF presentations
│   ├── figures/                        # Images and diagrams
│   └── references.md
│
├── src/
│   ├── mods/                           # ViZDoom / Doom modifications
│   │
│   ├── scenarios/
│   │   └── CacodemonRecognition/
│   │       ├── config_files/
│   │       │   ├── Cacodemon_Recognition_most_basic.cfg
│   │       │   ├── Cacodemon_Recognition_basic.cfg
│   │       │   ├── Cacodemon_Recognition_Final.cfg
│   │       │   └── README.md
│   │       │
│   │       ├── model_evaluation/
│   │       │   └── run_model.py
│   │       │
│   │       ├── training_files/
│   │       │   ├── active_vision_model_training/
│   │       │   │   ├── active_visual_model_training_lvl_1.py
│   │       │   │   ├── active_visual_model_training_lvl_2.py
│   │       │   │   └── active_visual_model_training_lvl_3.py
│   │       │   │
│   │       │   ├── baseline_model_training/
│   │       │   │   ├── baseline_training_lvl_1.py
│   │       │   │   ├── baseline_training_lvl_2.py
│   │       │   │   └── baseline_training_lvl_3.py
│   │       │   │
│   │       │   ├── envs/
│   │       │   │   ├── Active_Visual_Cacodemon_Recognition_env.py
│   │       │   │   └── Baseline_Cacodemon_Recognition_env.py
│   │       │   │
│   │       │   └── example_files/
│   │       │       ├── simple_random_action_model.py
│   │       │       └── simple_random_action_model_manual_rewards.py
│   │       │
│   │       ├── wad_files/
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
│   └── README.md                       # Source-level overview
│
├── .gitignore
├── plan.md                             # Project plan / milestones
├── timelog.md                          # Time tracking
├── requirements.txt
└── README.md                           # Project overview

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

The following assumes a **UNIX SYSTEM** (e.g. a Linux distribution or WSL). It can be done on other systems but a warning is issued as this has **NOT** been tested:

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

---

### Test Steps

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

---

## Hardware Specifications

ViZDoom is a particularly versatile software that can run on a variety of hardware. The following lists the hardware used by my machine but, this does not mean that these are the only hardware that can run the project:

- **CPU**: AMD Ryzen 5 5600X (12 Core)
- **GPU**: NVIDIA GeForce RTX 3060
- **Installed RAM**: 16.0 GB
- **OS**: Windows 11 Home / WSL Ubuntu
