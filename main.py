from tkinter import *
import os
from IconGrid import IconGrid

tk = Tk()
tk.geometry("400x500")
tk.title('Explorer')
tk.resizable(1, 1)

# Variables
PWD = StringVar()
PWD.set(os.getcwd())
iconGrid = []

# Functions
def clear_win():
    global tk, mainCanva
    a = 0
    if (len(iconGrid) == 0):
        return
    for i in range(0, a):
        iconGrid[a].grid_forget()
        iconGrid[a].destroy()
    mainCanva.grid_forget()
    mainCanva.destroy()
    iconGrid.clear()
    mainCanva = Canvas(tk, width = 400)
    mainCanva.grid(row = 1, sticky = 'nsew')
    return

def print_list(fdlist, fdtype, a, i, j):
    for node in fdlist:
        o = IconGrid(mainCanva)
        iconGrid.append(o.new(fdtype, node))
        iconGrid[a].grid(row = i, column = j)
        j += 1
        a += 1
        if (j >= 3):
            j = 0
            i += 1
    return ([a, i, j])

def print_dir(self):
    global mainCanva
    mainCanva = clear_win()
    a = i = j = 0
    for (path, dirs, files) in os.walk(PWD.get()):
        a, i, j = print_list(dirs, 1, a, i, j)
        a, i, j = print_list(files, 0, a, i, j)
    return

# Widgets
pathInput = Entry(tk, font = 30, width = 400, textvariable = PWD)
pathInput.grid(sticky = "ew")

mainCanva = Canvas(tk, width = 400)
mainCanva.grid(sticky = "nsew")

tk.bind('<Return>', print_dir)
tk.mainloop()