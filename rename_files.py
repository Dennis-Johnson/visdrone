'''
Util for Visdrone Dataset
Renames images (jpg) and annotations (txt)to consecutive integers.

Input: 
'''

import os 

path = '/Users/dennis/development/visdrone/visdrone_val/annotations/'
file_extension = '.txt'

for count, filename in enumerate(os.listdir(path)):
	src = path + filename
	dst = path + str(count) + file_extension
	os.rename(src, dst) 
	
print("Files renamed")
