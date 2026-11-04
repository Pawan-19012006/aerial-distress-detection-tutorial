# Data Directory

This directory is designated for datasets and local testing media used throughout the tutorial.

## Dataset Acquisition

The dataset used in this tutorial is **SeaDronesSee** (specifically the Object Detection v2 track).

- **Official Source:** [https://seadronessee.cs.uni-tuebingen.de/](https://seadronessee.cs.uni-tuebingen.de/)
- **Download Instructions:** Visit the official portal, register/request access according to their guidelines, and download the dataset archive.
- **Placement:** Extract the downloaded dataset contents directly into `data/seadronessee/`.
- **License and Terms:** SeaDronesSee is provided by its respective authors under its own research/usage terms. Check the official dataset license and citation requirements before use or redistribution.

## Directory Structure

```text
data/
├── README.md              # Dataset guidance and instructions
├── sample/                # Directory for local sample clips/frames
└── seadronessee/          # Place extracted SeaDronesSee dataset here
    └── .gitkeep
```

## Important Warnings

- **Do NOT commit dataset files to Git:** Raw imagery and annotation archives are excluded via `.gitignore`. Committing large image sets bloats repository size and may violate dataset redistribution licenses.
- Keep all local dataset downloads inside `data/seadronessee/` or specify an external path when running tools.
