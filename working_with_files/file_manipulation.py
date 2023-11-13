#built in modules for handling files
#os, shutil, pathlib
import os

# try:
#     os.mkdir('clean_up')
# except:
#     print('Directory exists already')

# files_in_directory = os.scandir('.')
# for file in files_in_directory:
#     if os.path.isfile(file):
#         print('file: ', file.name)
#     elif os.path.isdir(file):
#         print('directory: ', file.name)

# below moved all the files into the clean_up directory

folder_org = '.'
# folder_dest = 'c:/users/chrxki1/git/python/python-getting-started/working_with_files/clean_up'
folder_dest = './clean_up'
#join will add missing slashes or remove extra slashes for us
location_org = os.path.join(folder_org, 'new.txt')
location_dest = os.path.join(folder_dest, 'new.txt')

try:
    os.mkdir('clean_up')
except:
    print('Directory exists already')

for entry in os.scandir(folder_org):    
    location_org = os.path.join(folder_org, entry.name)
    location_dest = os.path.join(folder_dest, entry.name)

    if os.path.isfile(location_org):
        os.rename(location_org,location_dest)