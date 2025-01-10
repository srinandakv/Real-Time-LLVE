# Real Time Low Light Video Enhancement

This repository houses the codes and resources associated with our work for the VLSID Design Contest 2024-25.

>### 🏆 This project has been recognized as one of the top 5 TI projects of the Design Contest at the prestigious VLSI Design Conference 2025.
> [Check out the post ⭢](https://www.linkedin.com/posts/himalya_brightertogether-vlsid2025-activity-7276544217110269952-IYtX?utm_source=share&utm_medium=member_desktop)

## Team Members

<a href="https://github.com/srinandakv/Real-Time-LLVE/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=srinandakv/Real-Time-LLVE" />
</a>

## Abstract

This project provides a real-time low-light video enhancement system for the Texas Instruments' SK-AM62A-LP platform. Optimized for the platform’s ARM processor and AI accelerators, it uses deep learning to improve video clarity in low-light conditions, making it ideal for surveillance and automotive applications.

## Technologies Used

![Tech Used](https://go-skill-icons.vercel.app/api/icons?i=python,tensorflow,scikitlearn,numpy,linux)

## System Block Diagram

![block_diagram](/Assets/block_diagram_dark.png#gh-dark-mode-only)
![block_diagram](/Assets/block_diagram_light.png#gh-light-mode-only)

## About the Hardware

![SK-AM62A-LP](/Assets/evm.png)

The TI **SK-AM62A-LP** evaluation module is a cost-effective development platform designed for evaluating and prototyping applications with Texas Instruments' AM62A processor. Targeting AI and vision-centric use cases, this low-power board supports machine learning inference, edge computing, and industrial IoT applications. It features key interfaces such as HDMI, Ethernet, and USB for flexible connectivity, along with camera and display options to facilitate multimedia processing. The EVM is also compatible with TI's software ecosystem, including Processor SDK Linux and Edge AI tools, enabling developers to accelerate application development with robust support and pre-built examples.

## About the Model

**Zero-Reference Deep Curve Estimation (Zero-DCE)** is a deep learning-based approach forlow-light image enhancement that stands out because it does not rely on any paired or unpaired data for training (hence, "zero-reference"). It operates by estimating a set of enhancement curves that are applied to the input image to produce an enhanced output. The architecture is lightweight, efficient, and capable of running on low-resource devices, making it an attractive choice for this project.

## About the Dataset

The model will be trained using the low light images from the **LoL (Low Light) dataset**. The LoL dataset is specifically designed for the task of low-light image enhancement. It consists of 500 pairs of low-light and normal-light images captured in real-world environments. However in order to train the DCE-Net, the corresponding enhanced images will not be required.

## Deployment on Hardware

To deploy the model on TI’s SK-AM62A-LP, the model is first coverted to LiteRT (formerly known as Tensorflow Lite) format. Using the `tflite_runtime` python module, which comes installed in the EdgeAI Processor SDK, the tflite file can be used to perform inferencing. At this point, inferencing is performed using the ARM Cortex A53 core which is part of the AM62A processor.

In order to use the built-in C7x DL accelerator for inferencing, the model is compiled using the [EdgeAI TIDL Tool](https://github.com/TexasInstruments/edgeai-tidl-tools) to obtain the model artifacts. The compilation process involves writing a configuration file which consists of information about the model to be used, normalization and image preprocessing. The configuration file is used by the TIDL tool to parse, optimize and calibrate the model and to generate the model artifacts. These artifacts are then used by the `tflite_runtime` module to delegate tasks to the DL accelerator for inferencing.

## CPU vs. C7x DL Accelerator

![Comparison of Results](/Assets/result_compare.png)

As seen in the image above, the enhanced image processed on CPU is much clearer than that processed on the DL accelerator. This difference in quality could be due to issues in quantization that could have come up during model compilation. However, since this project is targetting towards real time enhancement, the DL accelerator would be the right choice of device due to its faster processing speeds which is ~98% less than that of the CPU.

## Final Result

https://github.com/user-attachments/assets/6710611b-e4fd-4c9c-aef8-357d4221ba28

## References

- Chunle Guo, Chongyi Li, Jichang Guo, Chen Change Loy, Junhui Hou, Sam Kwong, and Runmin Cong, "Zero-Reference Deep Curve Estimation for Low-Light Image Enhancement." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020, pp. 1780-1789.

- Chen Wei, Wenjing Wang, Wenhan Yang, and Jiaying Liu, "Deep Retinex Decomposition for Low-Light Enhancement." British Machine Vision Conference (BMVC), 2018.

- [Zero-DCE for Low-Light Image Enhancement](https://keras.io/examples/vision/zero_dce/)

- [EdgeAI TIDL Tool](https://github.com/TexasInstruments/edgeai-tidl-tools)
