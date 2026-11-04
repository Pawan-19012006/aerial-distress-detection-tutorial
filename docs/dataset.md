# Dataset Reference: SeaDronesSee

This tutorial centers on aerial maritime computer vision using benchmarks representative of real-world search-and-rescue operations, specifically the **SeaDronesSee** dataset family.

---

## About SeaDronesSee

**SeaDronesSee** is a large-scale aerial maritime benchmark collection developed to advance object detection, tracking, and segmentation for autonomous aerial search-and-rescue missions.

### Key Characteristics
- **Sensor Modality:** High-resolution RGB imagery captured from low-to-medium altitude unmanned aerial systems (UAS).
- **Target Classes:** Swimmers, persons in water, life jackets, life vests, life rafts, boats, and other maritime objects.
- **Environmental Diversity:** Captured across diverse water bodies, illumination levels, sea states, wave patterns, glint angles, and flight altitudes.
- **Sub-benchmarks:**
  - *SeaDronesSee Object Detection*: Frame-level detection of small maritime targets.
  - *SeaDronesSee Multi-Object Tracking (MOT)*: Video sequences annotated with continuous identities across frames.

---

## Obtaining the Dataset

> **Important:** This repository does not distribute, host, or mirror any portion of the SeaDronesSee dataset.

Users must obtain the dataset directly through official distribution channels:
1. Visit the official project repository and download portal:
   - Official website: [https://seadronessee.cs.uni-tuebingen.de/](https://seadronessee.cs.uni-tuebingen.de/)
   - Benchmark challenges and papers: Search for "SeaDronesSee: A Maritime Benchmark for Detecting Humans in Open Water".
2. Review and comply with the original terms of use, licensing agreements, and citation requirements specified by the dataset authors before using the data in any academic or commercial context.

---

## Expected Local Directory Organization

Once acquired, dataset files should be organized outside version control. The recommended directory structure for subsequent tutorial exercises is:

```text
data/
├── seadronessee/
│   ├── annotations/
│   │   ├── instances_train.json
│   │   └── instances_val.json
│   └── images/
│       ├── train/
│       └── val/
└── sample/
    └── README.md
```

Detailed instructions on loading annotations and preparing training or validation splits will be provided in upcoming educational notebook modules.

