from tkinter import *
import os
from PIL import Image, ImageTk

class IconGrid:
    # type :
    # 0 = file
    # 1 = dir
    def __init__(self, tk):
        self.tk = tk
    def new(self, type, name):
        canva = Canvas(self.tk, width = 50, bg = '#212121')
        if (type == 0):
            fileName = "./file.png"
        elif (type == 1):
            fileName = "./folder.png"
        img = Image.open(fileName)
        imaged = ImageTk.PhotoImage(img)
        btn = Button(canva, image = imaged)
        btn.grid()
        text = Label(canva, text = name)
        text.grid(row = 1)
        return canva