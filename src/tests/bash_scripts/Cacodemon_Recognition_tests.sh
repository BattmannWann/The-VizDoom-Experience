#!/bin/bash

# CONSTANTS

# === DIRECTORIES ===

PROJ_DIR=$(find ~ -type d -name "The-VizDoom-Experience" -print -quit)
CACODEMON_SRC="$PROJ_DIR/src/scenarios/CacodemonRecognition"

TRAINING_FILES_DIR="${CACODEMON_SRC}/training_files"

ACTIVE_TRAINED_MODELS_DIR="${PROJ_DIR}/data/trained_models/Cacodemon_Recognition_active_vision_models"
BASELINE_TRAINED_MODELS_DIR="${PROJ_DIR}/data/trained_models/Cacodemon_Recognition_baseline_models"

ERROR_LOG="${PROJ_DIR}/src/tests/bash_scripts/error.log"
SCRIPTS_TEST_DIR="${PROJ_DIR}/src/tests/bash_scripts"

PARENT_DIR=$(dirname "$PROJ_DIR")
VENV_PYTHON="${PARENT_DIR}/venv/bin/python"


#FUNCTIONS
remove_folders_active() {

    rm -r "${CACODEMON_SRC}/models_active/TEST/"
    rm -r "${CACODEMON_SRC}/logs_active/TEST/"

}


remove_folders_baseline() {

    rm -r "${CACODEMON_SRC}/models_baseline/TEST/"
    rm -r "${CACODEMON_SRC}/logs_baseline/TEST/"
}

#python -m "active_vision_model_training.active_visual_model_training_lvl_1" 2>> error.log



train_model() {

    local type=$1
    local level=$2

    cd "${TRAINING_FILES_DIR}" || true

    if [ $type == "active" ]; then

        remove_folders_active

        if [ $level == 1 ]; then

            python -m active_vision_model_training.active_visual_model_training_lvl_1 --test "true" 2>> "$ERROR_LOG"

        elif [ $level == 2 ]; then

            python -m active_vision_model_training.active_visual_model_training_lvl_2 --test "true" 2>> "$ERROR_LOG"

        fi

    elif [ $type == "baseline" ]; then

        remove_folders_baseline

        if [ $level == 1 ]; then

            python -m baseline_model_training.baseline_training_lvl_1 --test "true" 2>> "$ERROR_LOG"

        elif [ $level == 2 ]; then

            python -m baseline_model_training.baseline_training_lvl_2 --test "true" 2>> "$ERROR_LOG"

        fi


    fi

    cd "${SCRIPTS_TEST_DIR}" || true
}


run_model() {

    local model_type=$1

    local model_file_active="Level 2/20_model_6850000.zip"
    local model_path_active="${ACTIVE_TRAINED_MODELS_DIR}/${model_file_active}"

    local model_file_baseline="Level 2/model_3720000.zip"
    local model_path_baseline="${BASELINE_TRAINED_MODELS_DIR}/${model_file_baseline}"

    local active_output="TEST_RUN_ACTIVE.txt"
    local baseline_output="TEST_RUN_BASELINE.txt"

    cd "${TRAINING_FILES_DIR}" || true

    if [ ! -d "${SCRIPTS_TEST_DIR}/results" ]; then
        mkdir -p "${SCRIPTS_TEST_DIR}/results" 
    fi

    if [ "$model_type" == "active" ]; then
        
        python -m model_evaluation.run_model --in-model-path "${model_path_active}" --config-path 1 --verbose 'true' --active 'true' --reduction 20 --sleep 0.035 --episodes 4 --output "$active_output" 2>> "$ERROR_LOG"
        mv "${PROJ_DIR}/data/model_performance_data/${active_output}" "${SCRIPTS_TEST_DIR}/results/"
    
    else
        
        python -m model_evaluation.run_model --in-model-path "${model_path_baseline}" --config-path 1 --sleep 0.035 --episodes 4 --output "$baseline_output" 2>> "$ERROR_LOG"
        mv "${PROJ_DIR}/data/model_performance_data/${baseline_output}" "${SCRIPTS_TEST_DIR}/results/"
    fi

    cd "${SCRIPTS_TEST_DIR}" || true
}


print_success() {

    local error_code=$1

    if [ "$error_code" -eq 0 ]; then

        printf "\n\nTest %d ran successfully! \n" "$total_tests"
        (( tests_passed+=1 ))

    else 
        printf "\n\nTest %d FAILED! Error code: %s , See logs at the end for more details. \n" "$total_tests" "$error_code" 
        problem_tests+=("$total_tests")

    fi

    (( total_tests+=1 ))
}

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
printf "If you have not, then %s can both create the venv and download the dependencies if you require assistance. \n\n" "${PROJ_DIR}/setup_project.sh"


printf "\n=================\n\n" 



if [[ ! "$1" == "-y" ]]; then
    read -r -p "Would you like to continue? [y/n]: " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || return 0
fi

printf "\n\n"
printf "=== TESTS ===\n\n"

#=== PRE-TEST SETUP ===

total_tests=0
tests_passed=0
problem_tests=()

# ==============================================

printf "\n\n === Test Suite 1: Training Models === \n\n"

printf "Test Objectives: \n"
printf "    - Window pops up \n"
printf "    - Model can be seen interacting with the environment \n"
printf "    - Model performance is logged successfully in logs_'model_type'/TEST/\n"
printf "    - Model weights are stored into models_type/TEST/ \n\n"

printf "(Where 'model_type(s)' in [active, baseline]) \n"
sleep 2


printf "\nRunning Test %d : Run active_visual_model_training_lvl_1.py \n\n" "${total_tests}"

train_model "active" "1"
print_success "$?"


printf "\nRunning Test %d : Run active_visual_model_training_lvl_2.py \n\n" "${total_tests}"

train_model "active" "2"
print_success "$?"


printf "\nRunning Test %d : Run baseline_training_lvl_1.py \n\n" "${total_tests}"

train_model "baseline" "1"
print_success "$?"

printf "\nRunning Test %d : Run baseline_training_lvl_2.py \n\n" "${total_tests}"

train_model "baseline" "2"
print_success "$?"


printf "\n\n=== END OF TEST SUITE 1 === \n\n"


printf "=== Test Suite 2: Model Evaluation (run_model.py) ==="

printf "Test Objectives: \n\n"
printf "    - Window pops up showing the scenario, enemies, and the agent's weapon \n"

printf "    - Agent weights have been loaded in correctly, based on performance
      (i.e. does the agent seek out and kill the Cacodemon?) \n\n"

printf "    - Agent performance can be successfully saved and written to disk (into a file):
       This file will be found in the test directory under 'results/TEST_RUN_model_type.txt' \n"


printf "\nRunning Test %d : run_model.py on Baseline Model" "${total_tests}"
run_model "baseline"
print_success "$?"


printf "\nRunning Test %d : run_model.py on Active Model" "${total_tests}"
run_model "active"
print_success "$?"

printf "\n\n=== END OF TEST SUITE 2 === \n\n"


#END OF TESTS
printf "\n\n=== TESTING COMPLETED ===\n"

percent_complete=$(( (tests_passed * 100) / total_tests ))
printf "    Tests Passed: %s  Tests Run: %s, Percentage: %s %% \n\n" "${tests_passed}" "${total_tests}" "${percent_complete}"

if [[ ${#problem_tests[@]} -gt 0 ]]; then

    printf "\n\nSome tests were unsuccessful.\n"
    # shellcheck disable=SC2145
    echo "See problematic tests: ${problem_tests[@]}"

    printf "And see the error log for more information: \n\n"
    echo "TO EXIT, PRESS 'q' " >> "$ERROR_LOG"
    less "$ERROR_LOG"
    rm "$ERROR_LOG"
fi

printf "\n\n=========================================\n\n"


