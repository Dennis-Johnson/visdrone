'''
Convert Visdrone annotation txt file to XML representation
Visdrone Annotation Format:
<bbox_left>, <bbox_top>, <bbox_width>, <bbox_height>, <score>, <object_category>, <truncation>, <occlusion>
'''

import cv2
import os


input_img_folder = 'visdrone_val/images'            #Path to input images folder
input_ann_folder = 'visdrone_val/annotations'       #Path to original text annotations folder
output_ann_folder = 'annotations_val'           	#Path to output annotaions in xml format
output_img_folder = 'images_val'          			#Path to ouput images with the bounding boxes shown

os.makedirs(output_img_folder, exist_ok=True)
os.makedirs(output_ann_folder, exist_ok=True)

label_dict = {
	0: "Ignored Regions",
	1 : "Pedestrian",
	2 : "People",
	3 : "Bicycle",
	4 : "Car",
	5 : "Van",
	6 : "Truck",
	7 : "Tricycle",
	8 : "Awning-Tricycle",
	9 : "Bus",
	10 : "Motor",
	11 : "Others",
}

# Bounding Box thickness and color
thickness = 1
color = (255,0,0)


def constructObjectSection(label, bbox):
	return '''
	<object>
		<name>{}</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>{}</xmin>
			<ymin>{}</ymin>
			<xmax>{}</xmax>
			<ymax>{}</ymax>
		</bndbox>
	</object>
	'''.format(label, bbox[0], bbox[1], bbox[2], bbox[3])


for count, annotation_file in enumerate(os.listdir(input_ann_folder)):
	annotation_path = os.path.join(os.getcwd(), input_ann_folder, annotation_file)

	xml_annotation_name = annotation_file.split('.txt')[0] + '.xml'
	xml_path = os.path.join(os.getcwd(), output_ann_folder, xml_annotation_name)

	img_file_name = annotation_file.split('.txt')[0] + '.jpg'
	img_path = os.path.join(os.getcwd(), input_img_folder, img_file_name)
	output_img_path = os.path.join(os.getcwd(), output_img_folder, img_file_name)

	img = cv2.imread(img_path)

	annotation_string = '''
<annotation>
	<folder>annotations</folder>
	<filename>{}</filename>
	<path>{}</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>{}</width>
		<height>{}</height>
		<depth>{}</depth>
	</size>
	<segmented>0</segmented>'''.format(img_file_name, img_path, img.shape[0], img.shape[1], img.shape[2])

	file = open(annotation_path, 'r')

	for line in file.readlines():
		# Cast all elements to ints
		line = [int(i) for i in line.strip('\n').split(',')] 

		coords_top_left  = (line[0],  line[1])
		coords_top_right = (line[0] + line[2], line[1] + line[3])
		bbox = (*coords_top_left, *coords_top_right)
		
		# Get category
		label = label_dict.get(line[5])		

		# Append a single object's details
		objectSection = constructObjectSection(label, bbox)
		annotation_string += objectSection 

		cv2.rectangle(img, coords_top_left, coords_top_right, color, thickness)

	cv2.imwrite(output_img_path, img)
	annotation_string +=  '</annotation>'

	f = open(xml_path, 'w')
	f.write(annotation_string)
	f.close()
	count += 1
	print('[INFO] Completed {} image(s) and annotation(s) pair'.format(count))