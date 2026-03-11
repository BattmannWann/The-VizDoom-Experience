#!/bin/bash


# === CONSTANTS ===

PROJ_DIR=$(find ~ -type d -name "The-VizDoom-Experience" -print -quit)
PROJ_INTEGRITY_TEST="Project_integrity_tests.sh"

#=== FUNCTIONS ===

download_and_handle_models() {

    if [ -d "${PROJ_DIR}/data/trained_models" ]; then

        printf "\n Directory for trained models already exists (data/trained_models/). \n Ensure that you have not already downloaded the models.\n "
        printf "If in doubt, delete the trained_models/ directory and try again.\n\n"

        read -p "Would you like to do this now? [y/n]: " confirm 

        if [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then

            rm -rv "${PROJ_DIR}/data/trained_models" &>> "${PROJ_DIR}/error.log"
            rm -rv "${PROJ_DIR}/data/all_trained_models.zip" &>> "${PROJ_DIR}/error.log"

        else
            return 1
        fi

    fi

    wget -a error.log --show-progress -O all_trained_models.zip "https://gla-my.sharepoint.com/:u:/g/personal/2682261s_student_gla_ac_uk/IQDq1_HvkM2rRaXj7agr07ocARJp2bzkpMitYGSAinJOiW0?download=1"
    mv all_trained_models.zip "${PROJ_DIR}/data/" 2>> error.log

    cd "${PROJ_DIR}/data/"
    unzip "${PROJ_DIR}/data/all_trained_models.zip" 2>> error.log

    printf "\nKeeping zip file in case there were any issues unzipping...\n\n"

    cd "${PROJ_DIR}/"
}


test_project() {

    source "${PROJ_DIR}/src/tests/${PROJ_INTEGRITY_TEST}" 2>> error.log
}


create_venv() {

    cd "${PROJ_DIR}"
    cd ..

    read -p "Would you like to customise the name of your virtual environment? [y/n] (default: venv): " confirm

    if [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then
        read -p "Please enter the name of your virtual environment: " venv_name

    else 
        venv_name="venv"
    fi

    python3 -m venv ${venv_name} 2>> "${PROJ_DIR}/error.log"
    source venv/bin/activate 2>> "${PROJ_DIR}/error.log"

    cd "${PROJ_DIR}"
    pip install -r requirements.txt 2>> error.log
}

#=== MAIN SCRIPT ===

printf "=== FOREWORD ===\n\n"
printf "This file has been designed to automatically test and setup the project for use, \nas some files, due to their size, have been removed from the GitHub repository.\n"
printf "\nThis can however be done manually, by following the steps in the build section of the project README:\n https://github.com/BattmannWann/The-VizDoom-Experience#build-steps \n\n"

printf "This file can do the following: \n"
printf "    1. Download the trained models folder, place it in the correct directory, and unzip it\n"
printf "    2. Test that the project has been pulled/downloaded correctly\n"
printf "    3. Create a virtual environment for you and download all required dependencies \n       (UNIX ONLY; REQUIRES PYTHON3 & PIP INSTALLATION)\n"
printf "    4.  \n"

printf "\n\n============================\n\n"


read -p "Would you like to continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || return 0
printf "\n\n"
read -p "Please enter the functionalities that you would like carried out, in a comma separated list or enter ALL for every functionality: [e.g. 1,3]: " function_list
printf "\n\n"


function_list="${function_list// /}"

if [[ "$function_list" == [aA][lL][lL] ]]; then
    functions_array=(1 2 3 4)

else
    
    IFS=',' read -r -a functions_array <<< "$function_list"
fi

problem_items=()

for item in "${functions_array[@]}"; do
    echo "Processing: $item"

    case "$item" in
        1)
            printf "\n Downloading models...\n"
            download_and_handle_models
            ;; 
        2)
            printf "\n Running overall project tests...\n"
            test_project
            ;;
        3)
            printf "\n Creating virtual environment...\n"
            create_venv
            ;;
        4)
            echo "Further processing of 4"
            ;;
        *)
            problem_items+=("$item")
            ;;
    esac
done

if [[ ${#problem_items[@]} -gt 0 ]]; then

    printf "\n\nFunction list contains an invalid option. Any valid functions were carried out, however.\n"
    # shellcheck disable=SC2145
    echo "See problematic items: ${problem_items[@]}"
fi

printf "\n\n"

printf "All tasks have been carried out. "

if [ -f error.log ]; then

    printf "For any issues/errors, see the following:\n\n"

    cat error.log
    rm error.log

fi

printf "\n\n====================== \n\n"
