'''
Util for Visdrone Dataset
Renames images (jpg) and annotations (txt) to consecutive integers.

Each image has a identically named annotation file. 
'''
import os 

def main():
	for dataset_type in ["train", "test", "val"]:
		ann_dir = '/Users/dennis/development/visdrone/visdrone_{}/annotations/'.format(dataset_type)
		img_dir = '/Users/dennis/development/visdrone/visdrone_{}/images/'.format(dataset_type)

		for count, filename in enumerate(os.listdir(img_dir)):
			filename = filename.split('.jpg')[0]
			
			# Rename Image
			img_src = img_dir + filename + '.jpg'
			img_dst = img_dir + str(count) + '.jpg'
			os.rename(img_src, img_dst) 

			# Rename corresponding annotation file
			ann_src = ann_dir + filename + '.txt'
			ann_dst = ann_dir + str(count) + '.txt'
			os.rename(ann_src, ann_dst) 

		print("{} images and annotation files renamed.".format(dataset_type))

if __name__ == "__main__":
	main()
