# Real Time Low Light Video Enhancement

This repository houses the codes and resources associated with our work for the VLSID Design Contest 2024-25.

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

![SDK-AM62A-LP](/Assets/evm.png)

The **SDK-AM62A-LP** is a low-power software development kit designed by Texas Instruments to support the AM62A family of processors, which target edge AI, vision, and industrial IoT applications. This SDK provides comprehensive tools and resources, including prebuilt libraries, frameworks, and documentation, to facilitate efficient development and optimization of machine learning and computer vision solutions. It is tailored for embedded Linux and real-time operating systems, offering developers flexibility and scalability for prototyping and deploying applications across industries.

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



## References

- **Chunle Guo, Chongyi Li, Jichang Guo, Chen Change Loy, Junhui Hou, Sam Kwong, and Runmin Cong.**  
   *"Zero-Reference Deep Curve Estimation for Low-Light Image Enhancement."*  
   Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020, pp. 1780-1789.

- **Chen Wei, Wenjing Wang, Wenhan Yang, and Jiaying Liu.**  
   *"Deep Retinex Decomposition for Low-Light Enhancement."*  
   British Machine Vision Conference (BMVC), 2018.

- [**Zero-DCE for Low-Light Image Enhancement**](https://keras.io/examples/vision/zero_dce/)

- [**EdgeAI TIDL Tool**](https://github.com/TexasInstruments/edgeai-tidl-tools)