#!/bin/zsh
# Script to convert all three datasets to xml format (PASCAL VOC)

python3 convertVis_to_xml.py val
python3 convertVis_to_xml.py test
python3 convertVis_to_xml.py train
