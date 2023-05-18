import os
import shutil

from_dir = "c:/Users/Nayan/Downloads"
to_dir = "Document_Files"

list_of_files = os.listdir(from_dir)
#print (list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == '':
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'Document_Files'


