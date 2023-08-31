import os
import shutil

# Vart jag jobbar (dir)
print("Please input the directory you would like to organize.")
directory = os.chdir(input())

# Lära programmet vilka endelser det finns
audio = ['.mp3', '.ogg', '.wav', '.sib', 'midi']
images = ['.png', '.jpg', '.jpeg', '.gif']
docs = ['.txt', '.doc', '.docx']
archs = ['.zip', '.rar']
video = ['.mp4', '.avi', '.flv', 'wmv']
data = ['.csv', '.json', 'xlsx']

# Loopa genom filnamn i dir för att hitta endelser samt skapa/lägga till i rätt dir
for file in os.listdir(directory):
    if not os.path.exists("Audio"):
        os.mkdir("Audio")
    for i in audio:
        if (file.endswith(i)):
            shutil.move(file, "Audio")
for file in os.listdir(directory):
    if not os.path.exists("Images"):
        os.mkdir("Images")
    for i in images:
        if (file.endswith(i)):
            shutil.move(file, "Images")
for file in os.listdir(directory):
    if not os.path.exists("Docs"):
        os.mkdir("Docs")
    for i in docs:
        if (file.endswith(i)):
            shutil.move(file, "Docs")
for file in os.listdir(directory):
    if not os.path.exists("Archives"):
        os.mkdir("Archives")
    for i in archs:
        if (file.endswith(i)):
            shutil.move(file, "Archives")
for file in os.listdir(directory):
    if not os.path.exists("Video"):
        os.mkdir("Video")
    for i in video:
        if (file.endswith(i)):
            shutil.move(file, "Video")
for file in os.listdir(directory):
    if not os.path.exists("Data"):
        os.mkdir("Data")
    for i in data:
        if (file.endswith(i)):
            shutil.move(file, "Data")

#exe och pdf är själva om sin extension så får egna enklare loopar
for file in os.listdir(directory):
    if (file.endswith('.exe')):
        if not os.path.exists("Program"):
            os.mkdir("Program")
        shutil.move(file, "Program")
for file in os.listdir(directory):
    if (file.endswith('.pdf')):
        if not os.path.exists("PDFs"):
            os.mkdir("PDFs")
        shutil.move(file, "PDFs")