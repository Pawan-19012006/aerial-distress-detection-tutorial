# Pipeline Architecture

This document describes the high-level system architecture of the aerial search-and-rescue (SAR) computer vision pipeline demonstrated in this tutorial.

---

## High-Level Pipeline Flow

The vision pipeline processes raw airborne video streams through a multi-stage sequential architecture:

```
┌─────────────────┐
│  Video Frames   │ (UAV downlink / Recorded video stream)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Swimmer         │ Frame-level localization & classification
│ Detection       │ Input: Frame image (H, W, C)
└────────┬────────┘ Output: Bounding boxes [x1, y1, x2, y2], scores, class IDs
         │
         ▼
┌─────────────────┐
│ Multi-Object    │ Inter-frame identity association & trajectory filtering
│ Tracking (MOT)  │ Input: Detections + motion model (Kalman filter)
└────────┬────────┘ Output: Persistent Track IDs + historical bounding box trajectories
         │
         ▼
┌─────────────────┐
│ Temporal        │ Behavior & movement pattern analysis over sliding windows
│ Distress        │ Input: Track history (positions, appearance crops, kinematics)
│ Analysis        │ Output: Distress probability score & behavioral category
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Structured      │ Coordinates, track history, distress levels, alert triggers
│ Outputs         │ Output formats: JSON logs, annotated video frames, geospatial alerts
└─────────────────┘
```

---

## Pipeline Stages

### 1. Video Frames Ingestion
- **Input:** Video stream or sequential frame directory captured from a downward-looking or oblique UAV camera.
- **Challenges:** Platform vibration, altitude changes, variable illumination, wave glint, and high camera velocity relative to the water surface.

### 2. Swimmer Detection
- **Purpose:** Localize candidate persons and swimmers within each isolated frame.
- **Design Considerations:**
  - Swimmers in open water typically occupy a minute percentage of the total frame pixels (often < 20x20 pixels at high flight altitudes).
  - High resolution inference (e.g., 1280x1280) or tiled slicing techniques are common strategies to preserve small-object spatial features.
- **Contract:** Produces spatial bounding boxes, confidence scores, and class labels for each frame.

### 3. Multi-Object Tracking (MOT)
- **Purpose:** Associate detections across frames to build persistent trajectories for each individual.
- **Design Considerations:**
  - Standard appearance-based re-identification is often unreliable in marine environments due to uniform wetsuits, sea spray, and low pixel counts.
  - Motion modeling (e.g., Kalman filters tailored for camera ego-motion plus oceanic drift) and spatial IoU association (such as ByteTrack or OC-SORT) are utilized to link tracks through brief occlusions caused by cresting waves.
- **Contract:** Assigns a consistent `track_id` to each individual and maintains a bounded temporal trajectory buffer.

### 4. Temporal Distress Analysis
- **Purpose:** Evaluate whether a tracked individual exhibits signs of distress versus normal swimming or floating.
- **Design Considerations:**
  - A single static frame rarely contains sufficient information to distinguish distress; behavioral state is inherently temporal.
  - Trajectory kinematics (displacement variance, erratic velocity spikes) and localized patch appearance dynamics over a sliding temporal window (e.g., 32–64 frames) provide signal for distress classification.
- **Contract:** Outputs a distress confidence score and state classification per active track.

### 5. Structured Outputs
- **Purpose:** Translate computer vision predictions into actionable search-and-rescue telemetry.
- **Outputs:**
  - Visual overlays for operator console displays (bounding boxes, track tails, color-coded distress status).
  - Machine-readable structured payloads (e.g., JSON telemetry records containing track IDs, normalized coordinates, and distress confidence metrics) for integration with mission planning systems.

