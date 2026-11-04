"""Inspect dataset directory structure and report contents.

This script scans a specified dataset directory, lists subdirectories,
and reports counts of identifiable image and annotation candidate files.
It makes no assumptions about specific annotation formats prior to actual inspection.
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set

# Recognizable file extension sets
IMAGE_EXTENSIONS: Set[str] = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}
ANNOTATION_EXTENSIONS: Set[str] = {".json", ".xml", ".txt", ".csv", ".yaml", ".yml"}


def format_size(size_bytes: int) -> str:
    """Format byte size into human-readable representation."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


def scan_directory(
    target_dir: Path,
    max_depth: int = 3,
) -> Dict[str, object]:
    """Scan directory hierarchy and count images, annotations, and other files.

    Args:
        target_dir: Directory path to inspect.
        max_depth: Maximum recursion depth for tree inspection.

    Returns:
        Dictionary containing directory structure summary and file counts.
    """
    summary: Dict[str, object] = {
        "root": str(target_dir),
        "total_files": 0,
        "image_count": 0,
        "annotation_candidates": [],
        "directories": [],
        "subfolder_counts": {},
    }

    if not target_dir.exists():
        raise FileNotFoundError(f"Path does not exist: {target_dir}")

    if not target_dir.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {target_dir}")

    annotation_files: List[Dict[str, str]] = []
    subfolder_stats: Dict[str, Dict[str, int]] = {}

    for item in sorted(target_dir.rglob("*")):
        # Skip hidden files and directories (e.g., .gitkeep, .DS_Store)
        if any(part.startswith(".") for part in item.relative_to(target_dir).parts):
            continue

        # Calculate relative depth to honor max_depth limit for structural summary
        rel_path = item.relative_to(target_dir)
        depth = len(rel_path.parts)

        if item.is_dir():
            if depth <= max_depth:
                summary["directories"].append(str(rel_path))
            continue

        if item.is_file():
            summary["total_files"] += 1
            top_folder = rel_path.parts[0] if len(rel_path.parts) > 1 else "."

            if top_folder not in subfolder_stats:
                subfolder_stats[top_folder] = {"images": 0, "annotations": 0, "others": 0}

            ext = item.suffix.lower()
            if ext in IMAGE_EXTENSIONS:
                summary["image_count"] += 1
                subfolder_stats[top_folder]["images"] += 1
            elif ext in ANNOTATION_EXTENSIONS:
                subfolder_stats[top_folder]["annotations"] += 1
                annotation_files.append({
                    "path": str(rel_path),
                    "size": format_size(item.stat().st_size),
                    "extension": ext,
                })
            else:
                subfolder_stats[top_folder]["others"] += 1

    summary["annotation_candidates"] = annotation_files
    summary["subfolder_counts"] = subfolder_stats
    return summary


def print_inspection_report(summary: Dict[str, object]) -> None:
    """Print a clean CLI summary of the inspection results."""
    print("=" * 70)
    print("DATASET INSPECTION REPORT")
    print("=" * 70)
    print(f"Target Directory : {summary['root']}")
    print(f"Total Files      : {summary['total_files']}")
    print(f"Image Files      : {summary['image_count']}")
    print(f"Candidate Annot. : {len(summary['annotation_candidates'])}")
    print("-" * 70)

    directories = summary.get("directories", [])
    if directories:
        print(f"Identified Subdirectories ({len(directories)}):")
        for d in directories:
            print(f"  └── {d}")
    else:
        print("Identified Subdirectories: None (flat directory or empty)")

    print("-" * 70)
    subfolder_counts = summary.get("subfolder_counts", {})
    if subfolder_counts:
        print("Summary by Top-level Folder:")
        for folder, counts in subfolder_counts.items():
            print(f"  • {folder}/ -> {counts['images']} images, {counts['annotations']} potential annotations, {counts['others']} others")
    else:
        print("No files found in directory.")

    print("-" * 70)
    annotations = summary.get("annotation_candidates", [])
    if annotations:
        print("Candidate Annotation Files Found:")
        for ann in annotations:
            print(f"  • {ann['path']} ({ann['size']}) [{ann['extension']}]")
        print("\nNote: Please inspect the content of these candidate files to identify the exact format (e.g. COCO, YOLO, VOC) before implementing parsers.")
    else:
        print("Candidate Annotation Files Found: None")

    print("=" * 70)


def main(argv: Optional[List[str]] = None) -> int:
    """Main command-line entrypoint."""
    parser = argparse.ArgumentParser(
        description="Inspect dataset directory layout and report image/annotation file counts."
    )
    parser.add_argument(
        "dataset_dir",
        type=str,
        nargs="?",
        default="data/seadronessee",
        help="Path to the dataset directory to inspect (default: data/seadronessee)",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=3,
        help="Maximum folder depth to display in directory structure listing (default: 3)",
    )

    args = parser.parse_args(argv)
    target_path = Path(args.dataset_dir)

    try:
        report = scan_directory(target_path, max_depth=args.max_depth)
        print_inspection_report(report)
        return 0
    except (FileNotFoundError, NotADirectoryError) as err:
        print(f"Error: {err}", file=sys.stderr)
        print(
            "\nPlease ensure you have obtained the SeaDronesSee dataset and placed it "
            f"under '{target_path}', or provide the correct path via CLI arguments.",
            file=sys.stderr,
        )
        return 1
    except Exception as err:
        print(f"Unexpected error while scanning directory: {err}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
