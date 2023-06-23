import os
import random
import ctypes
from PIL import Image
from screeninfo import get_monitors
import sys
import subprocess

def get_random_directory(root_directory):
    # List of secret target folders to search within before main target folders
    secret_target_folders = ['yiff','homework','porn', 'OwO']

    # List of main target folders to search within
    main_target_folders = ['Photos', 'Downloads', 'Pictures']

    # Initialize an empty list to store the directories found within target folders
    directories = []

    # Search for secret target folders within the root directory
    for folder in secret_target_folders:
        folder_path = os.path.join(root_directory, folder)

        if os.path.isdir(folder_path):
            for dirpath, dirnames, filenames in os.walk(folder_path):
                directories.extend([os.path.join(dirpath, dirname) for dirname in dirnames])

    if not directories:
        # If no directories are found in secret target folders, search within main target folders
        for folder in main_target_folders:
            folder_path = os.path.join(root_directory, folder)

            if os.path.isdir(folder_path):
                for dirpath, dirnames, filenames in os.walk(folder_path):
                    directories.extend([os.path.join(dirpath, dirname) for dirname in dirnames])

    if not directories:
        return None  # Return None if no directories are found

    # Select a random directory
    random_directory = random.choice(directories)

    return random_directory

def get_random_image_path(directory):
    # Get a list of all files in the specified directory
    files = os.listdir(directory)

    # Filter the files to include only image files (you can modify this condition based on your specific requirements)
    image_files = [file for file in files if file.endswith(('.png', '.jpg', '.jpeg', '.webp'))]

    if not image_files:
        return None  # Return None if no image files are found

    # Select a random image file
    random_image = random.choice(image_files)

    # Get the absolute path of the random image file
    absolute_path = os.path.abspath(os.path.join(directory, random_image))

    return absolute_path



def resize_to_monitor(image_path):
    screen_width = get_monitors()[0].width
    screen_height = get_monitors()[0].height

    image = Image.open(image_path)
    resized_image = image.resize((screen_width, screen_height), Image.ANTIALIAS)

    resized_image.save("ballsacks.png")  # Save the resized image as PNG



def bg():
    # Get the user's home directory
    home_directory = os.path.expanduser('~')

    # Set a flag to indicate if an image file is found
    image_found = False

    while not image_found:
        # Get a random directory path within the target folders
        random_directory_path = get_random_directory(home_directory)

        if random_directory_path:
            # Get a random image path within the random directory
            random_image_path = get_random_image_path(random_directory_path)

            if random_image_path:
                resize_to_monitor(random_image_path)
                image_found = True
                SPI_SETDESKWALLPAPER = 0x0014
                SPIF_SENDCHANGE = 0x02

                # Set the desktop wallpaper
                ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r'C:\Users\jkjones\PycharmProjects\pygui practice\ballsacks.png', SPIF_SENDCHANGE)
            else:
                pass
        else:
            break

def img():
    # Get the user's home directory
    home_directory = os.path.expanduser('~')

    # Set a flag to indicate if an image file is found
    image_found = False

    while not image_found:
        # Get a random directory path within the target folders
        random_directory_path = get_random_directory(home_directory)

        if random_directory_path:
            print("Random Directory Path:", random_directory_path)

            # Get a random image path within the random directory
            random_image_path = get_random_image_path(random_directory_path)

            if random_image_path:
                print("Random Image Path:", random_image_path)
                resize_to_monitor(random_image_path)
                image_found = True
                # Open the file using the default application associated with its file type
                try:
                    os.startfile(random_image_path)  # For Windows
                except AttributeError:
                    try:
                        opener = "open" if sys.platform == "darwin" else "xdg-open"
                        subprocess.call([opener, random_image_path])  # For macOS and Linux
                    except:
                        pass
            else:
                pass
        else:
            break


bg()