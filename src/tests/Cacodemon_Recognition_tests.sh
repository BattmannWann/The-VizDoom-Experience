#!/bin/bash

#CONSTANTS

ACTIVE_MODELS_DIR="../models_active/"
BASELINE_MODELS_DIR="../models_baseline/"

TESTS_PASSED=0

printf "=== Pre-test setup evaluation: ===\n\n"
printf "CHECKING DIRECTORIES..."

if [ -d ${ACTIVE_MODELS_DIR} ]; then

    printf "\n ${ACTIVE_MODELS_DIR} EXISTS!"
    (( TESTS_PASSED += 1 ))

else
    printf "\n ${ACTIVE_MODELS_DIR}\n DOES NOT EXIST!. Please see: https://github.com/BattmannWann/The-VizDoom-Experience#build-steps 
    \n on ensuring that the directories are set up accordingly to run evaluations. \n\n"

fi


if [ -d ${BASELINE_MODELS_DIR} ]; then

    printf "\n ${BASELINE_MODELS_DIR} EXISTS!\n"
    (( TESTS_PASSED += 1 ))

else
    printf "\n ${BASELINE_MODELS_DIR}\n DOES NOT EXIST!. Please see: https://github.com/BattmannWann/The-VizDoom-Experience#build-steps 
    \n on ensuring that the directories are set up accordingly to run evaluations. \n\n"

fi


printf "\n\nTESTING COMPLETED\n"
printf "    Tests Passed: ${TESTS_PASSED}\n\n"

printf "=========================================\n\n" 
