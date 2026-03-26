# All Logs Directory

This directory holds ALL the logs for the Active and Baseline models, including the reruns with different seeds.

This is a massive directory, as such, when running tensorboard, select a specific directory within this parent directory. On that note, the baseline reruns can be found within the `Baseline/` directory. However, as the active models generate significantly more logs in total (due to the several FOV reductions which have their own models), these have been extracted out into their own directory: `logs_active_different_seeds/`.

To see the logs in tensorboard, issue the following command:

`tensorboard --logdir logs_dir_name_here/`