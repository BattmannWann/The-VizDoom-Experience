# Plan for 4th year Project

* PROJECT TITLE - A ViZDoom Visual Learning Environment
* COMPLETED BY - Rhys Oliver Anthony Stewart
* STUDENT ID - 2682261s
* SUPERVISOR NAME - Dr. Jan Paul Siebert

---

The following is a week-by-week plan for the whole project, that will be updated during project completion. This will include appropriate information on where to find/see any progress and whether or not the actions have been completed or postponed to a following week.

`NOTE: Any notes that have been taken will be featured under the repository` [wiki](https://github.com/BattmannWann/The-VizDoom-Experience/wiki)

See the following:

## Winter semester

* **Week 1**:
    1. Break the project description down into actionable steps - ***COMPLETED***

    2. research papers that have been published that have used ViZDoom, and evaluate what hasn't been done yet, or that which can be improved on/further proven. Ensure to take notes of any important concepts and technologies identified while reading, and keep a record of any sources with an appropriate reference manager (e.g. Zotero)
    
    3. Research additional APIs similar to ViZDoom and solidify project directions; i.e. decide if using ViZDoom, finish project plan - ***COMPLETED***
    
    4. Create a project repository on GitHub, using the provided template. Ensure to add supervisor to the repository. - ***COMPLETED***

    5. Attend meeting with supervisor, take meeting minutes, and get questions answered. ***COMPLETED***

    6. Research how to implement and use any concepts identified in the notes. ***COMPLETED***

    7. Begin project dissertation - using overleaf. ***COMPLETED***


* **Week 2: Baseline Model Scaffolding**
    * **Tasks:** 

        1. Install ViZDoom and all required libraries (PyTorch, etc.). Run the provided example scenarios to ensure the environment is working correctly. Familiarize yourself with the ViZDoom API (state/action spaces, rewards). ***COMPLETED***

        2. Implement the basic skeleton of the CNN in PyTorch. Write the code to take a ViZDoom screen buffer (frame) as input and produce a forward pass with action logits as output. ***COMPLETED***

    * **Deliverables:** 
        - A fully functional development environment.
        - A script that can load a ViZDoom frame and process it through the baseline CNN model.

* **Week 3: Scenario Design & Metrics**

    * **Tasks:** Design a focused evaluation scenario (e.g., the motion interception task). Create the map (`.wad` file) and the configuration (`.cfg` file) in ViZDoom. Formally define the metrics that will be used to measure success (e.g., interception rate, reaction time).

    * **Deliverable:** A complete, runnable ViZDoom scenario file and a document defining evaluation metrics.

* **Week 4: Agent Implementation & Logging**

    * **Tasks:** Implement a simple reinforcement learning agent (e.g., Deep Q-Network). Integrate the baseline CNN into this agent. Set up a robust logging framework (e.g., using `wandb` or `TensorBoard`) and a method for saving configuration files to ensure reproducibility.

    * **Deliverable:** A trainable RL agent that can take actions in the custom scenario.

* **Week 5: Initial Baseline Training**

    * **Tasks:** Begin the first training runs of the baseline agent in the custom ViZDoom scenario. The goal here is not to achieve perfect performance, but to debug the training loop and ensure the agent is learning. Determine a suitable episodal iteration for the agent (i.e. run for thousands or hundreds of episodes?). 

    * **Deliverable:** The agent successfully runs for several episodes without crashing; initial learning curves are logged.

* **Week 6: Full Baseline Training Run**

    * **Tasks:** Conduct the full training run for the baseline ViZDoom agent across multiple random seeds to ensure results are robust.

    * **Deliverable:** A set of trained model weights for the baseline agent.

* **Week 7: Baseline Evaluation in ViZDoom**

    * **Tasks:** Evaluate the trained baseline agent. Run it in evaluation mode (no learning) for a large number of episodes and log the performance metrics defined in Week 3.
    * **Deliverable:** A table of results showing the baseline agent's performance in your ViZDoom scenario.

* **Week 8: ImageNet Baseline Setup**

    * **Tasks:** Prepare the comparative benchmark. Set up the data pipeline for a subset of ImageNet. Adapt the baseline CNN to perform classification and load a pretrained model for fine-tuning.

    * **Deliverable:** A working script that can train/validate the baseline CNN on ImageNet.

* **Week 9: ImageNet Baseline Training & Evaluation**

    * **Tasks:** Fine-tune and evaluate the baseline CNN on the ImageNet subset.
    * **Deliverable:** A table of results showing the baseline model's top-1 and top-5 accuracy on ImageNet.

* **Week 10: Implement Innovation (Attention Module)**

    * **Tasks:** Code the chosen innovation (e.g., a CBAM attention module) and integrate it into the CNN architecture. Verify the model's forward pass and check that all tensor shapes are correct.

    * **Deliverable:** A new "Attention-CNN" model that is ready for training.

* **Week 11 [PROJECT WEEK]: Innovation Integration & Mid-Project Consolidation**

    * **Tasks:** Integrate the new Attention-CNN into both the ViZDoom RL agent and ImageNet classification script. Consolidate all baseline results and draft the methodology section for your status report.

    * **Deliverable:** All code is ready for the main experimental runs.

* **Week 12 [PROJECT WEEK]: Analysis & Reporting**
    * **Tasks:** Write and submit the mid-project status report. This report should detail motivation, the custom scenario designed, the baseline agent's architecture, and the complete set of baseline performance data from both ViZDoom and ImageNet.

    * **Deliverable:** **Status report submitted.**

---

### Winter Break

Try to finish off development and ensure any missing requirements are fulfilled. 
---

### Spring Semester

* **Week 13: Train Attention Agent in ViZDoom (Part 1)**

    * **Tasks:** Begin the full training runs for the new Attention-CNN agent in the ViZDoom scenario across multiple seeds.

    * **Deliverable:** Training runs initiated and logged.

* **Week 14: Train Attention Agent in ViZDoom (Part 2)**

    * **Tasks:** Complete the ViZDoom training runs and evaluate the final attention-based agent.
    * **Deliverable:** A complete set of performance data for the attention agent in ViZDoom.

* **Week 15: Train Attention Agent on ImageNet**

    * **Tasks:** Train and evaluate the Attention-CNN on the ImageNet subset.
    * **Deliverable:** A complete set of performance data for the attention model on ImageNet.

* **Week 16: Comparative Analysis**

    * **Tasks:** Place the results from all four experiments (Baseline/ViZDoom, Attention/ViZDoom, Baseline/ImageNet, Attention/ImageNet) side-by-side. Calculate the performance gains for each.

    * **Deliverable:** A summary table comparing the performance of both models across both benchmarks.

* **Week 17: Statistical Testing**

    * **Tasks:** Run statistical tests (e.g., independent t-tests) to determine if the performance difference between the baseline and attention agents is statistically significant in the ViZDoom environment.

    * **Deliverable:** p-values and a conclusion on the significance of your results.

* **Week 18: Visualization of Results**

    * **Tasks:** Create the core figures for the dissertation: bar charts comparing performance, learning curves, and qualitative visualizations (e.g., heatmaps of agent behavior or attention maps).

    * **Deliverable:** A set of high-quality, report-ready plots.

* **Week 19: Optional Extension or Writing Buffer**

    * **Tasks:** If time permits, begin experimenting with a second innovation. If not, use this week as a buffer and start drafting the Experiments and Results sections of your dissertation.

    * **Deliverable:** Extra experimental data or a partial draft of the results chapter.

* **Week 20: Dissertation Writing: Methodology & Results**

    * **Tasks:** Write a full draft of the Methodology and Results chapters. Integrate tables and plots.
    * **Deliverable:** A solid draft of the core technical sections.

* **Week 21: Dissertation Writing: Introduction & Discussion**

    * **Tasks:** Write the Introduction, Literature Review, and Discussion sections. In the discussion, analyse *why* ViZDoom was more sensitive to the innovation(s) than ImageNet.

    * **Deliverable:** A complete first draft of the entire dissertation.

* **Week 22: Review and Refine**

    * **Tasks:** Read through full draft. Refine your arguments, improve clarity, and check for consistency. Share the draft with the supervisor for feedback.

    * **Deliverable:** A revised draft incorporating feedback.

* **Week 23 [TERM ENDS]: Final Edits & Bibliography**

    * **Tasks:** Finalise all edits based on feedback. Format the bibliography (e.g., using BibTeX), and proofread the entire document carefully.

    * **Deliverable:** A submission-ready dissertation draft.

* **Week 24: Final Submission & Presentation Prep**

    * **Tasks:** Perform a final proofread. Submit the dissertation. Prepare presentation slides for the presentation.
    
    * **Deliverable:** **Dissertation submitted and presentation ready.** 
