"""Dataset statistics computation module.

TODO: This module will compute ground-truth dataset distributions (class frequencies,
bounding box area distributions, image resolution ranges, aspect ratios) once the
real SeaDronesSee annotations are confirmed and parsed.
No synthetic or fabricated statistics should be produced here.
"""

from pathlib import Path
from typing import Dict, Any


def compute_dataset_statistics(dataset_dir: Path) -> Dict[str, Any]:
    """Compute empirical statistics across dataset splits.

    Args:
        dataset_dir: Root path to the verified SeaDronesSee dataset.

    Returns:
        Dictionary containing verified metrics such as class distribution,
        bounding box scales, and split counts.

    Raises:
        NotImplementedError: Implementation is deferred until actual annotation
            schema is verified from downloaded dataset files.
    """
    raise NotImplementedError(
        "Dataset statistics computation requires parsing real annotations. "
        "Inspect the downloaded dataset structure and annotations before computing metrics."
    )

