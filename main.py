import os
import shutil

def create_folder(path: str, extension: str) -> str:
    """Creates a folder that is named after the extension of the file passed in"""
    
    
    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


def sort_files(source_path: str):
    """Sorts files based on a given path"""

    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            extension: str = os.path.splitext(filename)[1]

            if extension:
                target_folder: str = create_folder(source_path)
                target_path: str = os.path.join(target_folder, filename)

                shutil.move(file_path, target_path)

def remove_empty_folderss(source_path: str):
    """Removes all empty folders"""

    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        for current_dir in sub_dir:
            folder_path: str = os.path.join(root_dir, current_dir)

            if not os.listdir(folder_path):
                os.rmdir(folder_path)
