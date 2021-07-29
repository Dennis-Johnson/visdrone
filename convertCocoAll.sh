#!/bin/zsh
# Script to convert all three datasets to COCO format from PASCAL VOC

python3 voc2coco.py annotations_val/ ./validation/annotations.json && cp -R visdrone_val/images validation
python3 voc2coco.py annotations_test/ ./test/annotations.json && cp -R visdrone_test/images test
python3 voc2coco.py annotations_train/ ./train/annotations.json && cp -R visdrone_train/images train

