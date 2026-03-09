#!/bin/bash

# printf "=== BASELINE EVALUATION === \n"

# printf "    LEVEL 1: \n"
# python -m model_evaluation.run_model --in-model-path ../models_baseline/Level\ 1/model_2450000.zip --config-path 0 --episodes 100 --output baseline_lvl_1_model

# printf "    LEVEL 2: \n"
# python -m model_evaluation.run_model --in-model-path ../models_baseline/Level\ 2/model_3720000.zip --config-path 1 --episodes 100 --output baseline_lvl_2_model

# printf "    LEVEL 3 using LEVEL 1 trained model: \n"
# python -m model_evaluation.run_model --in-model-path ../models_baseline/Level\ 1/model_2450000.zip --config-path 2 --episodes 100 --output baseline_lvl_1_model_on_lvl_3

# printf "    LEVEL 3 using LEVEL 1 trained model: \n"
# python -m model_evaluation.run_model --in-model-path ../models_baseline/Level\ 2/model_3720000.zip --config-path 2 --episodes 100 --output baseline_lvl_2_model_on_lvl_3


#     - Active

#         - Level 1 

#             - 100%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_24_100/model_1275000.zip --active "true" --config-path 0 --reduction 0 --episodes 100 --output active_lvl_1_100_model`

#             - 80%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_16_80/model_1575000.zip --active "true" --config-path 0 --reduction 80 --episodes 100 --output active_lvl_1_80_model`

#             - 60%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_23_60/model_1950000.zip --active "true" --config-path 0 --reduction 60 --episodes 100 --output active_lvl_1_60_model`

#             - 40%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_18_40/model_3025000.zip --active "true" --config-path 0 --reduction 40 --episodes 100 --output active_lvl_1_40_model`

#             - 20%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_19_20/model_1975000.zip --active "true" --config-path 0 --reduction 20 --episodes 100 --output active_lvl_1_20_model`

#             - 10%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_20_10/model_2000000.zip --active "true" --config-path 0 --reduction 10 --episodes 100 --output active_lvl_1_10_model`

#             - 5%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_21_5/model_2100000.zip --active "true" --config-path 0 --reduction 5 --episodes 100 --output active_lvl_1_5_model`

#             - 1%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_22_1/model_2100000.zip --active "true" --config-path 0 --reduction 1 --episodes 100 --output active_lvl_1_1_model`


#         - Level 2

#             - 100%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_26_100/model_4700000.zip --active "true" --config-path 1 --reduction 0 --episodes 100 --output active_lvl_2_100_model.txt`

#             - 80%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_19_80/model_6350000.zip --active "true" --config-path 1 --reduction 80 --episodes 100 --output active_lvl_2_80_model`

#             - 60%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_20_60/model_6475000.zip --active "true" --config-path 1 --reduction 60 --episodes 100 --output active_lvl_2_60_model`

#             - 40%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_21_40/model_3000000.zip --active "true" --config-path 1 --reduction 40 --episodes 100 --output active_lvl_2_40_model`

#             - 20%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_22_20/model_6850000.zip --active "true" --config-path 1 --reduction 20 --episodes 100 --output active_lvl_2_20_model`

#             - 10%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_23_10/model_2650000.zip --active "true" --config-path 1 --reduction 10 --episodes 100 --output active_lvl_2_10_model`

#             - 5%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_24_5/model_2800000.zip --active "true" --config-path 1 --reduction 5 --episodes 100 --output active_lvl_2_5_model`

#             - 1%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_27_1/model_4775000.zip --active "true" --config-path 1 --reduction 1 --episodes 100 --output active_lvl_2_1_model`


#         - Level 3: Each trained model on each percentage reduction of each level will be tested in this unknown environment, to understand how, if at all, generalisable the actions and understanding that the model learned is. This means that the `--config-path` needs to be changed to 2, and a suitable output file name chosen.
                    

#             - Level 1 onto 3:

#                 - 100%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_24_100/model_1275000.zip --active "true" --config-path 2 --reduction 0 --episodes 100 --output active_lvl_1_on_3_100_model`

#                 - 80%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_16_80/model_1575000.zip --active "true" --config-path 2 --reduction 80 --episodes 100 --output active_lvl_1_on_3_80_model`

#                 - 60%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_23_60/model_1950000.zip --active "true" --config-path 2 --reduction 60 --episodes 100 --output active_lvl_1_on_3_60_model`

#                 - 40%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_18_40/model_3025000.zip --active "true" --config-path 2 --reduction 40 --episodes 100 --output active_lvl_1_on_3_40_model`

#                 - 20%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_19_20/model_1975000.zip --active "true" --config-path 2 --reduction 20 --episodes 100 --output active_lvl_1_on_3_20_model`

#                 - 10%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_20_10/model_2000000.zip --active "true" --config-path 2 --reduction 10 --episodes 100 --output active_lvl_1_on_3_10_model`

#                 - 5%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_21_5/model_2100000.zip --active "true" --config-path 2 --reduction 5 --episodes 100 --output active_lvl_1_on_3_5_model`

#                 - 1%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 1/Cacodemon_Recognition_1_22_1/model_2100000.zip --active "true" --config-path 2 --reduction 1 --episodes 100 --output active_lvl_1_on_3_1_model`


#             - Level 2 onto 3:

#                 - 100%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_26_100/model_4700000.zip --active "true" --config-path 2 --reduction 0 --episodes 100 --output active_lvl_2_on_3_100_model`

#                 - 80%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_19_80/model_6350000.zip --active "true" --config-path 2 --reduction 80 --episodes 100 --output active_lvl_2_on_3_80_model`

#                 - 60%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_20_60/model_6475000.zip --active "true" --config-path 2 --reduction 60 --episodes 100 --output active_lvl_2_on_3_60_model`

#                 - 40%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_21_40/model_3000000.zip --active "true" --config-path 2 --reduction 40 --episodes 100 --output active_lvl_2_on_3_40_model`

#                 - 20%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_22_20/model_6850000.zip --active "true" --config-path 2 --reduction 20 --episodes 100 --output active_lvl_2_on_3_20_model`

#                 - 10%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_23_10/model_2650000.zip --active "true" --config-path 2 --reduction 10 --episodes 100 --output active_lvl_2_on_3_10_model`

#                 - 5%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_24_5/model_2800000.zip --active "true" --config-path 2 --reduction 5 --episodes 100 --output active_lvl_2_on_3_5_model`

#                 - 1%: `python -m model_evaluation.run_model --in-model-path ../models_active/Rescaled/Level\ 2/Cacodemon_Recognition_2_27_1/model_4775000.zip --active "true" --config-path 2 --reduction 1 --episodes 100 --output active_lvl_2_on_3_1_model`
