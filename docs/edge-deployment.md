# Edge Deployment Considerations

Search-and-rescue UAV operations often require on-board real-time perception to support low-latency alert generation and operate in environments lacking high-bandwidth satellite or cellular downlinks.

This document discusses architectural and optimization considerations for deploying this pipeline onto embedded edge platforms, with a focus on the **NVIDIA Jetson Orin Nano**.

> **Note:** The considerations discussed herein represent engineering guidelines and deployment patterns. These models and runtimes have not yet been benchmarked within this repository.

---

## Target Hardware: NVIDIA Jetson Orin Nano

The Jetson Orin Nano is an entry-level embedded system-on-module (SoM) commonly integrated into small unmanned aerial systems (sUAS) due to its power efficiency and compact form factor.

### Architectural Parameters
- **Compute:** Ampere architecture GPU with dedicated Tensor Cores and an ARM Cortex CPU cluster.
- **Power Envelope:** Configurable operation modes (typically 7W to 15W).
- **Memory Bandwidth:** Unified memory architecture (typically 4GB or 8GB LPDDR5 shared between CPU and GPU).
- **Implication for Vision Pipelines:** Memory footprint and thermal throttling are critical design constraints. Pipeline stages must avoid unnecessary memory allocations and host-to-device transfers.

---

## Acceleration and Optimization Strategies

### 1. Model Compilation via NVIDIA TensorRT
TensorRT optimizes deep learning models for inference on NVIDIA hardware by:
- Fusing adjacent layers (e.g., Conv + BatchNorm + Activation).
- Selecting kernel implementations optimal for target GPU microarchitecture.
- Eliminating unused subgraphs and tensor memory re-use.

Target workflow:
```
PyTorch Model (.pt) ──> ONNX Intermediate Representation (.onnx) ──> TensorRT Engine (.engine)
```

### 2. Precision Optimization (FP16 / INT8)
- **FP16 (Half Precision):** Typically offers significant throughput improvements on Ampere Tensor Cores with negligible accuracy degradation for maritime small-target detection.
- **INT8 (Quantization):** Reduces memory bandwidth pressure and latency further, but requires representative calibration datasets to avoid quantization error on tiny targets like distant swimmers.

### 3. Pipeline Engineering for Streaming Video
- **Zero-Copy Memory Pipelines:** Leveraging unified memory via NVIDIA JetPack libraries (VPI, GStreamer plugins, or NVMM memory buffers) reduces CPU-GPU copy bottlenecks.
- **Decoupled Execution:** Decoupling frame acquisition, detection inference, and tracking onto separate execution threads or worker queues prevents tracking frame drops when detection takes multiple frame periods.

---

## Performance Profiling Considerations

Before conducting flight integration tests, edge pipelines should be profiled against:
- **Inference Latency:** Mean and 99th percentile execution time per frame.
- **End-to-End Latency:** Time elapsed from camera sensor capture to final structured alert generation.
- **Thermal and Power Profiling:** Monitoring system thermals under sustained maximum workload using tools such as `tegrastats` or NVIDIA Nsight Systems.
- **Memory Consumption:** Ensuring peak unified memory usage remains safely beneath physical RAM limits to prevent out-of-memory kernel panics during flight.

