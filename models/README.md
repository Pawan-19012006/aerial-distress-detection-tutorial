# Models Directory

This directory is the local destination for trained model checkpoints, weights files, and exported inference engines.

## Storage Conventions

Place downloaded or trained model weights into this directory according to stage:
```text
models/
├── README.md
├── swimmer_detector.pt       # PyTorch checkpoint for swimmer detection
├── swimmer_detector.onnx     # Intermediate ONNX export
├── swimmer_detector.engine   # Serialized TensorRT engine (edge deployment)
└── distress_classifier.pt    # Temporal distress analysis checkpoint
```

## Why Weights Are Not Committed to Git

Binary model weights (e.g., `.pt`, `.onnx`, `.engine`) typically range from tens of megabytes to several gigabytes. Committing large binary files directly to a Git repository:
- Bloats repository clone and fetch times for all contributors.
- Causes Git history to expand irreversibly since Git stores full binary snapshots on changes.
- Violates GitHub's file size limits (100 MB hard limit per file).

All binary weight formats in this directory are excluded via `.gitignore`. External release tags, dedicated model hubs, or cloud storage links will be provided for accessing pre-trained checkpoints as modules are released.

