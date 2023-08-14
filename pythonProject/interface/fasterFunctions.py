import os
import shutil


def copy_files(origin_path, dest_path):
    os.chdir(origin_path)
    counter = 0
    for file in os.listdir():
        shutil.copy2(file, dest_path)
        counter += 1
    print(str(counter) + " files have copied to " + dest_path)
    return counter


def create_dest_folder(folder_path, folder_name):
    os.makedirs(os.path.join(folder_path, folder_name))
