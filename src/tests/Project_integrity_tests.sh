#!/bin/bash

# CONSTANTS

# === DIRECTORIES ===

PROJ_DIR=$(find ~ -type d -name "The-VizDoom-Experience" -print -quit)

DATA_DIR="${PROJ_DIR}/data/"
MEETINGS_DIR="${PROJ_DIR}/meetings/"

PRESENTATION_DIR="${PROJ_DIR}/presentation/"
SRC_DIR="${PROJ_DIR}/src/"


# === FILES ===

REQUIREMENTS_FILE="${PROJ_DIR}/requirements.txt"
PROJ_README_FILE="${PROJ_DIR}/README.md"
PROJ_PLAN_FILE="${PROJ_DIR}/plan.md"


# === OTHER VARIABLES ===

TESTS_PASSED=0
TOTAL_TESTS=0


# TESTS
printf "==================================================================================\n"
printf "RUNNING TESTS\n"
printf "==================================================================================\n\n"

printf "=== DIRECTORY TESTS ===\n\n"

if [ -d $DATA_DIR ]; then

    printf "Data directory has been found!\n"
    (( TESTS_PASSED += 1 ))

else

    printf "Data directory was not found! Should be at:\n ${DATA_DIR}\n\n"

fi

(( TOTAL_TESTS += 1 ))


if [ -d $MEETINGS_DIR ]; then

    printf "Meetings directory has been found!\n"
    (( TESTS_PASSED += 1 ))

else

    printf "Meetings directory was not found! Should be at:\n ${MEETINGS_DIR}\n\n"

fi

(( TOTAL_TESTS += 1 ))


if [ -d $PRESENTATION_DIR ]; then

    printf "Presentation directory has been found!\n"
    (( TESTS_PASSED += 1 ))

else

    printf "Presentation directory was not found! Should be at:\n ${PRESENTATION_DIR}\n\n"

fi

(( TOTAL_TESTS += 1 ))


if [ -d $SRC_DIR ]; then

    printf "Source (src) directory has been found!\n\n"
    (( TESTS_PASSED += 1 ))

else

    printf "Source (src) directory was not found! Should be at:\n ${SRC_DIR}\n\n"

fi

(( TOTAL_TESTS += 1 ))


printf "==================================================================================\n\n"

printf "=== FILE TESTS ===\n\n"

if [ -f $REQUIREMENTS_FILE ]; then

    printf "Requirements file (requirements.txt) has been found!\n"
    (( TESTS_PASSED += 1 ))

else

    printf "Requirements file (requirements.txt) was not found! Should be at:\n ${REQUIREMENTS_FILE}\n\n"

fi

(( TOTAL_TESTS += 1 ))


if [ -f $PROJ_README_FILE ]; then

    printf "Project overview file (README.md) has been found!\n"
    (( TESTS_PASSED += 1 ))

else

    printf "Project overview file (README.md) was not found! Should be at:\n ${PROJ_README_FILE}\n\n"

fi

(( TOTAL_TESTS += 1 ))


if [ -f $PROJ_PLAN_FILE ]; then

    printf "Project plan file (plan.md) has been found!\n\n"
    (( TESTS_PASSED += 1 ))

else

    printf "Project plan file (plan.md) was not found! Should be at:\n ${PROJ_PLAN_FILE}\n\n"

fi

(( TOTAL_TESTS += 1 ))

printf "==================================================================================\n\n"

PERCENT_TESTS_PASSED=$(( ($TESTS_PASSED / $TOTAL_TESTS) * 100  ))

printf "TESTS COMPLETE \n"
printf "Tests Passed: ${TESTS_PASSED}, Total Tests: ${TOTAL_TESTS}, Percentage: ${PERCENT_TESTS_PASSED}%% \n\n"

printf "\n==================================================================================\n\n"