import tkinter as tk
from random import randint

def flash(color='white'):
    root = tk.Tk()
    root.configure(bg=color)
    root.overrideredirect(True)
    root.state('zoomed')
    root.attributes('-alpha', 0.9)  # Set window transparency to 50%
    root.after(randint(100,500), root.destroy)  # set the flash time to 100 milliseconds
    root.mainloop()


def flash_strips(colors):
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # Make the root window fullscreen
    root.attributes('-alpha', 0.9)  # Set window transparency to 50%

    for color in colors:
        strip = tk.Frame(root, bg=color)
        strip.pack(fill=tk.BOTH, expand=True)

        # Schedule the destruction of each strip after 100 milliseconds
        root.after(randint(100,500), root.destroy)

    root.mainloop()



strip_colors = ['red', 'purple', 'red', 'orange', 'yellow', 'orange', 'orange']
flash_strips(strip_colors)
flash()

'''
while True:
    if randint(0,5) == 3:
        # Example usage: Flash two strips with different colors
        strip_colors = ['red', 'blue']
        flash_strips(strip_colors)
        #flash()
'''