# DeTAL: Open-Vocabulary Temporal Action Localization with Decoupled Networks

## Overview

This repository contains the code for DeTAL: Open-Vocabulary Temporal Action Localization with Decoupled Networks [paper](https://ieeexplore.ieee.org/document/10517407). 

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

#### ActivityNet-v1.3 dataset
Download features and annotations from [ActivityNet_i3d](https://github.com/happyharrycn/actionformer_release/tree/main)

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
Modified the config file './configs/thumos_i3d.yaml'
##### Run Training the first stage on THUMOS14 dataset

`python ./train.py ./configs/thumos_i3d.yaml --output rpn_split_x`

##### Run Testing the first stage on THUMOS14 dataset

`python ./eval.py ./configs/thumos_i3d.yaml ./ckpt_base/thumos_i3d_rpn_split_x/`

### Evaluation on the Second Stage

ModiFied the file_path in 'cls_heads.py'

`python ./eval.py ./configs/thumos_i3d.yaml ./ckpt_base/thumos_i3d_rpn_split_x/`

##### We will provide a bash file to facilitate the training and testing of the second stage under various split settings.
