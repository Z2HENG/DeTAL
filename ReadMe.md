# DeTAL: Open-Vocabulary Temporal Action Localization with Decoupled Networks

## Overview

This repository contains the code for DeTAL: Open-Vocabulary Temporal Action Localization with Decoupled Networks [paper](https://www.baidu.com). 

![Overview](./assets/overview.png)

## Installation
The project was modified from [ActionFormer](https://github.com/happyharrycn/actionformer_release), thanks for their wonderful work!

+ Recommended Environment: python >= 3.8, cuda 11.3, PyTorch 1.10.2
+ Install dependencies: `pip install -r requirements.txt`
+ Install NMS(Non-Maximum Suppression) by following steps:
  `cd ./libs/utils; python setup.py install --user; cd ../..`

## Data Preparation
#### Thumos14 dataset
Download features and annotations from [Thumos_i3d](https://github.com/happyharrycn/actionformer_release/tree/main)

Unpack the zip folder and modified as './data', the folder structure should look like

```
DeTAL-release/
  ├── data
  │   ├── anet_1.3
  │   │   ├── annotations
  │   │   ├── i3d_features
  │   │   ├── tsp_features
  │   └── thumos
  │       ├── annotations
  │       ├── i3d_features
  ├── libs
  ├── tools
  ├── eval.py
  ├── train.py
  └── ...
```


## Training and Testing

### First Stage
