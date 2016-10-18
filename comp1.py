#Folder/File comparision...
#common files..
#other than common files...

#user options..
#ask for two folder paths..
#raw_input(or) input
#common/uncommon

import os
path1=raw_input("enter the folder path 1: ")
path2=raw_input("enter the folder path 2: ")
list_folder1=os.listdir(path1)
list_folder2=os.listdir(path2)
commonfiles=[]
uncommonfiles=[]
commonfolder=[]
uncommonfolder=[]
if list_folder1==list_folder2:
	print("choose different folders")
else:
	for i in list_folder1:
		if i in list_folder2:
			commonfiles.append(i)
		else:
			uncommonfiles.append(i)
	print("common files in both the folders are:",commonfiles)
	print("uncommon files in both the folder1 are:",uncommonfiles)
	print("uncommon files in both the folder2 are:",uncommonfiles)
	
	
			
