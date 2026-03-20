import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np


def get_proj_root():
    curr_path = Path(__file__).resolve()
    
    for parent in [curr_path] + list(curr_path.parents):
        if (parent / ".git").exists() or (parent / "requirements.txt").exists():
            return parent
        
    raise FileNotFoundError("could not locate project root directory")


def generate_large_learning_curve(csv_filepath, window_size=10000, learned_threshold=0, max_plot_points=5000, save_dir = ""):
    """
    Optimized to graph massive RL Monitor logs (1M+ rows) without crashing.
    Uses rolling means and shaded standard deviation bands.
    """
    csv_path = Path(csv_filepath)
    if not csv_path.exists():
        raise FileNotFoundError(f"Could not find the CSV file: {csv_filepath}")
        
    print(f"Loading {csv_path.name} (This might take a few seconds for 1M+ rows)...")
    
    # Read CSV, skipping the metadata row
    df = pd.read_csv(csv_path, comment='#')
    
    if not {'r', 'l', 't'}.issubset(df.columns):
        raise ValueError(f"CSV {csv_path.name} must contain 'r', 'l', and 't' columns.")

    print("Crunching the numbers...")
    # Calculate continuous training steps
    df['Step'] = df['l'].cumsum()
    
    # 1. Calculate Rolling Mean and Standard Deviation on the FULL dataset
    # Because your data is huge, we need a large window (e.g., 10,000 episodes) to get a smooth line
    df['Rolling_Mean'] = df['r'].rolling(window=window_size, min_periods=1).mean()
    df['Rolling_Std'] = df['r'].rolling(window=window_size, min_periods=1).std().fillna(0)

    # 2. Downsample for Plotting
    # Matplotlib will choke on 1.3M points. We reduce it to a safe number (e.g., 5000 points)
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

    # 5. Find when the model "learned"
    learned_df = df[df['Rolling_Mean'] > learned_threshold]
    
    if not learned_df.empty:
        learned_step = learned_df['Step'].min()
        
        plt.axvline(x=learned_step, color='red', linestyle='--', linewidth=2, 
                    label=f'Model Learned (Step ~{int(learned_step):,})')
        
        # Dynamic text placement
        x_offset = (plot_df['Step'].max() - plot_df['Step'].min()) * 0.02 
        y_pos = plot_df['Rolling_Mean'].min() + (plot_df['Rolling_Mean'].max() - plot_df['Rolling_Mean'].min()) * 0.15 
        
        plt.text(learned_step + x_offset, y_pos, f'Stable Learning\nAchieved ({learned_threshold} Reward)', 
                 color='red', fontsize=12, weight='bold')
        print(f"Model successfully reached threshold ({learned_threshold}) at step: {int(learned_step):,}")
    else:
        print(f"Notice: Model never reached the learning threshold of {learned_threshold}.")

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


if __name__ == "__main__":
    
    TARGET_CSV = "./env_monitor_1_24_100.csv.monitor.csv" 

    proj_root = get_proj_root()
    data_dir = proj_root / "data" / "Graphs" / "Training_Graphs"
    
    try:
        generate_large_learning_curve(
            csv_filepath=TARGET_CSV, 
            window_size=10000,       
            learned_threshold=10,     
            max_plot_points=5000,
            save_dir = data_dir     
        )
    except Exception as e:
        print(f"Error: {e}")