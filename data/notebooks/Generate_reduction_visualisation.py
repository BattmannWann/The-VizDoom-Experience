import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
from pathlib import Path

"""
This script takes in an image and applies the following reductions on it:

    {0, 1, 5, 10, 20, 40, 60, 80}
    
    i.e. Percentage of the image left.
    
    For example, with an image of size 160x120, this will produce the following:
    
    Original (100%)    : 160x120
        80%            : 128x96
        60%            : 96x72
        40%            : 64x48
        20%            : 32x24
        10%            : 16x12
        5%             : 8x6
        1%             : 1x1
        
        
    Then scales it back up to the original image size
        
"""

def get_proj_root():
    # Grab the directory the notebook is currently running in
    curr_path = Path.cwd().resolve()
    
    for parent in [curr_path] + list(curr_path.parents):
        if (parent / ".git").exists() or (parent / "requirements.txt").exists():
            return parent
            
    raise FileNotFoundError("Could not locate project root directory")


def simulate_agent_vision(image_path, reduction, squeeze = "false"):
    
    """
    Gets a centre crop of the image, reducing it by a reduction factor and scales it back up to the original image shape
    """
    
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    if squeeze != "false":
        img = cv2.resize(img, (160, 120), interpolation=cv2.INTER_AREA)
    
    height, width, _ = img.shape
    width_crop, height_crop = int(width * reduction/100), int(height * reduction/100)
    
    img_reduced_shape = f"({width_crop}x{height_crop})"

    if reduction == 0:
        return img, f"None ({img.shape[1]}x{img.shape[0]})"

    y1 = (height - height_crop) // 2
    y2 = y1 + height_crop

    x1 = (width - width_crop) // 2
    x2 = x1 + width_crop
    
    crop = img[y1:y2, x1:x2]
    crop_resized = cv2.resize(crop, (width, height), interpolation = cv2.INTER_NEAREST)
    
    return crop_resized, img_reduced_shape


def generate_visualisation(file = "Cacodemon.png", reduction_list = [0, 80, 60, 40, 20, 10, 5, 1], output_name = None, output_dir = None, squeeze = "false"):
    
    """
    Generates a visualisation of all the reductions provided in the reduction list
    """
    
    image_file = file
    reductions = reduction_list
    
    img = cv2.imread(image_file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    img_shape = f"({img.shape[1]}x{img.shape[0]})"
    
    if output_name == None:
        output_name = f"cacodemon_reduction_{img_shape}.png"
        
    if output_dir == None:
        output_dir = f"{data_dir}/visualisations/"

    fig, axes = plt.subplots(2,4, figsize=(16, 7))
    axes = axes.flatten()

    for i, r in enumerate(reductions):
        
        processed_img, reduced_img_shape = simulate_agent_vision(image_file, r, squeeze)
        axes[i].imshow(processed_img, interpolation = "nearest")
        
        axes[i].set_title(f"Reduction: {r}% {reduced_img_shape}", fontsize=16, pad = 10)
        axes[i].axis('off')

    plt.subplots_adjust(left=0.02, right=0.98, top=0.90, bottom=0.02, wspace=0.05, hspace=0.1)
    plt.savefig(f"{output_dir}/{output_name}", dpi=300, bbox_inches = "tight")
    plt.show()
    
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description = """
            \n\n
            This file is for generating visualisations based on the reductions used in the active vision model.
            The standard reductions are in the set of: {0, 80, 60, 40, 20, 10, 5, 1}, where 0 represents no reduction (i.e. 100% of the image)
              
            """,
            
            epilog = "Example: python -m Generate_reduction_visualisation")
    
    
    parser.add_argument("--file", type = str, required = False, help = "The file name/path for the image to be reduced", default = "Cacodemon.png")
    
    parser.add_argument("--reductions", type = str, required = False, 
                        help = "The list of reductions you want to apply on the image. Ensure this is a comma separated list with NO spaces. Default: 0,80,60,40,20,10,5,1",
                        default = "0,80,60,40,20,10,5,1")
    
    parser.add_argument("--output_name", type = str, required = False, 
                        help = "The name for the generated visualisation Default: cacodemon_reduction_[reduced_img_shape].png",
                        default = None)
    
    parser.add_argument("--output_dir", type = str, required = False, 
                        help = "The directory that will store the image. Default: Local (i.e. '.')",
                        default = None)
    
    parser.add_argument("--squeeze", type = str, required = False, 
                        help = "Reduces the image down to 160x120 before doing the reduction and resize. Default: false",
                        default = "false")
    
    args = parser.parse_args()
    
    
    file = args.file
    reductions_list = [int(num) for num in args.reductions.split(",")]
    
    output_name = args.output_name
    output_dir = args.output_dir
    
    proj_dir = get_proj_root()
    data_dir = proj_dir / "data"
        
    if not file or not os.path.exists(file):
        
        print(f"\n\n=== NO FILE HAS BEEN PROVIDED ===\n")
        print("Ensure that file Cacodemon.png exists OR rerun with the --file flag and a valid file \n")
        print("=================================")
        
        exit(0)
        
    if not os.path.exists(f"{data_dir}/visualisations/"):
        os.makedirs(f"{data_dir}/visualisations")
        
    generate_visualisation(file, reductions_list, output_name, output_dir, squeeze = args.squeeze)
    
    