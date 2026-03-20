import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import re
import os

def extract_model_name(filepath):
    """Helper function to create clean legend labels from filenames."""
    name = Path(filepath).stem.replace('.monitor', '').replace('.csv', '')
    
    # Try to make the names look a bit nicer (e.g., active_10_model -> Active (10%))
    if "active" in name.lower():
        match = re.search(r'_(\d+)_', name)
        if match:
            return f"Active ({match.group(1)}% FOV)"
        return "Active Model"
    elif "baseline" in name.lower():
        return "Baseline Model"
    return name.replace("_", " ").title()



def get_graphs(file_list, save_dir):
    
    generate_averaged_learning_curve(
        csv_filepaths=file_list,
        save_path=f"{save_dir}/compound_learning_curve.pdf",
        window_size=1000
    )


def get_proj_root():
    curr_path = Path(__file__).resolve()
    
    for parent in [curr_path] + list(curr_path.parents):
        if (parent / ".git").exists() or (parent / "requirements.txt").exists():
            return parent
        
    raise FileNotFoundError("could not locate project root directory")


def get_csv_monitor_files(dir_path, active = False):
    
    files_list_lvl_1 = []
    files_list_lvl_2 = []
    files_list = []
    
    for filepath in dir_path.rglob('*'):
        
        if ".csv.monitor.csv" in str(filepath):
        
            if active:
                
                if "level 1" in str(filepath).lower():
                    files_list_lvl_1.append(str(filepath))
                    
                elif "level 2" in str(filepath).lower():
                    files_list_lvl_2.append(str(filepath))
                    
                    
            else:
                files_list.append(str(filepath))
                
    
    if active:
            
        assert len(files_list_lvl_1) + len(files_list_lvl_2) == 16, f"""ERROR, make sure that you have downloaded the trained_models dir successfully. 
        Some csv files are missing: should be {16}, have {len(files_list)}"""
        
    else:
        
        assert len(files_list) == 2, f"""ERROR,  make sure that you have downloaded the trained_models dir successfully.
        Some csv files are missing: should be {2}, have {len(files_list)}"""
        
    return files_list, files_list_lvl_1, files_list_lvl_2


def generate_averaged_learning_curve(csv_filepaths, save_path=None, window_size=50):
    """
    Takes multiple RL monitor files, aligns their timelines, and plots 
    a single averaged learning curve with variance shading.
    """
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({'font.size': 12, 'font.family': 'serif'})
    
    dfs = []
    max_steps = []
    
    # 1. Load and prepare all files
    for file in csv_filepaths:
        file_path = Path(file)
        if not file_path.exists():
            print(f"Skipping - File not found: {file_path}")
            continue
            
        try:
            df = pd.read_csv(file_path, skiprows=1)
            if not all(col in df.columns for col in ['r', 'l']):
                continue
                
            # Calculate cumulative steps
            df['Step'] = df['l'].cumsum()
            
            # Smooth the raw data FIRST before we average the files together
            df['Smoothed_Reward'] = df['r'].rolling(window=window_size, min_periods=1).mean()
            
            dfs.append(df)
            max_steps.append(df['Step'].max())
            
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    if not dfs:
        print("No valid data found to plot.")
        return

    # 2. Create a common timeline
    # We stop at the shortest file's max step so we don't extrapolate false data
    global_min_step = 0
    global_max_step = min(max_steps) 
    
    # Create 1,000 evenly spaced points across the timeline
    common_steps = np.linspace(global_min_step, global_max_step, num=1000)
    
    all_interpolated_rewards = []

    # 3. Align all runs to the common timeline
    for df in dfs:
        # np.interp estimates what the reward was at our exact common_steps
        aligned_rewards = np.interp(common_steps, df['Step'], df['Smoothed_Reward'])
        all_interpolated_rewards.append(aligned_rewards)
        
    # Convert to a 2D numpy array: Shape is (Number of Files, 1000)
    reward_matrix = np.array(all_interpolated_rewards)
    
    # 4. Calculate the true mathematical average and variance
    mean_rewards = reward_matrix.mean(axis=0)
    std_rewards = reward_matrix.std(axis=0)

    # 5. Build the Graph
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot the thick average line
    ax.plot(common_steps, mean_rewards, color='blue', linewidth=2.5, 
            label=f'Mean Performance ({len(dfs)} runs)')
    
    # Shade the variance (+/- 1 Standard Deviation)
    ax.fill_between(common_steps, 
                    mean_rewards - std_rewards, 
                    mean_rewards + std_rewards, 
                    color='blue', alpha=0.2, edgecolor="none",
                    label='± 1 Std Dev')

    # Add environment target thresholds if desired
    for thresh in [0, 5, 9]:
        ax.axhline(y=thresh, color='gray', linestyle=':', linewidth=1.5, alpha=0.7)

    # Formatting
    ax.set_title("Averaged Learning Curve Across Multiple Runs", pad=15, fontweight='bold')
    ax.set_xlabel("Environment Steps", weight='bold')
    ax.set_ylabel("Cumulative Episode Reward", weight='bold')
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax.legend(loc='lower right')
    
    plt.tight_layout()
    
    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, format='pdf', dpi=300, bbox_inches='tight')
        print(f"Graph saved to: {save_path}")
        
    plt.show()

# === Example Usage ===
if __name__ == "__main__":
    
    
    proj_root = get_proj_root()
    data_dir = proj_root / "data" 
    
    graph_dir = data_dir / "Graphs" / "Training_Graphs"
    active_models_dir = data_dir / "trained_models/Cacodemon_Recognition_active_vision_models"
    baseline_model_dir = data_dir / "trained_models/Cacodemon_Recognition_baseline_models"
    
    active_path = Path(active_models_dir)
    baseline_path = Path(baseline_model_dir)
    
    _, active_lvl_1, active_lvl_2 = get_csv_monitor_files(active_path, active=True)
    baseline_files_for_graphing, _, _ = get_csv_monitor_files(baseline_path)
    
    
    if not os.path.exists(f"{graph_dir}/active_models"):
        os.makedirs(f"{graph_dir}/active_models")
    
    
    if not os.path.exists(f"{graph_dir}/baseline_models"):
        os.makedirs(f"{graph_dir}/baseline_models")
   
    get_graphs(baseline_files_for_graphing, f"{graph_dir}/baseline_aggregate/")
    get_graphs(active_lvl_1, f"{graph_dir}/active_aggregate/level 1/")
    get_graphs(active_lvl_2, f"{graph_dir}/active_aggregate/level 2/")
    