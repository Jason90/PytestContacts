import os
import shutil
from typing import Union

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(file_name,mode="r") -> Union[str, bytes]:
    file_path = os.path.join(BASE_DIR, file_name)
    # binary mode no encoding
    if 'b' in mode: 
        with open(file_path, mode=mode) as f:
            return f.read()  
    else: 
        with open(file_path, mode=mode, encoding="UTF-8") as f:
            return f.read()  

def write(file_name, data) -> int:
    with open(os.path.join(BASE_DIR, file_name), mode="w", encoding="UTF-8") as f:
        return f.write(data)
    
def create_directory(dir):
    path= os.path.join(BASE_DIR, dir)
    if not os.path.exists(path):
        os.makedirs(path)  
    return path 

def clean_directory(dir):
    path = os.path.join(BASE_DIR, dir)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)
