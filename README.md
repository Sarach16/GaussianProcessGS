# GP-GS Extension: LMC-Based Multi-Output Gaussian Processes for Enhanced 3D Gaussian Splatting

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

[Original GP-GS Paper](https://arxiv.org/pdf/2502.02283)

## Overview

This project builds on **GP-GS: Gaussian Processes for Enhanced 3D Gaussian Splatting**, a framework that improves 3D Gaussian Splatting by densifying sparse Structure-from-Motion (SfM) point clouds with Multi-Output Gaussian Processes (MOGP).

My work focused on understanding, reproducing, and extending this pipeline, with particular attention to using **Linear Model of Coregionalization (LMC)** to better capture correlations between spatial coordinates and RGB color channels during point cloud densification.

### Pipeline Figures

![Pipeline](assets/gpgs.drawio.png)
![Pipeline Detail](assets/gpgs-Page-6.drawio.png)

## My Contribution

In this project, I worked on:

- studying and reproducing the GP-GS pipeline
- debugging setup and dependency issues in the codebase
- adapting the environment to run correctly
- exploring depth generation for scenes beyond the default example
- experimenting with **LMC-based correlated-output Gaussian Processes**
- comparing correlated-output modeling with independent-output baselines
- documenting the workflow and implementation process more clearly

This project was meaningful to me because it combined research, experimentation, and software engineering. It required reading technical papers, working through incomplete documentation, and making sense of a complex pipeline in practice.

## Project Goal

The goal of GP-GS is to improve the initialization of **3D Gaussian Splatting (3DGS)** by densifying sparse SfM point clouds before Gaussian optimization. Better point cloud initialization can improve reconstruction quality and novel view synthesis, especially in regions with limited structure or sparse coverage.

My extension explores whether **correlated-output Gaussian Process models** can improve this densification step by modeling relationships between geometry and color rather than predicting each output independently.

## Original GP-GS Abstract

3D Gaussian Splatting has emerged as an efficient photorealistic novel view synthesis method. However, its reliance on sparse Structure-from-Motion (SfM) point clouds often limits scene reconstruction quality. GP-GS addresses this by using a multi-output Gaussian Process model to enable adaptive and uncertainty-guided densification of sparse SfM point clouds. GP-based predictions infer new candidate points from input 2D pixels and depth maps, and uncertainty estimates are used to filter noisy predictions. These densified point clouds provide higher-quality initial 3D Gaussians, improving reconstruction performance.

## Pipeline

The overall pipeline consists of:

1. **Multi-view image input**
2. **Depth estimation** using models such as Depth Anything
3. **SfM reconstruction** to generate a sparse point cloud
4. **Point cloud densification** using MOGP
5. **Uncertainty-based filtering** to remove noisy predictions
6. **3D Gaussian initialization and optimization**
7. **Novel view rendering**


## Technical Focus of My Work

My technical focus was on the densification stage.

The MOGP model takes pixel coordinates and depth values as input and predicts:
- 3D position
- RGB color information

I explored how **LMC-based MOGPs** could better model cross-output dependencies, especially between spatial structure and appearance, compared with treating each output independently.

This helped me better understand:
- Gaussian Process modeling
- multi-output regression
- uncertainty-guided filtering
- the role of point cloud quality in downstream rendering

## Tech Stack

- Python
- GPyTorch
- Matplotlib
- 3D Gaussian Splatting
- Multi-Output Gaussian Processes
- COLMAP / SfM processing
- Depth Anything V2
- Conda

## Local Setup

```shell
conda env create --file environment.yml
conda activate GP-GS
pip install gpytorch
pip install matplotlib




### Running
**MOGP**:
```shell
python MOGP/top_four_contribution.py #Find the image from a perspective that contributes most to SfM points cloud.
python MOGP/mogp_train.py #Training MOGP model
python MOGP/predict.py #Predict high quality dense points cloud.
```
**MOGP for 3D gaussians Initialization**:
```shell
python MOGP/rewrite_images_sfm.py
python MOGP/write_points3d.py
```
**3DGS***:
```shell
python train.py -s <scene path>
```
**Render and Evaluation**:
```shell
python render.py -m <model path>
python metrics.py -m <model path>
```


## Notes to running GaussianProcessGS  
```shell
clone repo  
conda env create --file environment.yml  
```
Changes to environment.yml:  
   Commented out # - cudatoolkit=11.6  
   Changed python version to 3.8  

   Submodeles/fused-ssim does not exist(install script expects one)  

   I found this: https://prefix.dev/channels/3dgs/packages/fused-ssim (doesn't work on Mac)  
```shell
pip install gpytorch  
pip install matplotlib  

conda activate GP-GS  
```
### This part below is for Scenes other then "flowers"

In config.py change SCENE to any dataset from mipnerf360 you want to work on  

if you want to ge Depth for datasets in mipnerf360 (other then flowers): 
```shell
   git clone https://github.com/DepthAnything/Depth-Anything-V2.git  
   pip install transformers  
   python generate_depth_map.py
```
   Output: depth folder in "scene" folder with depth map images and stacked depths  

To get the top four key frames of a scene (other then flowers):  
```shell
   python -m MOGP.top_four_contribution
``` 
   Output: mipnerf360/"scene"/top_four_images.json  

### Start here for working on "flowers":  
```shell
python -m MOGP.mogp_train (trains model and saves to gp folder in scene folder/ gives R^2 RMSE and CD)  
python -m MOGP.predict  
python -m MOGP.vis_var  
python -m rewrite_images_sfm 
python =m write_points3d (still being edited)  
```


## 📚Citation
If you find this project useful in your research, please consider cite:

```bibtex
@article{guo2025gp,
  title={GP-GS: Gaussian Processes for Enhanced Gaussian Splatting},
  author={Guo, Zhihao and Su, Jingxuan and Wang, Shenglin and Fan, Jinlong and Zhang, Jing and Han, Liangxiu and Wang, Peng},
  journal={arXiv preprint arXiv:2502.02283},
  year={2025}
}
