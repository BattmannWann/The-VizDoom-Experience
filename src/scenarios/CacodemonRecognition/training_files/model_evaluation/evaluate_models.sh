#!/bin/bash

# CONSTANTS

PROJ_DIR=$(find ~ -type d -name "The-VizDoom-Experience" -print -quit)

TRAINED_MODELS_DIR="${PROJ_DIR}/data/trained_models"
ACTIVE_DIR="${TRAINED_MODELS_DIR}/Cacodemon_Recognition_active_vision_models"
BASELINE_DIR="${TRAINED_MODELS_DIR}/Cacodemon_Recognition_baseline_models"

# TESTS

if [ ! -d "$TRAINED_MODELS_DIR" ]; then

    printf "TRAINED MODELS DIRECTORY %s  DOES NOT EXIST \n" "${TRAINED_MODELS_DIR}"
    printf "Please setup the project before trying again. You can use the setup_proj.sh file to do this"

    exit 0

fi


# MAIN

printf "\n\n=== FOREWORD ===\n\n"
printf "This file has been designed to run all of the evaluations for each model type, level, and level condition, on the Cacodemon Recognition scenario. 
    Specifically, it can run: \n\n"

printf "    - Baseline Models: \n"
printf "        - Level 1 \n"
printf "        - Level 2 \n"

printf "    - Active Vision Models: \n"
printf "        - Level 1: With reduction set: {None, 1, 5, 10, 20, 40, 60, 80%%} \n"
printf "        - Level 2: With reduction set: {None, 1, 5, 10, 20, 40, 60, 80%%} \n"

printf "\n=================\n\n" 


printf "=== BASELINE EVALUATION === \n"

printf "    LEVEL 1: \n"
python -m model_evaluation.run_model --in-model-path "${BASELINE_DIR}/Level 1/model_2450000.zip" --config-path 0 --episodes 100 --output baseline_lvl_1_model

printf "    LEVEL 2: \n"
python -m model_evaluation.run_model --in-model-path "${BASELINE_DIR}/Level 2/model_3720000.zip" --config-path 1 --episodes 100 --output baseline_lvl_2_model

printf "    LEVEL 3 using LEVEL 1 trained model: \n"
python -m model_evaluation.run_model --in-model-path "${BASELINE_DIR}/Level 1/model_2450000.zip" --config-path 2 --episodes 100 --output baseline_lvl_1_model_on_lvl_3

printf "    LEVEL 3 using LEVEL 2 trained model: \n"
python -m model_evaluation.run_model --in-model-path "${BASELINE_DIR}/Level 2/model_3720000.zip" --config-path 2 --episodes 100 --output baseline_lvl_2_model_on_lvl_3

printf "    LEVEL 2 using LEVEL 1 trained model: \n"
python -m model_evaluation.run_model --in-model-path "${BASELINE_DIR}/Level 1/model_2450000.zip" --config-path 1 --episodes 100 --output baseline_lvl_1_model_on_lvl_2

printf "    LEVEL 1 using LEVEL 2 trained model: \n"
python -m model_evaluation.run_model --in-model-path "${BASELINE_DIR}/Level 2/model_3720000.zip" --config-path 0 --episodes 100 --output baseline_lvl_2_model_on_lvl_1


printf "\n=================\n\n" 

printf "=== ACTIVE VISION EVALUATION === \n"

printf "\n=== ACTIVE LEVEL 1 ===\n"

printf "    100%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/100_model_1275000.zip" --active "true" --config-path 0 --reduction 0 --episodes 100 --output active_lvl_1_100_model

printf "    80%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/80_model_1575000.zip" --active "true" --config-path 0 --reduction 80 --episodes 100 --output active_lvl_1_80_model

printf "    60%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/60_model_1950000.zip" --active "true" --config-path 0 --reduction 60 --episodes 100 --output active_lvl_1_60_model

printf "    40%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/40_model_3025000.zip" --active "true" --config-path 0 --reduction 40 --episodes 100 --output active_lvl_1_40_model

printf "    20%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/20_model_1975000.zip" --active "true" --config-path 0 --reduction 20 --episodes 100 --output active_lvl_1_20_model

printf "    10%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/10_model_2000000.zip" --active "true" --config-path 0 --reduction 10 --episodes 100 --output active_lvl_1_10_model

printf "    5%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/5_model_2100000.zip" --active "true" --config-path 0 --reduction 5 --episodes 100 --output active_lvl_1_5_model

printf "    1%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/1_model_2100000.zip" --active "true" --config-path 0 --reduction 1 --episodes 100 --output active_lvl_1_1_model


printf "\n=== ACTIVE LEVEL 2 ===\n"

printf "    100%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/100_model_4700000.zip" --active "true" --config-path 1 --reduction 0 --episodes 100 --output active_lvl_2_100_model.txt

printf "    80%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/80_model_6350000.zip" --active "true" --config-path 1 --reduction 80 --episodes 100 --output active_lvl_2_80_model

printf "    60%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/60_model_6475000.zip" --active "true" --config-path 1 --reduction 60 --episodes 100 --output active_lvl_2_60_model

printf "    40%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/40_model_3000000.zip" --active "true" --config-path 1 --reduction 40 --episodes 100 --output active_lvl_2_40_model

printf "    20%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/20_model_6850000.zip" --active "true" --config-path 1 --reduction 20 --episodes 100 --output active_lvl_2_20_model

printf "    10%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/10_model_2650000.zip" --active "true" --config-path 1 --reduction 10 --episodes 100 --output active_lvl_2_10_model

printf "    5%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/5_model_2800000.zip" --active "true" --config-path 1 --reduction 5 --episodes 100 --output active_lvl_2_5_model

printf "    1%%: \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/1_model_4775000.zip" --active "true" --config-path 1 --reduction 1 --episodes 100 --output active_lvl_2_1_model


printf "\n=== ACTIVE LEVEL 3 (Unknown Environment Testing) ===\n"
printf "Each trained model on each percentage reduction will be tested in an unknown environment to gauge generalisation.\n\n"

printf "    LEVEL 1 onto 3 (100%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/100_model_1275000.zip" --active "true" --config-path 2 --reduction 0 --episodes 100 --output active_lvl_1_on_3_100_model

printf "    LEVEL 1 onto 3 (80%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/80_model_1575000.zip" --active "true" --config-path 2 --reduction 80 --episodes 100 --output active_lvl_1_on_3_80_model

printf "    LEVEL 1 onto 3 (60%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/60_model_1950000.zip" --active "true" --config-path 2 --reduction 60 --episodes 100 --output active_lvl_1_on_3_60_model

printf "    LEVEL 1 onto 3 (40%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/40_model_3025000.zip" --active "true" --config-path 2 --reduction 40 --episodes 100 --output active_lvl_1_on_3_40_model

printf "    LEVEL 1 onto 3 (20%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/20_model_1975000.zip" --active "true" --config-path 2 --reduction 20 --episodes 100 --output active_lvl_1_on_3_20_model

printf "    LEVEL 1 onto 3 (10%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/10_model_2000000.zip" --active "true" --config-path 2 --reduction 10 --episodes 100 --output active_lvl_1_on_3_10_model

printf "    LEVEL 1 onto 3 (5%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/5_model_2100000.zip" --active "true" --config-path 2 --reduction 5 --episodes 100 --output active_lvl_1_on_3_5_model

printf "    LEVEL 1 onto 3 (1%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/1_model_2100000.zip" --active "true" --config-path 2 --reduction 1 --episodes 100 --output active_lvl_1_on_3_1_model


printf "    LEVEL 2 onto 3 (100%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/100_model_4700000.zip" --active "true" --config-path 2 --reduction 0 --episodes 100 --output active_lvl_2_on_3_100_model

printf "    LEVEL 2 onto 3 (80%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/80_model_6350000.zip" --active "true" --config-path 2 --reduction 80 --episodes 100 --output active_lvl_2_on_3_80_model

printf "    LEVEL 2 onto 3 (60%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/60_model_6475000.zip" --active "true" --config-path 2 --reduction 60 --episodes 100 --output active_lvl_2_on_3_60_model

printf "    LEVEL 2 onto 3 (40%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/40_model_3000000.zip" --active "true" --config-path 2 --reduction 40 --episodes 100 --output active_lvl_2_on_3_40_model

printf "    LEVEL 2 onto 3 (20%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/20_model_6850000.zip" --active "true" --config-path 2 --reduction 20 --episodes 100 --output active_lvl_2_on_3_20_model

printf "    LEVEL 2 onto 3 (10%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/10_model_2650000.zip" --active "true" --config-path 2 --reduction 10 --episodes 100 --output active_lvl_2_on_3_10_model

printf "    LEVEL 2 onto 3 (5%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/5_model_2800000.zip" --active "true" --config-path 2 --reduction 5 --episodes 100 --output active_lvl_2_on_3_5_model

printf "    LEVEL 2 onto 3 (1%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/1_model_4775000.zip" --active "true" --config-path 2 --reduction 1 --episodes 100 --output active_lvl_2_on_3_1_model


printf "\n=== ACTIVE CROSS-EVALUATION (Level 1 on Level 2) ===\n"
printf "Testing Level 1 trained models on Level 2 environment.\n\n"

printf "    LEVEL 1 onto 2 (100%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/100_model_1275000.zip" --active "true" --config-path 1 --reduction 0 --episodes 100 --output active_lvl_1_on_2_100_model

printf "    LEVEL 1 onto 2 (80%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/80_model_1575000.zip" --active "true" --config-path 1 --reduction 80 --episodes 100 --output active_lvl_1_on_2_80_model

printf "    LEVEL 1 onto 2 (60%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/60_model_1950000.zip" --active "true" --config-path 1 --reduction 60 --episodes 100 --output active_lvl_1_on_2_60_model

printf "    LEVEL 1 onto 2 (40%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/40_model_3025000.zip" --active "true" --config-path 1 --reduction 40 --episodes 100 --output active_lvl_1_on_2_40_model

printf "    LEVEL 1 onto 2 (20%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/20_model_1975000.zip" --active "true" --config-path 1 --reduction 20 --episodes 100 --output active_lvl_1_on_2_20_model

printf "    LEVEL 1 onto 2 (10%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/10_model_2000000.zip" --active "true" --config-path 1 --reduction 10 --episodes 100 --output active_lvl_1_on_2_10_model

printf "    LEVEL 1 onto 2 (5%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/5_model_2100000.zip" --active "true" --config-path 1 --reduction 5 --episodes 100 --output active_lvl_1_on_2_5_model

printf "    LEVEL 1 onto 2 (1%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 1/1_model_2100000.zip" --active "true" --config-path 1 --reduction 1 --episodes 100 --output active_lvl_1_on_2_1_model


printf "\n=== ACTIVE CROSS-EVALUATION (Level 2 on Level 1) ===\n"
printf "Testing Level 2 trained models on Level 1 environment.\n\n"

printf "    LEVEL 2 onto 1 (100%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/100_model_4700000.zip" --active "true" --config-path 0 --reduction 0 --episodes 100 --output active_lvl_2_on_1_100_model

printf "    LEVEL 2 onto 1 (80%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/80_model_6350000.zip" --active "true" --config-path 0 --reduction 80 --episodes 100 --output active_lvl_2_on_1_80_model

printf "    LEVEL 2 onto 1 (60%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/60_model_6475000.zip" --active "true" --config-path 0 --reduction 60 --episodes 100 --output active_lvl_2_on_1_60_model

printf "    LEVEL 2 onto 1 (40%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/40_model_3000000.zip" --active "true" --config-path 0 --reduction 40 --episodes 100 --output active_lvl_2_on_1_40_model

printf "    LEVEL 2 onto 1 (20%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/20_model_6850000.zip" --active "true" --config-path 0 --reduction 20 --episodes 100 --output active_lvl_2_on_1_20_model

printf "    LEVEL 2 onto 1 (10%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/10_model_2650000.zip" --active "true" --config-path 0 --reduction 10 --episodes 100 --output active_lvl_2_on_1_10_model

printf "    LEVEL 2 onto 1 (5%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/5_model_2800000.zip" --active "true" --config-path 0 --reduction 5 --episodes 100 --output active_lvl_2_on_1_5_model

printf "    LEVEL 2 onto 1 (1%%): \n"
python -m model_evaluation.run_model --in-model-path "${ACTIVE_DIR}/Level 2/1_model_4775000.zip" --active "true" --config-path 0 --reduction 1 --episodes 100 --output active_lvl_2_on_1_1_model