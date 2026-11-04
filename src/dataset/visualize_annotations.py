"""Visualize annotations on SeaDronesSee imagery.

TODO: This module will be implemented after inspecting the actual annotation format
of the SeaDronesSee dataset (e.g. COCO-compliant JSON, YOLO text format, or custom structure).
Do not assume or invent an annotation schema until the downloaded dataset files
have been inspected using `inspect_dataset.py`.
"""

from pathlib import Path
from typing import Optional


def visualize_sample(
    image_path: Path,
    annotation_path: Path,
    output_path: Optional[Path] = None,
) -> None:
    """Overlay bounding boxes and class labels on an aerial image.

    Args:
        image_path: Path to the target image file.
        annotation_path: Path to the corresponding annotation file or metadata entry.
        output_path: Optional destination path to save the visualized image.

    Raises:
        NotImplementedError: Implementation is deferred until the ground truth
            annotation schema is verified against the real dataset.
    """
    raise NotImplementedError(
        "Annotation visualization cannot be executed until the ground-truth format "
        "is confirmed. Inspect candidate annotation files in 'data/seadronessee' first."
    )

