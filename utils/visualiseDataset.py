'''
View ground truth bounding boxes from the dataset.
Sample a number of random images from each dataset type.
'''
import torch
print(torch.__version__, torch.cuda.is_available())

from detectron2.data.datasets import register_coco_instances
from detectron2.utils.logger import setup_logger
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
import  cv2, random


setup_logger()

# Register the custom datasets (COCO format)
if 'visdrone_train' in DatasetCatalog.list():
  DatasetCatalog.remove("visdrone_train")
if 'visdrone_validation' in DatasetCatalog.list():
  DatasetCatalog.remove("visdrone_validation")
if 'visdrone_test' in DatasetCatalog.list():
  DatasetCatalog.remove("visdrone_test")

# Choose annotation files accordingly.
register_coco_instances("visdrone_train", {}, "train_personOnly.json", "train/images")
register_coco_instances("visdrone_validation", {}, "validation_personOnly.json", "validation/images")
register_coco_instances("visdrone_test", {}, "test_personOnly.json", "test/images")

train_dataset_dicts = DatasetCatalog.get("visdrone_train")
train_metadata = MetadataCatalog.get("visdrone_train")
validation_dataset_dicts = DatasetCatalog.get("visdrone_validation")
validation_metadata = MetadataCatalog.get("visdrone_validation")
test_dataset_dicts = DatasetCatalog.get("visdrone_test")
test_metadata = MetadataCatalog.get("visdrone_test")

for d in random.sample(train_dataset_dicts, 2):
    img = cv2.imread(d["file_name"])
    visualizer = Visualizer(img[:, :, ::-1], metadata=train_metadata, scale=0.8)
    out = visualizer.draw_dataset_dict(d)
    cv2.imshow("train" + d["file_name"], out.get_image()[:, :, ::-1])


for d in random.sample(validation_dataset_dicts, 2):
    img = cv2.imread(d["file_name"])
    visualizer = Visualizer(img[:, :, ::-1], metadata=validation_metadata, scale=0.8)
    out = visualizer.draw_dataset_dict(d)
    cv2.imshow("validation" + d["file_name"], out.get_image()[:, :, ::-1])

for d in random.sample(test_dataset_dicts, 2):
    img = cv2.imread(d["file_name"])
    visualizer = Visualizer(img[:, :, ::-1], metadata=test_metadata, scale=0.8)
    out = visualizer.draw_dataset_dict(d)
    cv2.imshow("test" + d["file_name"], out.get_image()[:, :, ::-1])

cv2.waitKey(0)
cv2.destroyAllWindows()