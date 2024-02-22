### Modified the config file './configs/thumos_i3d.yaml'
### Run Training the first stage on THUMOS14 dataset
python ./train.py ./configs/thumos_i3d.yaml --output rpn_split_x

# Testing the first stage on THUMOS14 dataset
python ./eval.py ./configs/thumos_i3d.yaml ./ckpt_base/thumos_i3d_rpn_split_x/