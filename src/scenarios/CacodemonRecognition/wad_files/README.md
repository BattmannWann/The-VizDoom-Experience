# WAD Files Folder

[WAD files](link_here) are the type of file used by DOOM for mapping. These contain all information about the map and its contents, along with [ACS Scripting Files](link_here) for extra map manipulation. 


>***Important Side Note***: To recap, for all scenarios, there are levels of 'difficulty' in which the agents are trained on. Below details how the maps are structured to accommodate for this.

<br>

This folder contains the following WAD files (all begin with Cacodemon_Recognition_...):

- ***...most_basic.wad***: This is the most basic map for the Cacodemon Recognition training scenario. The map features 2 Cacodemons and very simple sector mapping images (different mapping for the floor, ceiling, and walls). The resources for this map consist of the `gzdoom.pk3` and `DOOM2.wad` files.

- ***...basic.wad***: This is a little more advanced map for the Cacodemon Recognition scenario, featuring 3 additional enemies called 'Lost Souls' and some additional environmental clutter through green torches placed throughout the map. This adds difficulty for the agent, by obscuring the goal of killing the Cacodemons through distractors. The resources for this map consist of the `gzdoom.pk3` and `DOOM2.wad` files.

- ***...Final.wad***: This is the most advanced map, featuring several types of enemy (Cacodemon, Lost Soul, Cyber Demon, Pain Elemental, and Former Human) along side the visual clutter from the torches. This is to really hone in on the agent's ability to search and recognise the Cacodemon. The resources for this map consist of the `gzdoom.pk3`, `DOOM2.wad`, and `Pain_Elemental_Mod.pk3` files. The mod file contains special characteristics for the `Pain Elemental` "DOOM thing" such that when it dies, it does not behave as normal (stopped it from spawning Lost Souls on death which would otherwise attack the player).

<br>

- **.dbs files**: These store data by default on the WAD files. Understanding of manipulating these is *NOT* required; except for the interpreter that runs them. If not available, then they are usually automatically created. 

<br><br>


## Future Considerations

- **Difficulty**: In the current WAD files, enemies are dormant, non-hostile, and die with one bullet shot by the agent (i.e. have 1 Health Point - HP). Difficulty, therefore, could be increased by several factors, and the agent trained to accommodate these and become more robust. As this project has limited time, the current configurations suffice for the experiments required. 

- **Pain Elemental Mod**: Instead of removing the lost souls being spawned, the mod could change the behaviour of the enemies spawned to be in line with the presets for the other enemies (e.g. for these configurations, enemies are non-hostile, dormant, and have 1 HP) - ***VERY DIFFICULT TASK***. Another possibility would be to add a "Dead Pain Elemental" thing which takes the place of the Pain Elemental when it dies, showcasing a carcass on the ground like other enemies - requires sprite creations and ACS scripting which is also a difficult and time-consuming task. These have not been implemented due to the time constraints of the current project, and because they are not entirely pertinent under the given constraints of the scenario nonetheless. 



