# Educational Notebooks

This directory contains interactive Jupyter notebooks designed to step through each phase of the aerial search-and-rescue vision pipeline.

## Planned Notebook Sequence

The educational walkthrough will be structured across five sequential notebooks:

| Step | Notebook | Description |
| :--- | :--- | :--- |
| **01** | `01_dataset_exploration.ipynb` | Inspecting aerial maritime imagery (SeaDronesSee format), exploring bounding box annotations, visualizing small-target challenges, and analyzing resolution implications. |
| **02** | `02_swimmer_detection.ipynb` | Loading a baseline detector, running frame-level inference on aerial imagery, tuning confidence and NMS thresholds, and evaluating detection performance. |
| **03** | `03_multiobject_tracking.ipynb` | Integrating association algorithms (e.g., ByteTrack), managing track births/deaths, handling intermittent wave occlusions, and visualizing target trajectories. |
| **04** | `04_temporal_distress_analysis.ipynb` | Extracting trajectory kinematics and temporal crop windows, defining distress criteria, and classifying behavior across temporal sliding windows. |
| **05** | `05_end_to_end_pipeline.ipynb` | Integrating all three stages into an end-to-end video processing pipeline producing annotated visual outputs and structured alert data. |

> **Status:** Notebooks will be added progressively as corresponding core modules are developed.

