# Week 5, Project Week 5

## October 20th, 2025

**Present**:

- Rhys Stewart 
- Dr. Gerardo Aragon Camarasa (Supervisor)

---

### Foreword

Previous meeting minutes were not taken due to redundancy. Project had a slow start-up due to initial supervisor issues which were resolved in `Project Week 5 (20/10/2025)`. Further meetings consisted of advice on where to begin research and learning. Subsequent weeks followed a 'check-in' of the learning process and a general suggestion to speed up the development process to ensure it was on track. i was advised that the meeting minutes aren't strictly pertinent however, as a standard for project development I will attempt to construct meeting notes if time allows from the notes I had taken. I will include a brief overall summary in this set of notes in the case that this is not possible and keep note of this for future projects to ensure that these and the timelogs are completed in appropriate time and consistently. I will ensure to include dates where is possible and is appropriate. 

---

### Achieved in Previous Weeks:

- **ACS Scripting (Week of 15/01/2025)**: Devised the basic reward structure for the scenario:

    - **Positive Rewards**: `+100 for killing a Cacodemon`
    - **Negative Rewards**: `-1 Living reward` (i.e every second the game goes on) - Puts a time constraint on the model to try and get it to act quickly - `-1 for shooting a bullet` - puts a constraint on resources

    Constructed basic operations to spawn enemies randomly. 


- **ACS Scripting (Week of 22/10/2025)**: Research into why random enemy spawning didn't perform well; the game engine is very sensitive towards thing 'hit-boxes' such that it will refuse to place things too close to each other. ***Solution***: Use the thing type `MapSpot` which serves as a coordinate location that can be used as reference for where to spawn enemies. To randomly spawn enemies, sample a random number between defined tags set for each MapSpot (i.e. each MapSpot receives a tag from 100-n_number_of_spots) and attempt to spawn the enemy there. If there is a conflict, keep trying until the enemy is successfully spawned -- turned out to be very effective.


- **ACS Scripting (Week of 27/10/2025)**: Rewards (both positive and negative) weren't being allocated properly. Research was conducted to understand how rewards are allocated and passed from the ViZDoom engine to Python; there is a default reward variable that the engine uses but that can't be easily accessed, instead, can pass through custom variables to communicate rewards to the Python file(s). These custom variables have a special place defined in the system, where variable 0 is reserved for the reward. Thus, must use user rewards from 1 onwards (see [Scopes](https://zdoom.org/w/index.php?title=Scope) for further details) when using the global space. These can then be passed using the configuration files when declaring what variables are available, these follow the order of `USER_number_here` (e.g. reward is passed using `USER1`). Documentation was particularly difficult to navigate through and an answer was hard to find. 


- **Basic Example Files**: These were used to test and pull information before integration and development of the `Stable Baselines 3 (SB3)` Python files. These can be found under `src/scenarios/CacodemonRecognition/training_files/example_files`. There are two versions but the main purpose is to demonstrate a model that takes random actions. One file manually (hardcoded) provides rewards and the other pulls the rewards from ACS correctly. Once these were finalised and an understanding of the core principles behind the ViZDoom engine and ACS scripting achieved, development could progress into SB3. 


- **SB3 Learning and Project Creation**: Before using SB3, the documentation was studied and the tutorial was completed before moving on to creating the customised version(s) for the project. Custom scenario development was slightly non-trivial and required tutorials and understanding of the Gymnasium library before development could take place. For simple projects, SB3 can be used as-is 'out-of-the-box' as it provides a plethora of resources to do so. However, since this project required very specific and custom configurations, a custom Gymnasium environment had to be created for SB3 to use properly. To start with, the baseline environment was created and placed in `src/scenarios/CacodemonRecognition/` however, this proved to be problematic as the training files directory was unable to retrieve the created code. Thus, this was then later placed into `.../training_files/envs`, to ensure proper compatibility between resources. 


- **Initial Model Training**: The baseline models were first trained on the `...most_basic.wad` file which was still in early development. Very quickly, it was evident that the hyperparameters and reward models were unsuitable to train a PPO model for this task. Many iterations ensued, along with research regarding what hyperparameters were suitable for a PPO model. The best source was taken from [AurelianTactics](https://medium.com/aureliantactics/ppo-hyperparameters-and-ranges-6fc2d29bccbe) but further sources used can be found in the [GitHub Wiki](https://github.com/BattmannWann/The-VizDoom-Experience/wiki) (under the PPO sidebar section). However, different tunings were still insufficient. On talking to the supervisor, it was clear some further reading of the SB3 documentation was required. This led to the addition of Gym wrappers (such as `DummyVecEnv` for parallelisation of learning models and `VecFrameStack` to combine multiple frames into one for input into the model's CNN to speed up the learning process). Once these wrappers were added, the model finally began to train. A further addition was when the model makes a step using the Gym environment, the action will be maintained for 4 tics before taking another to ensure that appropriate mappings can be made from the model between action and outcome (see `_ = self.game.make_action(action_vector, 4)` in `step()`).
  
 

- **Curriculum Learning Approach**: To model learning more humanly and provide a smoother learning of objectives for the model, the scenario was split into three levels, under the naming convention `Cacodemon_Recognition_..._.wad/.cfg` for the WAD and configuration files respectively:

    1. `...most_basic.`: This is a level that features a very simple, all similar textured environment that hosts two Cacodemons and only two Cacodemons.

    2. `...basic.`: This is a smaller step up from level 1 by including some torches around the map for visual clutter and two extra enemy types to hone in on Cacodemon recognition; these are a Pain Elemental and two Lost Souls (see [Things and Enemies](https://github.com/BattmannWann/The-VizDoom-Experience/wiki/Enemy-and-Thing-Types) for more information on the enemies used in the project).

    3. `...Final.`: This is the last level which features additional wall textures to provide further visual clutter and two extra types of enemies: `Cyberdemons` and a `Zombieman`

    WAD files can be found in: `src/scenarios/CacodemonRecognition/wad_files` and Configuration files found in: `src/scenarios/CacodemonRecognition/config_files`. The WAD files directory also includes the ACS scripts provided within the WADs themselves as these otherwise wouldn't be visible without a WAD editor. 


- **Further Development of Gymnasium Environments**: These have been split up into one for the baseline and one for the active vision models. Notes:

    - **Baseline Model**: Passes on the full, raw, pixel images from the game to the chosen model (this is PPO for this project). As it is a custom Gym environment, it inherits from the custom model class and implements the required methods. An extra method that was developed here is the "_get_cacodemon_alignment_reward(self)" which aims to break up 

    - **Active Vision Model**: instead of receiving the full raw pixel input (like the baseline model) receives a smaller bounded-box image, with very limited overall view of the game

    


---

### Achieved in the Current Week:

- Trained part of the active vision model to understand how training will work and gauge hyperparameter tunings

- Learning rate was studied further to ensure that the best values were selected. This resulted in a scheduler for learning rate that slowly decreases as time goes on to ensure that the model learns within a reasonable timeframe and learning amount throughout the process. 

- Fine tunings for scripts in ACS and Python files to ensure project completion in due time. 

- Finished level 2 training of the baseline model

---


### Notes from the Meeting

- Refine training objectives, a successful project does NOT mean success in every task completed by the model. Instead, train the baseline on killing only one Cacodemon (the target enemy for the recognition task) given the full input for all three levels to ensure that the models successfully learn a scenario for appropriate comparison later on in the project

- Once baseline model has been trained, train the active vision model in a way that tests how small the bounded-box frame input can be before model training collapses. This provides further insights on how beneficial/detrimental active vision may be in training an agent in this task and provide further insights into how small the input needs to be to outperform the baseline if possible. 

---

### Questions:

- "My baseline model still isn't learning to complete the given task (kill all cacodemons present). I have tried a plethora of hyperparameter tunings and reward shaping values to try and convince the model to learn the scenario fully, but it can only successfully identify one Cacodemon and kill that. What can I do? Is this too complicated?":

    - **Answer**: The answer provided by the supervisor was very helpful and disambiguated a common misconception while taking a level 4 project. The scenario wasn't necessarily too difficult, but having successfully completed tasks isn't entirely necessary to investigate trends between a proposed hypothesis. In this case, it doesn't really matter if the baseline and or active vision model can kill all the Cacodemons if it can at least identify a Cacodemon from other enemies and kill it, as this still adheres to the given task. The supervisor then went on to say that perhaps it would be better to change the scenario goal just to kill one Cacodemon anyways, such that more important testing and analysis can be done, and the original scenario put forward as future work to experiment on how much a model can do at one time. 


---

### Objectives for the Week:

- Refactor the scenario across the models and retrain (where and if possible given time constraints)

- Reduce the bounding box size in general for the active vision model as it is currently just too big, and then, time permitting for this week, try and test how small the bounding box can go before model learning collapses