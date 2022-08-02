import os
import shutil

download_path = os.path.expanduser("~") + "/Downloads/"

# Asking for the Path
print("What Folder do you want to sort?")
print("You can choose between: Downloads or an Specific Path!")
print("Mind you have to write the full Path (Example: C:\\Users\\Name\\Downloads)")
print("Write \"Downloads\" or specific")

path = input()

# Decides on path of the sorter
if path == ('Downloads' or 'downloads'):
    download_path = os.path.expanduser("~") + "/Downloads/"
    download_path_2 = os.path.expanduser("~") + "/Downloads/"
else:
    download_path = path + "/"
    download_path_2 = path + "/"
print(download_path)
print(path)
# Info Message
print("Please make sure you have no open Files in the Download folder (including this one)")
print("Press enter to continue!")

input()

# Definition of variables
fileNames = os.listdir(download_path)  # Gets all file names from Path
folders = dict()  # Creates a dictionary
fileEnding = dict()  # Creates a dictionary
value = 0  # number of File

# Checks Folder ending (for example .exe)
for fileName in fileNames:
    var: int = value + 1
    if '.' in fileName:
        numberOfDots = len(fileName.split('.')) - 1
        fileEnding[fileName.split('.', numberOfDots)[numberOfDots]] = value
    else:
        folders[fileName] = value

# Checks if file Ending already exists as Folder if not creates a Folder
folderExists = False
for x in fileEnding:
    download_path = download_path_2
    download_path = download_path + '.' + x
    if not os.path.exists(download_path):
        os.mkdir(download_path)
        print('Directory ', x, ' Created')
    else:
        print('Directory ', x, ' already exists')

# Redefines Folder path
download_path = download_path_2

# Main Code
for fileName in fileNames:
    if '.' in fileName:
        numberOfDots = len(fileName.split('.')) - 1
        currentFileEnding = fileName.split('.', numberOfDots)[numberOfDots]
        try:  # Tries to move File
            shutil.move(download_path + fileName, download_path + '.' + currentFileEnding)
        except PermissionError:  # If file is running
            print("The file: " + fileName + " is currently running! Try again after this!")
        except shutil.Error:  # If file Name already exists
            print("The file: " + fileName + " exists twice! do you want to overwrite the old file? Write \"yes\" if so")
            if input() == "yes":
                try:
                    os.remove((download_path + '.' + currentFileEnding + '/') + fileName)  # Removes file
                    print("Successfully deleted")
                    try:  # Tries to move File
                        shutil.move(download_path + fileName, download_path + '.' + currentFileEnding)
                        print("Successfully Moved")
                        print("Successfully Replaced")
                    except PermissionError:  # Checks if file is running
                        print("The file: " + fileName + " is currently running! Try again after this!")
                except PermissionError:  # Checks if file is running
                    print("The file: " + fileName + " is currently running! Try again after this!")
# Checks if the File is a Folder if so moves to Folder "Folder"
    if not os.path.exists(download_path + "Folder"):
        os.mkdir(download_path + "Folder")
    isFile = os.path.isfile(download_path + fileName)
    if not isFile:
        print(fileName)
        numberOfDots = len(fileName.split('.')) - 1
        if not numberOfDots > 0:
            try:
                shutil.move(download_path + fileName, download_path + "Folder")
            except PermissionError:  # Checks if file is running inside Folder
                print("An File in The Folder: " + fileName + " is currently running! Try again after this!")
            except shutil.Error:
                print("The File: " + fileName + " exists twice! do you want to overwrite the old file? Write "
                                  "\"yes\" if so")
                if input() == "yes":
                    try:
                        shutil.rmtree((download_path + "Folder/") + fileName)  # Removes file
                        print("Successfully deleted")
                        shutil.move(download_path + fileName, download_path + "Folder")
                        print("Successfully Moved")
                        print("Successfully Replaced")
                    except PermissionError:  # Checks if file is running inside Folder
                        print("An File in The Folder: " + fileName + " is currently running! Try again after this!")

print("Press enter to stop the program!")
input()
