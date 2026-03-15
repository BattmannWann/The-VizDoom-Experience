#!/bin/bash

# CONSTANTS

# === DIRECTORIES ===

PROJ_DIR=$(find ~ -type d -name "The-VizDoom-Experience" -print -quit)

DATA_DIR="${PROJ_DIR}/data/"
MEETINGS_DIR="${PROJ_DIR}/meetings/"

PRESENTATION_DIR="${PROJ_DIR}/presentation/"
SRC_DIR="${PROJ_DIR}/src/"

TRAINED_MODELS_DIR="${DATA_DIR}trained_models/"


# === FILES ===

REQUIREMENTS_FILE="${PROJ_DIR}/requirements.txt"
PROJ_README_FILE="${PROJ_DIR}/README.md"
PROJ_PLAN_FILE="${PROJ_DIR}/plan.md"


# === OTHER VARIABLES ===

tests_passed=0
total_tests=0


# TESTS

printf "\n\n=== FOREWORD ===\n\n"
printf "This file has been designed to check the integrity of the project file system. It will do the following: \n\n"
printf "    - Check that all required folders (that which are not checked by programs already) exist\n"
printf "    - Check that all required files (that aren't automatically generated) exist\n"

printf "\n=================\n\n"

if [ ! "$1" == -y ]; then
    read -r -p "Would you like to continue? [y/n]: " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || return 0
fi

printf "\n\n"

printf "==================================================================================\n"
printf "RUNNING TESTS\n"
printf "==================================================================================\n\n"

printf "=== DIRECTORY TESTS ===\n\n"

if [ -d "$DATA_DIR" ]; then

    printf "Data directory has been found!\n"
    (( tests_passed += 1 ))

else

    printf "Data directory was not found! Should be at:\n %s \n\n" "${DATA_DIR}"

fi

(( total_tests += 1 ))


if [ -d "$TRAINED_MODELS_DIR" ]; then

    printf "Trained models directory has been found!\n"
    (( tests_passed += 1 ))

else

    printf "\n\nTrained models directory was not found! Should be at: \n %s \n\n" "${TRAINED_MODELS_DIR}"
    printf "You will want to ensure to download these! \n\n" 

    printf "There is guidance in the project README.md or this can be done automatically by the setup_project.sh script 
found in the root project directory: \n %s \n\n" "${PROJ_DIR}/setup_project.sh"


fi

(( total_tests += 1 ))


if [ -d "$MEETINGS_DIR" ]; then

    printf "Meetings directory has been found!\n"
    (( tests_passed += 1 ))

else

    printf "Meetings directory was not found! Should be at:\n %s \n\n" "${MEETINGS_DIR}"

fi

(( total_tests += 1 ))


if [ -d "$PRESENTATION_DIR" ]; then

    printf "Presentation directory has been found!\n"
    (( tests_passed += 1 ))

else

    printf "Presentation directory was not found! Should be at:\n %s \n\n" "${PRESENTATION_DIR}"

fi

(( total_tests += 1 ))


if [ -d "$SRC_DIR" ]; then

    printf "Source (src) directory has been found!\n\n"
    (( tests_passed += 1 ))

else

    printf "Source (src) directory was not found! Should be at:\n %s \n\n" "${SRC_DIR}"

fi

(( total_tests += 1 ))


if [ -d "${SRC_DIR}scenarios/" ]; then

    printf "Scenarios directory has been found!\n\n"
    (( tests_passed += 1 ))

else

    printf "Scenarios directory was not found! Should be at:\n %s \n\n" "${SRC_DIR}scenarios"

fi

(( total_tests += 1 ))


if [ -d "${SRC_DIR}scenarios/CacodemonRecognition" ]; then

    printf "Cacodemon Recognition scenario directory has been found!\n\n"
    (( tests_passed += 1 ))

else

    printf "Cacodemon Recognition scenario directory was not found! Should be at:\n %s \n\n" "${SRC_DIR}scenarios/CacodemonRecognition"

fi

(( total_tests += 1 ))

printf "==================================================================================\n\n"

printf "=== FILE TESTS ===\n\n"

if [ -f "$REQUIREMENTS_FILE" ]; then

    printf "Requirements file (requirements.txt) has been found!\n"
    (( tests_passed += 1 ))

else

    printf "Requirements file (requirements.txt) was not found! Should be at:\n %s \n\n" "${REQUIREMENTS_FILE}"
 
fi

(( total_tests += 1 ))


if [ -f "$PROJ_README_FILE" ]; then

    printf "Project overview file (README.md) has been found!\n"
    (( tests_passed += 1 ))

else

    printf "Project overview file (README.md) was not found! Should be at:\n %s \n\n" "${PROJ_README_FILE}"

fi

(( total_tests += 1 ))


if [ -f "$PROJ_PLAN_FILE" ]; then

    printf "Project plan file (plan.md) has been found!\n\n"
    (( tests_passed += 1 ))

else

    printf "Project plan file (plan.md) was not found! Should be at:\n %s \n\n" "${PROJ_PLAN_FILE}"

fi

(( total_tests += 1 ))

printf "==================================================================================\n\n"

percent_tests_passed=$(( (tests_passed * 100) / total_tests ))

printf "TESTS COMPLETE \n"
printf "Tests Passed: ${tests_passed}, Total Tests: ${total_tests}, Percentage: ${percent_tests_passed}%% \n\n"

printf "\n==================================================================================\n\n"