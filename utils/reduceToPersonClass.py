'''
Util to merge the 'People' and 'Pedestrian' classes in Visdrone
to a single 'person' class. Discard the remaining annotations.
Uses the COCO detection format of Visdrone-DET2021.
'''
import json 

TRAIN_ANNOTATIONS_PATH = 'train/annotations.json'
VALIDATION_ANNOTATIONS_PATH = 'validation/annotations.json'
TEST_ANNOTATIONS_PATH = 'test/annotations.json'

def reduceToPersonClass(annotationFilePath, datasetName):
    with open(annotationFilePath) as ann_file:
        annotations = json.load(ann_file)

    for category in annotations["categories"]:
        print(f"INFO: Found category {category}")

    # Copy the unchanged fields to a new dict
    updated_annotations = {
        "images": annotations["images"],
        "type": "instances",
        "annotations": [],
        "categories": [{"id": 1, "name": "person", "supercategory": ""}]
    }

    hitCount = 0
    for annotation in annotations["annotations"]:
        # Class 2 corresponds to 'Pedestrian'
        # Class 3 corresponds to 'People'
        if annotation["category_id"] == 2 or annotation["category_id"] == 3:
            hitCount += 1
            # Change to class 1: 'person' and add to the new annotations dict.
            annotation["category_id"] =  1
            updated_annotations["annotations"].append(annotation)

    print(f"\nINFO: Converted {hitCount} instances to 'person' class.")
    obj = json.dumps(updated_annotations) #Serialize

    new_file_path = datasetName + "_personOnly.json"

    # Overwrite with updated_annotations
    with open(new_file_path, "w") as outfile:
        outfile.write(obj)
        print(f"INFO: Pruned classes in the {datasetName} dataset.\n")
        

if __name__ == "__main__":
    reduceToPersonClass(TRAIN_ANNOTATIONS_PATH, "train")
    reduceToPersonClass(VALIDATION_ANNOTATIONS_PATH, "validation")
    reduceToPersonClass(TEST_ANNOTATIONS_PATH, "test")