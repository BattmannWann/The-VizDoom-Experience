# WAD Files Folder

[WAD files](https://vizdoom.farama.org/environments/creating_custom/) are the type of file used by DOOM for mapping. These contain all information about the map and its contents, along with [ACS Scripting Files](https://zdoom.org/wiki/ACS) for extra map manipulation. To access any ACS scripts, the WAD file MUST be opened in an editor, otherwise, there is no other way to view the ACS scripts.


>***Important Side Note***: To recap, for all scenarios, there are levels of 'difficulty' in which the agents are trained on. Below details how the maps are structured to accommodate for this.

<br>

This folder contains the following WAD files (all begin with Cacodemon_Recognition_...):

- ***...most_basic.wad***: This is the most basic map for the Cacodemon Recognition training scenario. The map features 2 Cacodemons and very simple sector mapping images (different mapping for the floor, ceiling, and walls). The resources for this map consist of the `gzdoom.pk3` and `DOOM2.wad` files.

- ***...basic.wad***: This is a little more advanced map for the Cacodemon Recognition scenario, featuring 3 additional enemies called 'Lost Souls' and some additional environmental clutter through green torches placed throughout the map. This adds difficulty for the agent, by obscuring the goal of killing the Cacodemons through distractors. The resources for this map consist of the `gzdoom.pk3` and `DOOM2.wad` files.

- ***...Final.wad***: This is the most advanced map, featuring several types of enemy (Cacodemon, Lost Soul, Cyber Demon, Pain Elemental, and Former Human) along side the visual clutter from the torches. This is to really hone in on the agent's ability to search and recognise the Cacodemon. The resources for this map consist of the `gzdoom.pk3`, `DOOM2.wad`, and `Pain_Elemental_Mod.pk3` files. The mod file contains special characteristics for the `Pain Elemental` "DOOM thing" such that when it dies, it does not behave as normal (stopped it from spawning Lost Souls on death which would otherwise attack the player).

<br>

- **.dbs**: These store data by default on the WAD files. Understanding of manipulating these is *NOT* required; except for the interpreter that runs them. If not available, then they are usually automatically created. 

- **.backup...**: These are automatically created files as a result of using UltimateDoomBuilder. These can be deleted and ignored if not already.


---

### ACS_Scripts folder

- **.acs**: Normally, these can only be viewed and accessed on opening a WAD file in a map maker/viewer programme, however, these have been included here such that specific functionalities can be determined nonetheless. 

    These dictate specific thing behaviours and map functionalities for:

    - Spawning enemies randomly
    - Setting enemy characteristics (1 health points, dormant, unable to move, "thing special" which points to a function to provide +ve/-ve rewards accordingly)
    - Negative rewards for shooting the gun
    - Negative rewards for killing the incorrect enemy type
    - Positive rewards for killing the correct enemy type
    - How the episode finishes; specified enemy in question needs to have been killed (for this scenario, all Cacodemons must be killed)

    The scripts have been written in a way to promote modularity, such that they can be reused and little work needs to be done to change their function(s). 

---

<br><br>


## Future Considerations

- **Difficulty**: In the current WAD files, enemies are dormant, non-hostile, and die with one bullet shot by the agent (i.e. have 1 Health Point - HP). Difficulty, therefore, could be increased by several factors, and the agent trained to accommodate these and become more robust. As this project has limited time, the current configurations suffice for the experiments required. 

- **Pain Elemental Mod**: Instead of removing the lost souls being spawned, the mod could change the behaviour of the enemies spawned to be in line with the presets for the other enemies (e.g. for these configurations, enemies are non-hostile, dormant, and have 1 HP) - ***VERY DIFFICULT TASK***. Another possibility would be to add a "Dead Pain Elemental" thing which takes the place of the Pain Elemental when it dies, showcasing a carcass on the ground like other enemies - requires sprite creations and ACS scripting which is also a difficult and time-consuming task. These have not been implemented due to the time constraints of the current project, and because they are not entirely pertinent under the given constraints of the scenario nonetheless. 



