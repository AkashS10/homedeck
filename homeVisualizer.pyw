from customtkinter import *
from PIL import Image, ImageTk
import socket

import constants

# Socket init
s = socket.socket()
s.connect(("localhost", 20119))

# Window init
root = CTk()
root.title(constants.TITLE + " - Visualizer")
root.minsize(1120, 630)
root.focus_force()

image = Image.open('res/icon.png')
photo = ImageTk.PhotoImage(image)
root.iconphoto(True, photo)

root.mainloop()