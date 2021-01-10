# detectron2 ballon dataset train
put this folder to detectron2 root folder

## Credit
[detectron2](https://github.com/facebookresearch/detectron2)
[balloon dataset](https://github.com/davamix/balloon-detectron2)

## Download Dataset
```bash
wget https://github.com/matterport/Mask_RCNN/releases/download/v2.1/balloon_dataset.zip
unzip balloon_dataset.zip
cd balloon_dataset
mv balloon ..
rm -rf balloon_dataset
```

## Train
```bash
python3 train.py
```

and you will get `model_final.pth` in `output` folder

## Use your model
```
python3 predictor.py
```

## Run on GPU
delete `cfg.MODEL.DEVICE = "cpu"`
