# ViZDoom Visual Learning Environment
#### An Individual Project Completed by Rhys Stewart

---

## Introduction

Welcome to the ViZDoom Experience. This repository serves the basis for research, data analysis, and a formal scientific report. 

Before diving into the content or the report, it is important to understand what is being researched here. This will be discussed in the section below, but first some pre-requisite. 

### What is ViZDoom?

>A "Doom-based AI reseach platform for reinforcement learning from raw visual information". This project has been developed based off of [ZDOOM](https://zdoom.org/) an "enhanced port of the Doom engine for running on modern operating systems". 

*For more information, click here: [ViZDoom](https://ViZDoom.cs.put.edu.pl/)*

This will be the basis of the project, used to answer the proposed research question. 

---

## Purpose and Aims

The purpose of this project is to answer the following research question: "What is the effect of having an active sensor in training a reinforcement learning (RL) agent in ViZDoom?"

The aims can then be derived as follows:

- Create specific test scenarios within the DOOM environment to test and train AI models on specific abilities. Examples include recognition, and hierarchy understanding. These should be appropriate `.wad` and `.cfg` files as per DOOM convention for map creation. See here for [futher examples.](https://github.com/BattmannWann/The-VizDoom-Experience/wiki/Initial-Project-Notes#project-description-broken-down)

- Create a baseline model for each scenario. This model should be implemented in PyTorch, using appropriate and conventional CNN architecture, optimisers, and loss functions. These models should take in frames from ViZDoom to learn and extrapolate features through unsupervised reinforcement learning. Rewards should be clearly stated in each scenario example

- Create new models from adding an active sensor to the baseline models (while ensuring to keep these separate) and train on the scenarios

- Use statistical tests and plot figures to determine if the addition of a visual sensor adds significant improvement to model performance

---

## File Structure and What to Expect

---

## Build Instructions

---

### Requirements

This project has been developed using a Linux environment. Versions of ViZDoom have been made available for MACOS and Windows but, there are no guarantees that this project will transfer over smoothly. Therefore, the recommendation is to use a Linux operating system or through WSL [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install). For more information about operating systems and ViZDoom, please consult the [GitHub repository.](https://github.com/Farama-Foundation/ViZDoom#python-quick-start)

Additionally, models have been trained using a GPU however, these [notes](https://github.com/BattmannWann/The-VizDoom-Experience/wiki/Saving-Models-in-PyTorch#using-a-gpu) provide a detailed explanation of how to transfer models saved and trained on a GPU to the CPU and vice versa if required. 

Specific requirements for packages and versions used can be found [here](requirements.txt) (not implemented yet...). However, the following provides a quick summary:

- Python: version ...
- PyTorch: version ...
- ViZDoom: version ...



---

### Build Steps

---

### Test Steps

---

## Support

Please feel free to contact me regarding any queries, issues, or concerns using the [issues page](https://github.com/BattmannWann/The-VizDoom-Experience/issues) or through email: 2682261s@gmail.com

I am more than happy to discuss the project at any stage and provide demonstrations of the finished product.

---

## Project Status

- Initiation stage has begun [week of 22/09/2025]
- Learning of technologies has finished [week of 03/11/2025]

---

## Hardware Specifications

ViZDoom is a particularly verstile software that can run on a variety of hardware. The following lists the hardware used by my machine but, this does not mean that these are the only hardware that can run the project:

- ...
- 
