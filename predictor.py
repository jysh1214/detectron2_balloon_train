from detectron2.utils.visualizer import Visualizer
from detectron2.data.catalog import MetadataCatalog, DatasetCatalog
import cv2
from detectron2.engine import DefaultTrainer
from detectron2.config import get_cfg
import os
from detectron2.engine.defaults import DefaultPredictor
from detectron2.utils.visualizer import ColorMode

balloon_metadata = MetadataCatalog.get("balloon_train")

if __name__ == "__main__":
    cfg = get_cfg()
    cfg.merge_from_file(
        "../configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
    )
    cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")
    print('loading from: {}'.format(cfg.MODEL.WEIGHTS))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5   # set the testing threshold for this model
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 3
    cfg.DATASETS.TEST = ("balloon_train", )

    # Run on cpu
    cfg.MODEL.DEVICE = "cpu"

    predictor = DefaultPredictor(cfg)

    data_f = './balloon/val/410488422_5f8991f26e_b.jpg'
    im = cv2.imread(data_f)
    outputs = predictor(im)
    v = Visualizer(im[:, :, ::-1],
                   metadata=balloon_metadata,
                   scale=0.8,
                   instance_mode=ColorMode.IMAGE_BW   # remove the colors of unsegmented pixels
                   )
    v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    img = v.get_image()[:, :, ::-1]
    cv2.imshow('predict', img)
    cv2.waitKey(0)
