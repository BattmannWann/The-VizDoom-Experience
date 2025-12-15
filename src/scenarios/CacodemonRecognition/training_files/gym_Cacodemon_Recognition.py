from gymnasium.envs.registration import register

DEFAULT_VIZDOOM_ENTRYPOINT = (
    "vizdoom.gymnasium_wrapper.gymnasium_env_defns:VizdoomScenarioEnv"
)

register(
    id="VizdoomCacodemonRecognition-v0",
    entry_point=DEFAULT_VIZDOOM_ENTRYPOINT,
    kwargs={"scenario_config_file": "/home/battmannwann/Projects/Individual_Project/The-VizDoom-Experience/src/scenarios/CacodemonRecognition/config_files/Cacodemon_Recognition.cfg", "max_buttons_pressed": 1},
)