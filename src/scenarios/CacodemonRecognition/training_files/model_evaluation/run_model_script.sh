#!/bin/bash

# =================================================================
#  Interactive Launcher for Cacodemon Recognition Model
# =================================================================

printf "\n=== Cacodemon Recognition Model Evaluation ===\n"

# Define the python execution command
PYTHON_EXEC="python"
MODULE_NAME="model_evaluation.run_model"

# --- 1. Global Settings (Config & Active Mode) ---

# 1a. Config Path
printf "Config Path Level:\n 0 = Most Basic\n 1 = Basic\n 2 = Final\n"
read -p "Select Config [Default: 0]: " config_path
config_path=${config_path:-0}

# 1b. Active Vision Mode
read -p "Enable Active Vision Mode? (y/n) [Default: n]: " active_input

if [[ "$active_input" =~ ^[yY] ]]; then
    active_arg="true"
    
    # Active Vision Specific Args
    printf "\n  [Active Vision Settings]\n"
    read -p "  Reduction % (0-100) [Default: 0]: " reduction
    reduction=${reduction:-0}

    read -p "  Use Padding? (y/n) [Default: n]: " padded_input

    if [[ "$padded_input" =~ ^[yY] ]]; then
        padded_arg="true" 

    else
        padded_arg="false"
    fi
    printf "\n"

else
    active_arg="false"
    reduction=0
    padded_arg="false"
fi


# --- 2. Model Path Selection ---

# Define your default paths here based on Config Level (0, 1, 2) Type (Active/Baseline), Reduction (if active), Reduction Style (if active)
if [ "$active_arg" == "true" ]; then

    if [ "$padded_arg" == "false" ]; then

        if [ "$config_path" == 0 ]; then
    
            case $reduction in
                #0) DEFAULT_PATH="";;
                80) DEFAULT_PATH="../models_active/Rescaled/Level 1/Cacodemon_Recognition_1_16_80/model_1575000.zip" ;;
                60) DEFAULT_PATH="../models_active/Rescaled/Level 1/Cacodemon_Recognition_1_23_60/model_1950000.zip" ;;
                40) DEFAULT_PATH="../models_active/Rescaled/Level 1/Cacodemon_Recognition_1_18_40/model_3025000.zip" ;;
                20) DEFAULT_PATH="../models_active/Rescaled/Level 1/Cacodemon_Recognition_1_19_20/model_1975000.zip" ;;
                10) DEFAULT_PATH="../models_active/Rescaled/Level 1/Cacodemon_Recognition_1_20_10/model_2000000.zip" ;;
                5)  DEFAULT_PATH="../models_active/Rescaled/Level 1/Cacodemon_Recognition_1_21_5/model_2100000.zip" ;;
                1)  DEFAULT_PATH="../models_active/Rescaled/Level 1/Cacodemon_Recognition_1_22_1/model_2100000.zip" ;;
            esac

        fi


        if [ "$config_path" == 1 ||  "$config_path" == 2 ]; then
    
            case $reduction in
                0)  DEFAULT_PATH="../models_active/Rescaled/Level 2/Cacodemon_Recognition_2_26_100/model_4800000.zip" ;;
                80) DEFAULT_PATH="../models_active/Rescaled/Level 2/Cacodemon_Recognition_2_19_80/model_6350000.zip" ;;
                60) DEFAULT_PATH="../models_active/Rescaled/Level 2/Cacodemon_Recognition_2_20_60/model_6475000.zip" ;;
                40) DEFAULT_PATH="../models_active/Rescaled/Level 2/Cacodemon_Recognition_2_21_40/model_3200000.zip" ;;
                20) DEFAULT_PATH="../models_active/Rescaled/Level 2/Cacodemon_Recognition_2_22_20/model_6850000.zip" ;;
                10) DEFAULT_PATH="../models_active/Rescaled/Level 2/Cacodemon_Recognition_2_23_10/model_7100000.zip" ;;
                5)  DEFAULT_PATH="../models_active/Rescaled/Level 2/Cacodemon_Recognition_2_24_5/model_7125000.zip" ;;
                1)  DEFAULT_PATH="../models_active/Rescaled/Level 2/Cacodemon_Recognition_2_27_1/model_4775000.zip" ;;
            esac  

        fi   
        
    fi

else

    case $config_path in
        0) DEFAULT_PATH="../models_baseline/Level 1/model_2450000.zip" ;;
        1) DEFAULT_PATH="../models_baseline/Level 2/model_3720000.zip" ;;
        2) DEFAULT_PATH="../models_baseline/Level 2/model_3720000.zip" ;;
    esac
fi

# Ask the user: Use default or custom?
if [ -n "$DEFAULT_PATH" ]; then
    printf "Recommended Model Path: $DEFAULT_PATH\n"
    read -p "Use this default path? (y/n) [Default: y]: " use_default
    use_default=${use_default:-y}

else
    # If couldn't determine a default (e.g. invalid config level), force custom
    use_default="n"
fi

if [[ "$use_default" =~ ^[yY] ]]; then
    model_path="$DEFAULT_PATH"

else
    # Custom Path Input Loop
    while [[ -z "$model_path" ]]; do

        read -e -p "Enter custom path to trained model (.zip): " model_path

        if [[ -z "$model_path" ]]; then
            printf "Error: Model path is required.\n"

        elif [[ ! -f "$model_path" ]]; then
            printf "Warning: File '$model_path' does not exist. Please check the path.\n"
            
        fi
    done
fi


# --- 3. Remaining Settings ---

# Episode Count
read -p "Number of episodes to run [Default: 5]: " episodes
episodes=${episodes:-5}

# Sleep Delay
read -p "Sleep delay between actions (e.g. 0.038 for human-speed) [Default: 0.0]: " sleep_val
sleep_val=${sleep_val:-0.0}

# Verbosity
read -p "Enable Verbose Logging? (y/n) [Default: n]: " verbose_input
if [[ "$verbose_input" =~ ^[yY] ]]; then
    verbose_arg="true"

else
    verbose_arg="false"
fi

# Output File
read -p "Output filename (Press Enter for none/false): " output_file
output_file=${output_file:-"false"}


# =================================================================
#  Execution
# =================================================================

printf "\n---------------------------------------------------------\n"
printf "Launching Python Script..."
printf "\n---------------------------------------------------------\n"

# Move up one directory as requested in your snippet
cd ..

# Construct command
CMD="$PYTHON_EXEC -m $MODULE_NAME \
    --in-model-path \"$model_path\" \
    --episodes $episodes \
    --sleep $sleep_val \
    --active \"$active_arg\" \
    --config-path $config_path \
    --verbose \"$verbose_arg\" \
    --output \"$output_file\" \
    --reduction $reduction \
    --padded \"$padded_arg\""

# Print command for verification
echo "$CMD"
echo ""

# Run it
eval $CMD

cd model_evaluation/