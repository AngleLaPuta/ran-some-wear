import time
import webbrowser

import pyautogui
import requests
import tempfile
import os
import sys
import subprocess

import requests
import os
from pathlib import Path

def checkInternet():
    hostname = "google.com"
    response = os.system("ping " + hostname)
    return response == 0

def dostuff():
    print('weed')
def promptInternet():
    offline_start_time = None

    while True:
        if checkInternet():
            if offline_start_time is not None:
                elapsed_time = time.time() - offline_start_time
                if elapsed_time >= 300:  # 300 seconds = 5 minutes
                    dostuff()
                offline_start_time = None
        else:
            if offline_start_time is None:
                offline_start_time = time.time()
        webbrowser.open("turn on your internet nigga")
        time.sleep(10)

def download(link):
    # Send a GET request to the link
    response = requests.get(link)
    response.raise_for_status()  # Raise an exception if the request was not successful

    # Get the filename from the URL
    filename = link.split("/")[-1]

    # Set the path to the Downloads folder
    downloads_path = str(r"C:\Users\jkjones\PycharmProjects\ran-some-wear\DesktopGoose v0.31\Assets\Images\Memes")

    # Save the downloaded content in the Downloads folder
    file_path = os.path.join(downloads_path, filename)
    with open(file_path, "wb") as file:
        file.write(response.content)

    # Open the file using the default application associated with its file type
    try:
        pass
        #os.startfile(file_path)  # For Windows
    except AttributeError:
        try:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, file_path])  # For macOS and Linux
        except:
            print("Unable to open the file. Please check the file type and associated default application.")

    # Optionally, you can return the path of the downloaded file if needed
    return file_path