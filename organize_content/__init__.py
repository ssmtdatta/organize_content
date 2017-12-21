import os
import shutil


current_dir = os.getcwd()
base_dir = current_dir
unorganized_dir = os.path.join(base_dir+"/","unorganized")
organized_dir = os.path.join(base_dir+"/","organized")
# these are expected types of files 
file_ext = ['jpg', 'png', 'pdf', 'txt', 'tex', 'other']


def makeDir(dir_name):
	if not os.path.exists(dir_name):
		os.makedirs(dir_name)
		print("Created {}".format(dir_name))
	else:
		print("Directory already exists.")


def readDirContent(parent_dir):
	for content in os.listdir(parent_dir):
		childDir = os.path.join(parent_dir+content)
		if os.path.isdir(childDir):
			readDirContent(childDir+"/")    		
		else:
			*rest, ext = content.split(".")
			if ext in file_ext:
				destination_dir = organized_dir + "/" + ext
				shutil.copy(childDir,destination_dir)
			else:
				destination_dir = organized_dir + "/other"
				shutil.copy(childDir,destination_dir)



	
if __name__ == '__main__':
	makeDir(organized_dir)
	for ext in file_ext:
		makeDir(organized_dir+'/'+ext)

	readDirContent(unorganized_dir+'/')



