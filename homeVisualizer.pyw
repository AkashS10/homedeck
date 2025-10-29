from customtkinter import *
from PIL import Image, ImageTk
import threading
import socket

import constants

def update(value):
    if value:
        light.configure(fg_color="#ffffff")
    else:
        light.configure(fg_color="#777777")

def recv():
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode()
        if data.startswith("L"):
            data = int(data[1])
            update(data)

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

room = CTkFrame(root)
room.place(relx=0.05, rely=0.05, relwidth=0.3, relheight=0.5)

light = CTkFrame(room, corner_radius=500, fg_color="#ffffff")
light.place(relx=0.45, rely=0.45, relwidth=0.1, relheight=0.1)

threading.Thread(target=recv, daemon=True).start()
root.mainloop()