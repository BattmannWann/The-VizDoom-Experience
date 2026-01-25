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


