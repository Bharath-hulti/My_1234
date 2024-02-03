import os
import shutil

from_dir = "C:/Users/DELL/Downloads"
to_dir = "C:/Users/DELL/Desktop/Coding/Document_Files"
list_of_files = os.listdir(from_dir)
#print(list_of_files)
for i in list_of_files:
    os.path.splitext()   