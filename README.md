# Real Time Low Light Video Enhancement

### Team Members: Joel Jojo Painuthara, K.V.Srinanda

### This repository houses the code and resources associated with our work for the VLSID Design Contest 2024.

## Abstract
This project provides a real-time low-light video enhancement system for the Texas Instruments' SK-AM62A-LP platform. Optimized for the platform’s ARM processor and AI accelerators, it uses deep learning to improve video clarity in low-light conditions, making it ideal for surveillance and automotive applications.

## Technologies Used
![Tech Used](https://go-skill-icons.vercel.app/api/icons?i=python,tensorflow,scikitlearn,numpy,tflite)

## System Block Diagram
![image](https://github.com/user-attachments/assets/94f0396b-7986-447c-86f1-0c3f81b163f3)

## Model and Dataset
Zero-Reference Deep Curve Estimation (Zero-DCE) is a deep learning-based approach for low-light image enhancement that stands out because it does not rely on any paired or unpaired data for training (hence, "zero-reference"). It operates by estimating a set of enhancement curves that are applied to the input image to produce an enhanced output. The architecture is lightweight, efficient, and capable of running on low-resource devices, making it an attractive choice for this project.

The model will be trained using the low light images from the LoL (Low Light) dataset.The LoL (Low-Light) dataset is specifically designed for the task of low-light image enhancement. It consists of 500 pairs of low-light and normal-light images captured in real- world environments. However in order to train the DCE-Net, the corresponding enhanced images will not be required.

## References

1. **Chunle Guo, Chongyi Li, Jichang Guo, Chen Change Loy, Junhui Hou, Sam Kwong, and Runmin Cong.**  
   *"Zero-Reference Deep Curve Estimation for Low-Light Image Enhancement."*  
   Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020, pp. 1780-1789.

2. **Chen Wei, Wenjing Wang, Wenhan Yang, and Jiaying Liu.**  
   *"Deep Retinex Decomposition for Low-Light Enhancement."*  
   British Machine Vision Conference (BMVC), 2018.

3. [**Zero-DCE for Low-Light Image Enhancement**](https://keras.io/examples/vision/zero_dce/)

