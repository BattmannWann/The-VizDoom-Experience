import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def generate_learning_curve(csv_filepath, window_size=50, learned_threshold=0):
    """
    Generates a learning curve graph from a Gym Monitor CSV format.
    Expects columns: 'r' (reward), 'l' (length), 't' (time).
    """
    csv_path = Path(csv_filepath)
    
    if not csv_path.exists():
        raise FileNotFoundError(f"Could not find the CSV file: {csv_filepath}")
        
    print(f"Loading data from {csv_path.name}...")
    
    # Read CSV, automatically skipping the first JSON metadata line that starts with '#'
    df = pd.read_csv(csv_path, comment='#')
    
    # Ensure expected columns exist
    if not {'r', 'l', 't'}.issubset(df.columns):
        raise ValueError(f"CSV {csv_path.name} must contain 'r', 'l', and 't' columns.")

    # Convert the Monitor format into our plotting variables
    # The current Training Step is the cumulative sum of all past episode lengths
    df['Step'] = df['l'].cumsum()
    df['Value'] = df['r']

    plt.figure(figsize=(12, 6))

    # Plot raw data
    plt.plot(df['Step'], df['Value'], alpha=0.3, color='gray', label='Raw Episode Reward')

    # Plot rolling average
    df['Rolling_Avg'] = df['Value'].rolling(window=window_size, min_periods=1).mean()
    plt.plot(df['Step'], df['Rolling_Avg'], color='blue', linewidth=2, label=f'{window_size}-Episode Rolling Average')

    # Find when the model "learned"
    learned_df = df[df['Rolling_Avg'] >= learned_threshold]
    
    if not learned_df.empty:
        learned_step = learned_df['Step'].min()
        
        # Draw vertical line
        plt.axvline(x=learned_step, color='red', linestyle='--', linewidth=2, 
                    label=f'Model Learned (Step ~{int(learned_step):,})')
        
        # Dynamically calculate text position so it scales to ANY dataset
        x_offset = (df['Step'].max() - df['Step'].min()) * 0.02 # 2% to the right of the line
        y_pos = df['Value'].min() + (df['Value'].max() - df['Value'].min()) * 0.15 # 15% up from the bottom
        
        plt.text(learned_step + x_offset, y_pos, 'Stable Learning\nAchieved', 
                 color='red', fontsize=12, weight='bold')
        
        print(f"Model reached threshold ({learned_threshold}) at step: {int(learned_step):,}")
        
    else:
        print(f"Notice: Model never reached the learning threshold of {learned_threshold} in this dataset.")

    # Formatting
    plt.title(f'Agent Learning Curve: {csv_path.stem}', fontsize=16, fontweight='bold')
    plt.xlabel('Total Training Steps', fontsize=12)
    
    plt.ylabel('Episode Reward', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Add commas to X-axis numbers for readability
    plt.gca().get_xaxis().set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
    
    plt.legend(loc='lower right', fontsize=12)
    plt.tight_layout()

    # Save dynamically named file in the same directory as the CSV
    output_filename = csv_path.parent / f"{csv_path.stem}_learning_curve.png"
    plt.savefig(output_filename, dpi=300)
    plt.show()
    
    print(f"Graph saved successfully to: {output_filename}")


if __name__ == "__main__":
    
    # --- CONFIGURATION ---
    TARGET_CSV = "./env_monitor_1_24_100.csv.monitor.csv" 
    
    try:
        generate_learning_curve(
            csv_filepath=TARGET_CSV, 
            window_size=10000,          
            learned_threshold=10    
        )
    except Exception as e:
        print(f"Error: {e}")