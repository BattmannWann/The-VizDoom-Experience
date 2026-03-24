import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import os
import matplotlib.cm as cm


#FUNCTIONS

def get_proj_root():
    curr_path = Path(__file__).resolve()
    
    for parent in [curr_path] + list(curr_path.parents):
        if (parent / ".git").exists() or (parent / "requirements.txt").exists():
            return parent
        
    raise FileNotFoundError("could not locate project root directory")


def get_csv_monitor_files(dir_path):
    
    files_list = []
    
    for filepath in dir_path.rglob('*'):
        
        if ".csv.monitor.csv" in str(filepath):
           files_list.append(str(filepath))
           
    
    if "active" in str(dir_path):
            
        assert len(files_list) == 16, f"""ERROR, make sure that you have downloaded the trained_models dir successfully. 
        Some csv files are missing: should be {16}, have {len(files_list)}"""
        
    else:
        
        assert len(files_list) == 2, f"""ERROR,  make sure that you have downloaded the trained_models dir successfully.
        Some csv files are missing: should be {2}, have {len(files_list)}"""
        
    return files_list


def get_graphs(file_list, model_type = "baseline"):
    
    for file in file_list:
        
        try:
            generate_large_learning_curve(
                csv_filepath=file, 
                window_size=10000,       
                learned_thresholds=[-20, -10, -5, -1, 0, 5, 10],     
                max_plot_points=5000,
                save_dir = graph_dir / f"{model_type}_models"    
            )
        
        except Exception as e:
            print(f"Error: {e}")


def generate_large_learning_curve(csv_filepath, window_size=10000, learned_thresholds=[-5, 0, 5, 10], max_plot_points=5000, save_dir = ""):
    """
    Optimized to graph massive RL Monitor logs (1M+ rows) without crashing.
    Uses rolling means and shaded standard deviation bands.
    """
    csv_path = Path(csv_filepath)
    
    colours = [cm.plasma(x) for x in np.linspace(0, 1, len(learned_thresholds))]
    
    if not csv_path.exists():
        raise FileNotFoundError(f"Could not find the CSV file: {csv_filepath}")
    
    print(f'\n\n{"=" * 20}\n')
        
    print(f"Loading {csv_path.name} (This might take a few seconds for 1M+ rows)...")
    
    # Read CSV, skipping the metadata row
    df = pd.read_csv(csv_path, comment='#')
    
    if not {'r', 'l', 't'}.issubset(df.columns):
        raise ValueError(f"CSV {csv_path.name} must contain 'r', 'l', and 't' columns.")

    print("Crunching the numbers...")
    # Calculate continuous training steps
    df['Step'] = df['l'].cumsum()
    
    # 1. Calculate Rolling Mean and Standard Deviation on the FULL dataset
    # Because data is huge, need a large window (e.g., 10,000 episodes) to get a smooth line
    df['Rolling_Mean'] = df['r'].rolling(window=window_size, min_periods=1).mean()
    df['Rolling_Std'] = df['r'].rolling(window=window_size, min_periods=1).std().fillna(0)

    # 2. Downsample for Plotting
    # Matplotlib will choke on 1.3M points. FIX: reduce it to a safe number (e.g., 5000 points)
    # This does NOT change the math, it only skips drawing redundant pixels.
    step_size = max(1, len(df) // max_plot_points)
    plot_df = df.iloc[::step_size].copy()

    plt.figure(figsize=(12, 6))

    # 3. Plot the Shaded Standard Deviation Band (Replaces the raw gray spikes)
    plt.fill_between(
        plot_df['Step'], 
        plot_df['Rolling_Mean'] - plot_df['Rolling_Std'], 
        plot_df['Rolling_Mean'] + plot_df['Rolling_Std'], 
        color='blue', alpha=0.15, label='Rolling Standard Deviation'
    )

    # 4. Plot the solid Rolling Average line
    plt.plot(
        plot_df['Step'], plot_df['Rolling_Mean'], 
        color='blue', linewidth=2, label=f'{window_size:,}-Episode Rolling Mean'
    )

    # 5. Iterate through the pairs
    for i, (thresh, col) in enumerate(zip(learned_thresholds, colours)):
    
        # Filter using the rolling mean
        learned_df = df[df['Rolling_Mean'] >= thresh]
        
        if not learned_df.empty:
            learned_step = learned_df['Step'].min()
            
            # Draw the vertical line
            plt.axvline(x=learned_step, color=col, linestyle='--', linewidth=2, 
                        label=f'Model Learned >= {thresh} (Step ~{int(learned_step):,})')
            
            # Dynamic text placement using your plot_df logic
            x_offset = (plot_df['Step'].max() - plot_df['Step'].min()) * 0.02 
            
            # Multiply by (0.15 + i*0.1) so the labels stack and don't overlap
            y_pos = plot_df['Rolling_Mean'].min() + (plot_df['Rolling_Mean'].max() - plot_df['Rolling_Mean'].min()) * (0.15 + (i * 0.1)) 
            
            
            print(f"Model successfully reached threshold ({thresh}) at step: {int(learned_step):,}")
            
        else:
        
            # 1. Find the actual highest rolling mean achieved
            actual_max = df['Rolling_Mean'].max()
            
            # # 2. Draw a horizontal dotted line at that peak
            # plt.axvline(x=actual_max, color=col, linestyle=':', linewidth=2, alpha=0.7,
            #             label=f'Peak: {actual_max:.2f} (Missed {thresh})')
            
            
            print(f"Notice: Model never reached threshold {thresh}. Plotted peak line at {actual_max:.2f}.")


    # Call this after the loop so all threshold lines appear in the legend
    plt.legend(loc='best')
            

    # 6. Call legend after the loop to show all labels
    plt.legend(loc='best', fontsize='small')

    # 6. Formatting
    plt.title(f'Agent Learning Curve: {csv_path.stem}', fontsize=16, fontweight='bold')
    plt.xlabel('Total Training Steps', fontsize=12)
    
    plt.ylabel('Episode Reward', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.gca().get_xaxis().set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend(loc='lower right', fontsize=12)
    plt.tight_layout()

    # Save output
    output_filename = save_dir / f"{csv_path.stem}_optimized_curve.png"
    plt.savefig(output_filename, dpi=300)
    plt.show()
    
    print(f"Graph rendered and saved to: {output_filename}")
    
    print(f'\n\n{"=" * 20}\n')


if __name__ == "__main__":

    proj_root = get_proj_root()
    data_dir = proj_root / "data" 
    
    graph_dir = data_dir / "Graphs" / "Training_Graphs"
    active_models_dir = data_dir / "trained_models/Cacodemon_Recognition_active_vision_models"
    baseline_model_dir = data_dir / "trained_models/Cacodemon_Recognition_baseline_models"
    
    active_path = Path(active_models_dir)
    baseline_path = Path(baseline_model_dir)
    
    active_files_for_graphing = get_csv_monitor_files(active_path)
    baseline_files_for_graphing = get_csv_monitor_files(baseline_path)
    
    
    if not os.path.exists(f"{graph_dir}/active_models"):
        os.makedirs(f"{graph_dir}/active_models")
    
    
    if not os.path.exists(f"{graph_dir}/baseline_models"):
        os.makedirs(f"{graph_dir}/baseline_models")
    
    
    get_graphs(active_files_for_graphing, "active")
    get_graphs(baseline_files_for_graphing, "baseline")
    
    
    