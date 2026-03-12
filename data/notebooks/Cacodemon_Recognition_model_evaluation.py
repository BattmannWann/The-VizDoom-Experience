import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import scipy.stats as stats
from statannotations.Annotator import Annotator

def get_proj_root():
    curr_path = Path(__file__).resolve()
    
    for parent in [curr_path] + list(curr_path.parents):
        if (parent / ".git").exists() or (parent / "requirements.txt").exists():
            return parent
        
    raise FileNotFoundError("could not locate project root directory")


def parse_rewards_file(filepath):
    """Parses the text file to extract episode rewards using regex."""
    with open(filepath, 'r') as file:
        content = file.read()
    
    # Regex to find all reward values. Matches: 'Episode X': <value>
    # captures positive, negative, integer, and float numbers
    rewards = re.findall(r"'Episode \d+':\s*([-+]?[0-9]*\.?[0-9]+)", content)

    return [float(r) for r in rewards]


def load_data(root_dir):
    """Traverses the directory structure and compiles data into a DataFrame."""
    data = []
    root_path = Path(root_dir)
    
    # Check if directory exists
    if not root_path.exists():
        raise FileNotFoundError(f"Directory {root_dir} not found.")

    # Walk through all directories and files
    for filepath in root_path.rglob('*'):
        if filepath.is_file():
                
            # Determine Model Type from parent directories
            if "Active Models" in filepath.parts:
                model_type = "Active"
            elif "Baseline Models" in filepath.parts:
                model_type = "Baseline"
            else:
                continue # Skip files not in these directories
                
            # Determine Level from parent directories (e.g., "Level 1", "Level 2")
            level_match = re.search(r'Level (\d+)', str(filepath))
            level = f"Level {level_match.group(1)}" if level_match else "Unknown Level"
            
            # Determine Percentage Reduction from filename (only for Active models)
            reduction = None
            if model_type == "Active":
                reduction_match = re.search(r'(100|80|60|40|20|10|5|1)(?=\D|$)', filepath.stem)
                if reduction_match:
                    reduction = int(reduction_match.group(1))
            
            # Extract rewards
            rewards = parse_rewards_file(filepath)
            
            # Append each episode's data
            for ep_num, reward in enumerate(rewards):
                data.append({
                    'Model_Type': model_type,
                    'Level': level,
                    'Reduction': reduction,
                    'Episode': ep_num,
                    'Reward': reward,
                    'Filename': filepath.name
                })
                
    return pd.DataFrame(data)


def generate_plots(df, save_dir):
    """Generates and saves the required visualizations to a specific directory."""
    
    # Set the visual style
    sns.set_theme(style="whitegrid")
    
    # ---------------------------------------------------------
    # Graph 1: Overall Differences (Histogram)
    # ---------------------------------------------------------
    # Histograms are great here because they show the distribution of scores,
    # making it easy to see the high cluster vs. the negative outliers.
    plt.figure(figsize=(10, 6))
    
    sns.histplot(
        data=df, x='Reward', hue='Model_Type', 
        kde=True, bins=40, palette='Set2', 
        alpha=0.6, element="step"
    )

    plt.title('Overall Reward Distribution: Active vs Baseline Models', fontsize=14)
    plt.ylabel('Frequency (Number of Episodes)', fontsize=12)
    plt.xlabel('Episode Reward', fontsize=12)
    
    plt.xlim(-10)
    
    plt.tight_layout()

    plt.savefig(save_dir / '1_overall_active_vs_baseline_histogram.png')
    plt.show()
    
    # ---------------------------------------------------------
    # Graph 2: Active vs Baseline Across Levels (Violin Plot)
    # ---------------------------------------------------------
    # A Violin plot combines a boxplot with a density/histogram shape.
    # Using split=True puts Active on one side and Baseline on the other!
    plt.figure(figsize=(10, 6))

    df_sorted_levels = df.sort_values('Level') 

    sns.violinplot(
        data=df_sorted_levels, x='Level', y='Reward', 
        hue='Model_Type', split=True, inner="quartile", 
        palette='Set2', cut=0 # cut=0 stops the shape from extending past actual data limits
    )

    plt.title('Reward Distribution Across Levels: Active vs Baseline', fontsize=14)
    plt.ylabel('Episode Reward', fontsize=12)
    plt.xlabel('Level', fontsize=12)
    plt.legend(title='Model Type')
    
    plt.ylim(8, 12)

    plt.tight_layout()
    plt.savefig(save_dir / '2_performance_across_levels_violin.png')
    plt.show()

    # ---------------------------------------------------------
    # Graph 3: Effect of Reductions on Active Models (Median Trend)
    # ---------------------------------------------------------
    active_df = df[(df['Model_Type'] == 'Active') & (df['Reduction'].notna())].copy()
    
    if not active_df.empty:
        plt.figure(figsize=(12, 6))
        
        active_df = active_df.sort_values(by=['Level', 'Reduction'], ascending=[True, False])
        
        # IMPORT CHANGE: Added estimator='median'.
        # The median is highly resistant to extreme negative outliers, 
        # giving you a much truer representation of typical performance.
        from numpy import median
        
        sns.pointplot(
            data=active_df, x='Reduction', y='Reward', hue='Level', 
            dodge=True, markers=['o', 's', 'D'], capsize=.1, 
            err_kws={'linewidth': 1}, estimator=median
        )
        
        plt.gca().invert_xaxis()
        
        plt.title('Effect of Percentage Reduction on Active Models (Median Reward)', fontsize=14)
        plt.ylabel('Median Episode Reward (with 95% CI)', fontsize=12)
        plt.xlabel('Percentage Reduction (%)', fontsize=12)
        plt.legend(title='Level')

        plt.tight_layout()
        plt.savefig(save_dir / '3_reduction_effects_median_trend.png')
        plt.show()

    else:
        print("No valid reduction data found in Active model filenames to plot Graph 3.")
        
        
# ---------------------------------------------------------
    # Graph 4: Time-Series Stability (Smoothed Line Plot)
    # ---------------------------------------------------------
    plt.figure(figsize=(14, 6))
    
    # We use a rolling window of 5 episodes to smooth out the jaggedness
    df['Rolling_Reward'] = df.groupby(['Model_Type', 'Level', 'Filename'])['Reward'].transform(lambda x: x.rolling(5, min_periods=1).mean())
    
    sns.lineplot(
        data=df, x='Episode', y='Rolling_Reward', 
        hue='Model_Type', style='Level', 
        errorbar=('ci', 95), linewidth=2, palette='Set2'
    )
    
    plt.title('Agent Stability Over Time (5-Episode Rolling Average)', fontsize=14)
    plt.ylabel('Smoothed Reward', fontsize=12)
    plt.xlabel('Episode Number', fontsize=12)
    plt.ylim(-10, 12) # Zooming in again to ignore the -33s!
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(save_dir / '4_time_series_stability.png')
    plt.show()

    # ---------------------------------------------------------
    # Graph 5: The "Sweet Spot" Heatmap (Active Models Only)
    # ---------------------------------------------------------
    if not active_df.empty:
        plt.figure(figsize=(10, 5))
        
        # Create a matrix of Level vs Reduction, calculating the median reward
        heatmap_data = active_df.pivot_table(
            index='Level', columns='Reduction', values='Reward', aggfunc='median'
        )
        
        # Sort columns descending (100 down to 1)
        heatmap_data = heatmap_data[sorted(heatmap_data.columns, reverse=True)]
        
        sns.heatmap(
            heatmap_data, annot=True, fmt=".2f", 
            cmap="RdYlGn", center=0, cbar_kws={'label': 'Median Reward'}
        )
        
        plt.title('Performance Heatmap: Reduction % vs Level', fontsize=14)
        plt.xlabel('Percentage Reduction (%)', fontsize=12)
        plt.ylabel('Level', fontsize=12)
        plt.tight_layout()
        plt.savefig(save_dir / '5_reduction_heatmap.png')
        plt.show()

    # ---------------------------------------------------------
    # Graph 6: Cumulative "Bank Account" Plot
    # ---------------------------------------------------------
    plt.figure(figsize=(12, 6))
    
    # Calculate cumulative sum of rewards per individual run
    df['Cumulative_Reward'] = df.groupby(['Model_Type', 'Level', 'Filename'])['Reward'].cumsum()
    
    sns.lineplot(
        data=df, x='Episode', y='Cumulative_Reward', 
        hue='Model_Type', style='Level', 
        errorbar=None, linewidth=1.5, palette='Set2', alpha=0.8
    )
    
    plt.title('Cumulative Reward Over 100 Episodes', fontsize=14)
    plt.ylabel('Total Accumulated Reward', fontsize=12)
    plt.xlabel('Episode Number', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(save_dir / '6_cumulative_rewards.png')
    plt.show()

    # ---------------------------------------------------------
    # Graph 7: Crash vs Success Ratio (Categorical Stacked Bar)
    # ---------------------------------------------------------
    # Define what a win, acceptable run, and crash look like
    def categorize_outcome(reward):
        if reward >= 8.5: return 'Success (>= 8.5)'
        elif reward >= 0: return 'Suboptimal (0 to 8.4)'
        else: return 'Crash (< 0)'
        
    df['Outcome'] = df['Reward'].apply(categorize_outcome)
    
    # Calculate percentages for the Active models
    if not active_df.empty:
        outcome_counts = df[df['Model_Type'] == 'Active'].groupby(['Reduction', 'Outcome']).size().unstack(fill_value=0)
        outcome_percentages = outcome_counts.div(outcome_counts.sum(axis=1), axis=0) * 100
        
        # Sort index so 100% is on the left
        outcome_percentages = outcome_percentages.sort_index(ascending=False)
        
        # Define colors (Green for success, Yellow for sub, Red for crash)
        colors = {'Success (>= 8.5)': '#2ca02c', 'Suboptimal (0 to 8.4)': '#ff7f0e', 'Crash (< 0)': '#d62728'}
        ordered_colors = [colors.get(col, '#333333') for col in outcome_percentages.columns]

        outcome_percentages.plot(kind='bar', stacked=True, figsize=(12, 6), color=ordered_colors, edgecolor='white')
        
        plt.title('Episode Outcomes by Reduction % (Active Models)', fontsize=14)
        plt.ylabel('Percentage of Episodes (%)', fontsize=12)
        plt.xlabel('Percentage Reduction (%)', fontsize=12)
        plt.legend(title='Episode Outcome', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig(save_dir / '7_crash_vs_success_ratio.png')
        plt.show()
        
        
    # ---------------------------------------------------------
    # Graph 8: Overall Reward by Level (Grouped Bar Chart)
    # ---------------------------------------------------------
    plt.figure(figsize=(10, 6))

    # Sort levels to ensure they appear in order (e.g., Level 1, Level 2)
    df_sorted_levels = df.sort_values('Level')

    # A bar plot automatically calculates the mean and shows error bars (95% CI)
    sns.barplot(
        data=df_sorted_levels, x='Level', y='Reward', 
        hue='Model_Type', palette='Set2', 
        capsize=.1, err_kws={'linewidth': 1}
    )

    plt.title('Average Overall Reward by Level: Active vs Baseline', fontsize=14)
    plt.ylabel('Mean Episode Reward', fontsize=12)
    plt.xlabel('Level', fontsize=12)
    plt.legend(title='Model Type')

    # Note: If the -33 outliers drag the mean bars too far down to read easily, 
    # uncomment the line below to zoom in on the positive scoring range!
    # plt.ylim(0, 11) 

    plt.tight_layout()
    plt.savefig(save_dir / '8_overall_reward_by_level_bar.png')
    plt.show()
    
    
    # ---------------------------------------------------------
    # Graph 9: Overall Reward by Level (Grouped Bar with Significance)
    # ---------------------------------------------------------
    plt.figure(figsize=(10, 6))

    df_sorted_levels = df.sort_values('Level')

    # We assign the plot to a variable 'ax' so the annotator can interact with it
    ax = sns.barplot(
        data=df_sorted_levels, x='Level', y='Reward', 
        hue='Model_Type', palette='Set2', 
        capsize=.1, err_kws={'linewidth': 1}
    )

    plt.title('Average Overall Reward by Level: Active vs Baseline', fontsize=14)
    plt.ylabel('Mean Episode Reward', fontsize=12)
    plt.xlabel('Level', fontsize=12)
    plt.legend(title='Model Type', loc='lower right')

    # Dynamically generate the pairs we want to compare (Active vs Baseline for each Level)
    levels = sorted(df['Level'].unique())
    box_pairs = [((level, 'Active'), (level, 'Baseline')) for level in levels]

    # Initialize the Annotator
    annotator = Annotator(ax, box_pairs, data=df_sorted_levels, x='Level', y='Reward', hue='Model_Type')
    
    # Configure it to use the Mann-Whitney test and format the text as stars
    annotator.configure(test='Mann-Whitney', text_format='star', loc='inside', verbose=2)
    
    # Draw the brackets!
    annotator.apply_and_annotate()

    plt.tight_layout()
    plt.savefig(save_dir / '9_overall_reward_by_level_bar_sig.png')
    plt.show()
    

def run_statistical_tests(df, save_dir):
    """Runs independent t-tests and Mann-Whitney U tests between Active and Baseline for each Level."""
    print("\n" + "="*50)
    print("STATISTICAL SIGNIFICANCE REPORT")
    print("="*50)
    
    results = []
    levels = sorted(df['Level'].unique())
    
    for level in levels:
        # Filter data for the specific level
        level_data = df[df['Level'] == level]
        
        active_rewards = level_data[level_data['Model_Type'] == 'Active']['Reward'].dropna()
        baseline_rewards = level_data[level_data['Model_Type'] == 'Baseline']['Reward'].dropna()
        
        # We need data in both groups to compare them
        if len(active_rewards) == 0 or len(baseline_rewards) == 0:
            print(f"[{level}] Skipped: Missing data for Active or Baseline models.")
            continue
            
        # 1. Welch's T-Test (Assumes normal distribution, allows unequal variance)
        t_stat, p_val_t = stats.ttest_ind(active_rewards, baseline_rewards, equal_var=False)
        
        # 2. Mann-Whitney U Test (Non-parametric, ignores extreme outlier magnitudes)
        u_stat, p_val_u = stats.mannwhitneyu(active_rewards, baseline_rewards, alternative='two-sided')
        
        # Determine if significant (Standard alpha = 0.05)
        sig_t = "Yes" if p_val_t < 0.05 else "No"
        sig_u = "Yes" if p_val_u < 0.05 else "No"
        
        # Calculate MEANS and MEDIANS for context
        mean_active = active_rewards.mean()
        mean_baseline = baseline_rewards.mean()
        median_active = active_rewards.median()
        median_baseline = baseline_rewards.median()
        
        print(f"\n--- {level} ---")
        print(f"Active   -> Mean: {mean_active:.2f} | Median: {median_active:.2f}")
        print(f"Baseline -> Mean: {mean_baseline:.2f} | Median: {median_baseline:.2f}")
        print(f"Welch's T-Test    -> p-value: {p_val_t:.4f} (Significant? {sig_t})")
        print(f"Mann-Whitney U    -> p-value: {p_val_u:.4f} (Significant? {sig_u})")
        
        # Save to list for CSV export
        results.append({
            'Level': level,
            'Active_Mean': round(mean_active, 2),
            'Baseline_Mean': round(mean_baseline, 2),
            'Active_Median': round(median_active, 2),
            'Baseline_Median': round(median_baseline, 2),
            'T_Test_P_Value': p_val_t,
            'T_Test_Significant': sig_t,
            'Mann_Whitney_P_Value': p_val_u,
            'Mann_Whitney_Significant': sig_u
        })
        
    # Export results to CSV so you have hard proof for your write-up
    if results:
        results_df = pd.DataFrame(results)
        csv_path = save_dir / 'statistical_results.csv'
        results_df.to_csv(csv_path, index=False)
        print("\n" + "="*50)
        print(f"Stats report saved to: {csv_path}")
        print("="*50 + "\n") 
        

if __name__ == "__main__":
    
    ROOT_DIR = get_proj_root()
    print(f"\n\nProject root directory: {ROOT_DIR}")

    MODEL_DATA_PATH = ROOT_DIR / "data" / "model_performance_data"
    GRAPHS_DIR = ROOT_DIR / "data" / "Graphs"
    
    GRAPHS_DIR.mkdir(parents=True, exist_ok=True)
    
    print("Loading and parsing data...")
    df = load_data(MODEL_DATA_PATH)
    
    if df.empty:
        print("No data was loaded. Please check your directory structure and file contents.")

    else:
        print(f"Successfully loaded {len(df)} episodes across {df['Filename'].nunique()} files.")
        print("Generating graphs...")
        
        generate_plots(df, GRAPHS_DIR)
        print(f"Graphs generated and saved to {GRAPHS_DIR}")
        
        run_statistical_tests(df, GRAPHS_DIR)