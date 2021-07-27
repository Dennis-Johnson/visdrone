# Pythono3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os 

annotations_path = '/Users/dennis/development/visdrone/visdrone_val'
# Function to rename multiple files 
def main(): 

	for count, filename in enumerate(os.listdir("D:\\8th SEM project\\vis_new\\train_annotations_txt\\")): #Directory in which the files have to be renamed
		dst =str(count) + ".txt"
		src ='D:\\8th SEM project\\vis_new\\train_annotations_txt\\'+ filename #original file name
		dst ='D:\\8th SEM project\\vis_new\\train_annotations_txt\\'+ dst  #new file name
		
		os.rename(src, dst) 

if __name__ == '__main__': 

	main() 
	print("Files have been renamed successfully.")
