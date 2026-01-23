# Configuration Files Folder

[Configuration files](https://vizdoom.farama.org/environments/creating_custom/) fetch and setup their corresponding WAD file. This provides the developer with the ability to preset game variables and states, such that the overhead of doing this is not carried out in training and model running Python files -- which is also more difficult to do in comparison to these files.

This folder contains all of the configuration files for the WAD map files. These files do contain the same logic for the current scenario setting under this project, however, for terms of modularity and possible future work, these have been created to accommodate accordingly. Configuration files are specific to their corresponding WAD files and as such ensure that having multiple is not redundant even in this case. 

<br>

The files found in this directory are as follows (under the naming convention `Cacodemon_Recognition_...`, copying that which has been done for their corresponding WAD file):

- ***...most_basic.cfg***: Points to `Cacodemon_Recognition_most_basic.wad`

- ***...basic.cfg***: Points to `Cacodemon_Recognition_basic.wad`

- ***...Final.cfg***: Points to `Cacodemon_Recognition_Final.wad`


How to calculate it -> using this formula:
$$\text{Tics} = \text{Seconds} \times 35$$


```
=======================================
|Desired Time  | Config Value (Tics)  |
=======================================
|30 Seconds    |  1050                |
|60 Seconds    |  2100 (Recommended)  |
|2 Minutes     |  4200                |
|5 Minutes     |  10500 (Too long)    |
=======================================
```