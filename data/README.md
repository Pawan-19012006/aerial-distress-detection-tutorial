# Data Directory

This directory is designated for datasets and local testing media used throughout the tutorial.

## Directory Structure

```text
data/
├── README.md       # Dataset and storage guidelines
└── sample/         # Permitted local video clips and test images (not tracked by Git)
```

## Guidelines

- **Raw Datasets:** Full benchmark datasets (such as SeaDronesSee) must **not** be stored directly inside version control. Refer to [`docs/dataset.md`](../docs/dataset.md) for details on dataset acquisition, directory structure, and licensing terms.
- **Sample Media:** Place small, permitted test clips or sample frames into `data/sample/`. These can be used for quick pipeline testing and visual debugging.
- **Git Tracking:** All contents under `data/` (except documentation and placeholder markers) are ignored by `.gitignore` to prevent accidental commits of large video files and third-party data assets.

