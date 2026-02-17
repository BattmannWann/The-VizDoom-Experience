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

