# Data Directory 

This directory holds the following data:

- **model_performance_data/**: Raw model performance data that has been output on using the `run_model.py` file in `src/scenarios/[scenario_name]/model_evaluation/` when the `--output` flag with suitable value has been enabled on execution. 

<br>

- **trained_models/**: Directories of trained model `.zip` files. As these are quite cumbersome, only the final `.zip` file will be included here. This directory will feature several subdirectories:

    - **[scenario_name]_baseline_models/**: Contains a trained baseline model from each curriculum level in their respective directories (i.e. Level 1/, ..., Level n/)
    - **[scenario_name]_active_vision_models/**: Contains a trained active vision model from each curriculum level. 


<br>

---

### Notes:

- The current project only had time scope for one scenario; the Cacodemon Recognition task. For possible future work, the project has been developed to be mindful to extensions and for modularity between components. 

- Under the `active_vision_models/` directory, within each level directory, models will follow the pattern of `REDUCTION_%_model_TRAINING_STEPS_REACHED`, where `REDUCTION_%` is the percentage reduction rescaled image passed to the CNN. For example, 80_model_157500.zip has a rescaled 80% reduction of the original image. Reductions compared against the original can be better explained using the following table:


    | Scale % | Resolution | Width (px) | Height (px) |
    | :--- | :--- | :--- | :--- |
    | **100% (Original)** | **160x120** | **160** | **120** |
    | 80% | 128x96 | 128 | 96 |
    | 60% | 96x72 | 96 | 72 |
    | 40% | 64x48 | 64 | 48 |
    | 20% | 32x24 | 32 | 24 |
    | 10% | 16x12 | 16 | 12 |
    | 5% | 8x6 | 8 | 6 |
    | 1% | 1x1 | 1 | 1 |


- All commands run to generate model performance files will be listed here in regards to repeatability, as well as what rewards are given across all models and levels, to ensure fair results:


    - **Reward Structure**

        - Level 1: Cacodemon Killed = +20, Living Reward = -1, Bullets Shot = -1
        - Level 2: Cacodemon Killed = +20, Wrong Enemy Killed = -20, Living Reward = -1, Bullets Shot = -1
        - Level 3: SAME AS LEVEL 2

    - Baseline

        - Level 1: `python -m model_evaluation.run_model --in-model-path ../models_baseline/Level\ 1/model_2450000.zip --config-path 0 --episodes 100 --output baseline_lvl_1_model`

        - Level 2: `python -m model_evaluation.run_model --in-model-path ../models_baseline/Level\ 2/model_3720000.zip --config-path 1 --episodes 100 --output baseline_lvl_2_model`

        - Level 3: Will be tested both with the `Level 1` model and the `Level 2` model. So, the above commands change into:

            - Level 1: `python -m model_evaluation.run_model --in-model-path ../models_baseline/Level\ 1/model_2450000.zip --config-path 2 --episodes 100 --output baseline_lvl_1_model_on_lvl_3`

            - Level 2: `python -m model_evaluation.run_model --in-model-path ../models_baseline/Level\ 2/model_3720000.zip --config-path 2 --episodes 100 --output baseline_lvl_2_model_on_lvl_3`


    - Active

        - Level 1 

            - 100%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_24_100/model_1275000.zip --active "true" --config-path 0 --reduction 0 --episodes 100 --output active_lvl_1_100_model`

            - 80%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_16_80/model_1575000.zip --active "true" --config-path 0 --reduction 80 --episodes 100 --output active_lvl_1_80_model`

            - 60%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_23_60/model_1950000.zip --active "true" --config-path 0 --reduction 60 --episodes 100 --output active_lvl_1_60_model`

            - 40%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_18_40/model_3025000.zip --active "true" --config-path 0 --reduction 40 --episodes 100 --output active_lvl_1_40_model`

            - 20%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_19_20/model_1975000.zip --active "true" --config-path 0 --reduction 20 --episodes 100 --output active_lvl_1_20_model`

            - 10%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_20_10/model_2000000.zip --active "true" --config-path 0 --reduction 10 --episodes 100 --output active_lvl_1_10_model`

            - 5%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_21_5/model_2100000.zip --active "true" --config-path 0 --reduction 5 --episodes 100 --output active_lvl_1_5_model`

            - 1%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_22_1/model_2100000.zip --active "true" --config-path 0 --reduction 1 --episodes 100 --output active_lvl_1_1_model`


        - Level 2

            - 100%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_26_100/model_4700000.zip --active "true" --config-path 1 --reduction 0 --episodes 100 --output active_lvl_2_100_model.txt`

            - 80%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_19_80/model_6350000.zip --active "true" --config-path 1 --reduction 80 --episodes 100 --output active_lvl_2_80_model`

            - 60%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_20_60/model_6475000.zip --active "true" --config-path 1 --reduction 60 --episodes 100 --output active_lvl_2_60_model`

            - 40%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_21_40/model_3000000.zip --active "true" --config-path 1 --reduction 40 --episodes 100 --output active_lvl_2_40_model`

            - 20%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_22_20/model_6850000.zip --active "true" --config-path 1 --reduction 20 --episodes 100 --output active_lvl_2_20_model`

            - 10%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_23_10/model_2650000.zip --active "true" --config-path 1 --reduction 10 --episodes 100 --output active_lvl_2_10_model`

            - 5%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_24_5/model_2800000.zip --active "true" --config-path 1 --reduction 5 --episodes 100 --output active_lvl_2_5_model`

            - 1%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_27_1/model_4775000.zip --active "true" --config-path 1 --reduction 1 --episodes 100 --output active_lvl_2_1_model`


        - Level 3: Each trained model on each percentage reduction of each level will be tested in this unknown environment, to understand how, if at all, generalisable the actions and understanding that the model learned is. This means that the `--config-path` needs to be changed to 2, and a suitable output file name chosen.
                    

            - Level 1 onto 3:

                - 100%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_24_100/model_1275000.zip --active "true" --config-path 2 --reduction 0 --episodes 100 --output active_lvl_1_on_3_100_model`

                - 80%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_16_80/model_1575000.zip --active "true" --config-path 2 --reduction 80 --episodes 100 --output active_lvl_1_on_3_80_model`

                - 60%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_23_60/model_1950000.zip --active "true" --config-path 2 --reduction 60 --episodes 100 --output active_lvl_1_on_3_60_model`

                - 40%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_18_40/model_3025000.zip --active "true" --config-path 2 --reduction 40 --episodes 100 --output active_lvl_1_on_3_40_model`

                - 20%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_19_20/model_1975000.zip --active "true" --config-path 2 --reduction 20 --episodes 100 --output active_lvl_1_on_3_20_model`

                - 10%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_20_10/model_2000000.zip --active "true" --config-path 2 --reduction 10 --episodes 100 --output active_lvl_1_on_3_10_model`

                - 5%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_21_5/model_2100000.zip --active "true" --config-path 2 --reduction 5 --episodes 100 --output active_lvl_1_on_3_5_model`

                - 1%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_22_1/model_2100000.zip --active "true" --config-path 2 --reduction 1 --episodes 100 --output active_lvl_1_on_3_1_model`


            - Level 2 onto 3:

                - 100%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_26_100/model_4700000.zip --active "true" --config-path 2 --reduction 0 --episodes 100 --output active_lvl_2_on_3_100_model`

                - 80%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_19_80/model_6350000.zip --active "true" --config-path 2 --reduction 80 --episodes 100 --output active_lvl_2_on_3_80_model`

                - 60%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_20_60/model_6475000.zip --active "true" --config-path 2 --reduction 60 --episodes 100 --output active_lvl_2_on_3_60_model`

                - 40%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_21_40/model_3000000.zip --active "true" --config-path 2 --reduction 40 --episodes 100 --output active_lvl_2_on_3_40_model`

                - 20%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_22_20/model_6850000.zip --active "true" --config-path 2 --reduction 20 --episodes 100 --output active_lvl_2_on_3_20_model`

                - 10%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_23_10/model_2650000.zip --active "true" --config-path 2 --reduction 10 --episodes 100 --output active_lvl_2_on_3_10_model`

                - 5%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_24_5/model_2800000.zip --active "true" --config-path 2 --reduction 5 --episodes 100 --output active_lvl_2_on_3_5_model`

                - 1%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_27_1/model_4775000.zip --active "true" --config-path 2 --reduction 1 --episodes 100 --output active_lvl_2_on_3_1_model`
