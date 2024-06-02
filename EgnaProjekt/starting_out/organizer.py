import os
import shutil
from tkinter import filedialog as fd

while True:
    directory = fd.askdirectory(title="Select a directory to organize.")
    if os.path.exists(directory):
        break
    else:
        print("Invalid directory path, please try again.")

audio = ['.mp3', '.ogg', '.wav', '.sib', '.midi', '.mid', '.m4a']
images = ['.png', '.jpg', '.jpeg', '.gif']
docs = ['.txt', '.doc', '.docx', '.pdf', '.ppt', '.pptx', '.xls', '.xlsx', '.odt', '.ods', '.odp', '.rtf', '.tex']
archs = ['.zip', '.rar']
video = ['.mp4', '.avi', '.flv', '.wmv']
data = ['.csv', '.json', '.sql', '.bak', '.geojson']
ex = ['.exe', '.msi']
code = ['.py', '.ipynb', '.c', '.cpp', '.java', '.html', '.css', '.js', '.php', '.sql', '.xml', '.yml', '.yaml', '.md', '.sh', '.bat']

def move_files(directory, extensions, folder_name):
    
    folder_path = os.path.join(directory, folder_name)
    
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        
    for file in os.listdir(directory):
        if file.endswith(tuple(extensions)):
            file_path = os.path.join(directory, file)
            shutil.move(file_path, folder_path)
            print(f"Moved {file_path} to {folder_path}")

def sort_directories(base_path):
    directories = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    
    grouped_directories = {}
    for directory in directories:
        prefix = directory[:3]
        if prefix not in grouped_directories:
            grouped_directories[prefix] = []
        grouped_directories[prefix].append(directory)
    
    for prefix, dirs in grouped_directories.items():
        if len(dirs) < 2:
            continue
        
        target_folder = os.path.join(base_path, prefix)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        for directory in dirs:
            src_path = os.path.join(base_path, directory)
            dest_path = os.path.join(target_folder, directory)
            shutil.move(src_path, dest_path)
            print(f"Moved {src_path} to {dest_path}")


move_files(directory, audio, "Audio")
move_files(directory, images, "Images")
move_files(directory, docs, "Docs")
move_files(directory, archs, "Archives")
move_files(directory, video, "Video")
move_files(directory, data, "Data")
move_files(directory, ex, "Executables")
move_files(directory, code, "Code")

sort_directories(directory)