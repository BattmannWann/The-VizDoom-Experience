import cv2
import matplotlib.pyplot as plt
import os
import math
import argparse
from pathlib import Path


def get_proj_root():
    # Grab the directory the notebook is currently running in
    curr_path = Path.cwd().resolve()
    
    for parent in [curr_path] + list(curr_path.parents):
        if (parent / ".git").exists() or (parent / "requirements.txt").exists():
            return parent
            
    raise FileNotFoundError("Could not locate project root directory")


def get_frames_from_dir(dir):
    
    files_list = []
    
    for filepath in dir.rglob('*'):
        
        if ".png" in str(filepath):
           files_list.append(str(filepath))
           
    return files_list


import cv2
import matplotlib.pyplot as plt
import os
import math

def generate_grid_visualisation(frame_list, titles=None, max_cols=3, output_name="tight_sequence_grid.png", output_dir="visualisations/"):
    """
    Generates a tightly packed grid visualisation of a sequence of frames, 
    dynamically scaling the figure size to eliminate whitespace.
    """
    num_frames = len(frame_list)
    if num_frames == 0:
        print("Error: No frames provided.")
        return
        
    cols = min(max_cols, num_frames)
    rows = math.ceil(num_frames / cols)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    first_img = cv2.imread(frame_list[0])
    img_height, img_width = first_img.shape[:2]
    aspect_ratio = img_height / img_width
    
    
    base_width = 4 
    figsize = (base_width * cols, (base_width * aspect_ratio * rows) + (0.3 * rows))
    # -------------------------------------------------------

    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    
    if num_frames == 1:
        axes = [axes]
        
    elif rows == 1 or cols == 1:
        axes = axes.flatten()
        
    else:
        axes = axes.flatten()

    for i in range(len(axes)):
        
        if i < num_frames:
            img = cv2.imread(frame_list[i])
            
            if img is not None:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                axes[i].imshow(img, interpolation="nearest", aspect="equal")
            
            
            if titles and i < len(titles):
                axes[i].set_title(titles[i], fontsize=14, pad=4)
                
            else:
                axes[i].set_title(f"Frame {i+1}", fontsize=14, pad=4)
        
        
        axes[i].axis('off')

    
    plt.subplots_adjust(left=0.01, right=0.99, top=0.95, bottom=0.01, wspace=0.02, hspace=0.15)
    
    save_path = os.path.join(output_dir, output_name)
    # bbox_inches="tight" ensures the final crop trims away any outer canvas margins
    plt.savefig(save_path, dpi=300, bbox_inches="tight", pad_inches=0.02, transparent=False)
    print(f"Successfully saved tight grid to: {save_path}")
    
    plt.show()
    
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description = """
            \n\n
            This file is for generating visualisations based on frames taken from model evaluations.
            
            You MUST enter the --dir flag to point the script to the directory that you want to create
            the visualisation from.
              
            """,
            
            epilog = "Example: python -m Create_Grid_Visualisation_from_frames ")
    
    
    parser.add_argument("--dir", type = str, required = True, help = "The directory/path for the images to be obtained from")
    
    parser.add_argument("--output_name", type = str, required = False, 
                        help = "The name for the generated visualisation Default: cacodemon_reduction_[reduced_img_shape].png",
                        default = None)
    
    parser.add_argument("--output_dir", type = str, required = False, 
                        help = "The directory that will store the image. Default: Local (i.e. '.')",
                        default = None)
    
    args = parser.parse_args()
    

    proj_root = get_proj_root()
    proj_root_path = Path(proj_root)
    
    dir = Path(args.dir)
    proj_output_dir = proj_root_path / "data" / "visualisations" / "model_evals"
    
    output_name = args.output_name if args.output_name != None else "Model_Eval_Showcase.png"
    output_dir = args.output_dir if args.output_dir != None else proj_output_dir
    
    proj_dir = get_proj_root()
    data_dir = proj_dir / "data"
        
    if not dir or not os.path.exists(dir):
        
        print(f"\n\n=== NO DIRECTORY HAS BEEN PROVIDED ===\n")
        print("Ensure that the directory exists and has been provided \n")
        print("=================================")
        
        exit(0)
        
    if not os.path.exists(f"{data_dir}/visualisations/"):
        os.makedirs(f"{data_dir}/visualisations")
        
        
    frames = get_frames_from_dir(dir)
    generate_grid_visualisation(frame_list = frames, output_name = output_name, output_dir = output_dir)
    