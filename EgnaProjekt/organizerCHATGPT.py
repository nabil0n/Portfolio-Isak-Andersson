import os
import shutil

while True:
    directory = input("Enter directory path: ")
    if os.path.exists(directory):
        break
    else:
        print("Invalid directory path, please try again.")

audio = ['.mp3', '.ogg', '.wav', '.sib', 'midi']
images = ['.png', '.jpg', '.jpeg', '.gif']
docs = ['.txt', '.doc', '.docx']
archs = ['.zip', '.rar']
video = ['.mp4', '.avi', '.flv', 'wmv']
data = ['.csv', '.json', 'xlsx']

def move_files(directory, extensions, folder_name):
    folder_path = os.path.join(directory, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    for file in os.listdir(directory):
        if file.endswith(tuple(extensions)):
            file_path = os.path.join(directory, file)
            shutil.move(file_path, folder_path)

move_files(directory, audio, "Audio")
move_files(directory, images, "Images")
move_files(directory, docs, "Docs")
move_files(directory, archs, "Archives")
move_files(directory, video, "Video")
move_files(directory, data, "Data")