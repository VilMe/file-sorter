import os
import shutil

def create_folder(path: str, extension: str) -> str:
    """Creates a folder that is named after the extension of the file passed in"""
    
    
    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path

