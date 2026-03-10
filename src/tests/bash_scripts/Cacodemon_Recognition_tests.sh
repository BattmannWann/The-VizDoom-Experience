#!/bin/bash

# CONSTANTS

# === DIRECTORIES ===

PROJ_DIR=$(find ~ -type d -name "The-VizDoom-Experience" -print -quit)
CACODEMON_SRC="$PROJ_DIR/src/scenarios/CacodemonRecognition"

TRAINING_FILES_DIR="${CACODEMON_SRC}/training_files"

ACTIVE_VISION_TRAINING_DIR="$/active_vision_model_training/"
BASELINE_TRAINING_DIR="$/baseline_model_training/"



#TESTS

printf "\n\n=== FOREWORD ===\n\n"
printf "This file has been designed to run the files within the Cacodemon Recognition scenario found under: \n %s \n" "$CACODEMON_SRC"
printf "It will: \n\n"

printf "    - Ensure that the model training files supplied can be run. These are under 'training_files/' : \n"
printf "        - active_visual_model_training_lvl_1.py : A file for training active models under level 1 \n"
printf "        - active_visual_model_training_lvl_2.py : A file for training active models under level 2 \n"
printf "        - baseline_training_lvl_1.py : A file for training baseline models under level 1 \n"
printf "        - baseline_training_lvl_2.py : A file for training baseline models under level 2 \n\n"

printf "    - Ensure that the models can be evaluated. These files are found under 'training_files/model_evaluation/' : \n"
printf "        - evaluate_models.sh : A script that runs all the trained models on every level and condition \n"
printf "        - run_model.py : The underlying python script that loads and runs a model, collecting results \n\n"

printf "Due to the coupled nature of some of the files above, the following will also be implicitly tested alongside: \n\n"

printf "   - Files under the 'training_files/envs/' directory: \n"
printf "       - Active_Visual_Cacodemon_Recognition_env.py: The environment provided for active vision models \n"
printf "       - Baseline_Cacodemon_recognition_env.py: The environment provided for baseline models \n\n"

printf "   - Files under the 'config_files/' directory: \n"
printf "       - Cacodemon_Recognition_ basic/most_basic/Final .cfg: 
          The varying configuration files for levels 1,2, and 3 respectively; used by the environment files. \n\n"

printf "   - Files under the 'wad_files' directory: \n"
printf "       - Cacodemon_Recognition_ basic/most_basic/Final .wad: The WAD files for levels 1,2, and 3 respectively. 
\n These are used by the .cfg files to load in the correct DOOM maps. \n\n"

printf "Any implicit testing that regards a Python file will be given explicit tests in the 'tests/Python Tests' directory. \n"
printf "If any further information is required regarding these files and their functionalities, please see the following resources: \n\n"
printf "   - The README.md files found in the majority of directories \n"
printf "   - The project README.md/WIKI which can be found in the respective links: \n\n"
printf "       - https://github.com/BattmannWann/The-VizDoom-Experience#vizdoom-visual-learning-environment \n"
printf "       - https://github.com/BattmannWann/The-VizDoom-Experience/wiki \n\n"

printf "For these tests to work, you MUST have activated your virtual environment and have installed all required dependencies.\n"
printf "If you have not, then %s can both create the venv and download the dependencies if you require assistance. \n\n" "{$PROJ_DIR}/setup_project.sh"


printf "\n=================\n\n" 

read -r -p "Would you like to continue? [y/n]: " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || return 0
printf "\n\n"

printf "=== TESTS ===\n\n"

#=== PRE-TEST SETUP ===

total_tests=0
tests_passed=0
problem_tests=()

rm -r "${CACODEMON_SRC}/models_active/TEST/"
rm -r "${CACODEMON_SRC}/logs_active/TEST/"

# ==============================================

printf "Running Test 1: Run active_visual_model_training_lvl_1.py \n\n"
printf "Test Objectives: \n"
printf "    - Window pops up \n"
printf "    - Model can be seen interacting with the environment \n"
printf "    - Model performance is logged successfully in logs_active/TEST/ \n"
printf "    - Model weights are stored into models_active/TEST/ \n"

sleep 2

cd "${TRAINING_FILES_DIR}"

python -m "active_vision_model_training.active_visual_model_training_lvl_1" 2>> error.log

(( total_tests+=1 ))

exec_status=$?

if [ $exec_status -eq 0 ]; then

    printf "\n\nTest ran successfully! \n"
    (( tests_passed+=1 ))

else 
    printf "\n\nTest FAILED! Error code: %s , See logs at the end for more details. \n" "$exec_status"
    problem_tests+=("$total_tests")

fi

cd "${PROJ_DIR}/src/tests/bash_scripts/"


printf "Running Test 2"

printf "\n\nTESTING COMPLETED\n"
printf "    Tests Passed: %s  Tests Run: %s \n\n" "${tests_passed}" "{$total_tests}"

printf "=========================================\n\n"


