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
docs = ['.txt', '.doc', '.docx', '.pdf', '.ppt', '.pptx',
        '.xls', '.xlsx', '.odt', '.ods', '.odp', '.rtf', '.tex']
archs = ['.zip', '.rar', '.tar', '.gz', '.bz2', '.7z', '.xz', '.tar.gz']
video = ['.mp4', '.avi', '.flv', '.wmv', '.mov', '.mkv',
         '.webm', '.mpeg', '.mpg', '.3gp', '.3g2', '.m4v', '.rmvb']
data = ['.csv', '.json', '.sql', '.bak', '.geojson']
ex = ['.exe', '.msi']
code = ['.py', '.ipynb', '.c', '.cpp', '.java', '.html', '.css', '.js',
        '.php', '.sql', '.xml', '.yml', '.yaml', '.md', '.sh', '.bat']

all_extensions = audio + images + docs + archs + video + data + ex + code


def move_files(directory, extensions, folder_name):

    folder_path = os.path.join(directory, folder_name)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    for file in os.listdir(directory):
        if file.endswith(tuple(extensions)):
            source_path = os.path.join(directory, file)
            destination_path = os.path.join(folder_path, file)

            if os.path.exists(destination_path):
                print(
                    f"File {file} already exists in {folder_name}, adding suffix")
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(os.path.join(folder_path, f"{base}_{counter}{ext}")):
                    counter += 1
                new_file_name = f"{base}_{counter}{ext}"
                destination_path = os.path.join(folder_path, new_file_name)
                print(f"Renamed to {new_file_name}")
            shutil.move(source_path, destination_path)
            print(f"Moved {source_path} to {destination_path}")


def sort_directories(base_path):
    directories = [d for d in os.listdir(base_path) if os.path.isdir(
        os.path.join(base_path, d)) and len(d) > 3]

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
            os.makedirs(target_folder, exist_ok=True)

        for directory in dirs:
            src_path = os.path.join(base_path, directory)
            dest_path = os.path.join(target_folder, directory)
            shutil.move(src_path, dest_path)
            print(f"Moved {src_path} to {dest_path}")


def get_miscellaneous_files(directory, known_extensions):
    misc_files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            _, ext = os.path.splitext(file)
            if ext and ext not in known_extensions:
                misc_files.append(file)
    return misc_files


move_files(directory, audio, "Audio")
move_files(directory, images, "Images")
move_files(directory, docs, "Docs")
move_files(directory, archs, "Archives")
move_files(directory, video, "Video")
move_files(directory, data, "Data")
move_files(directory, ex, "Executables")
move_files(directory, code, "Code")

misc_files = get_miscellaneous_files(directory, all_extensions)
if misc_files:
    misc_folder = os.path.join(directory, "Miscellaneous")
    if not os.path.exists(misc_folder):
        os.mkdir(misc_folder)

    for file in misc_files:
        source_path = os.path.join(directory, file)
        destination_path = os.path.join(misc_folder, file)

        if os.path.exists(destination_path):
            print(f"File {file} already exists in Miscellaneous, adding suffix")
            base, ext = os.path.splitext(file)
            counter = 1
            while os.path.exists(os.path.join(misc_folder, f"{base}_{counter}{ext}")):
                counter += 1
            new_file_name = f"{base}_{counter}{ext}"
            destination_path = os.path.join(misc_folder, new_file_name)
            print(f"Renamed to {new_file_name}")

        shutil.move(source_path, destination_path)
        print(f"Moved {source_path} to {destination_path}")

sort_directories(directory)
