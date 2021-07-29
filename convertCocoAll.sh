#!/bin/zsh
# Script to convert all three datasets to COCO format from PASCAL VOC

python3 voc2coco.py annotations_val/ ./validation/annotations.json
python3 voc2coco.py annotations_test/ ./test/annotations.json
python3 voc2coco.py annotations_train/ ./train/annotations.json

