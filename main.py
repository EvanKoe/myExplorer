from tkinter import *
import os
from IconGrid import IconGrid

tk = Tk()
tk.geometry("900x500")
tk.title('Explorer')
tk.resizable(1, 1)

# Variables
PWD = StringVar()
PWD.set(os.getcwd())
iconGrid = []
a = 0
tk.update()
n = 3

# Functions
def clear_win():
    global tk, mainCanva, a
    if (len(iconGrid) == 0):
        return
    for i in iconGrid:
        i.grid_forget()
        i.destroy()
    iconGrid.clear()
    a = 0
    return

def print_list(fdlist, fdtype, i, j):
    global a, o, n
    for node in fdlist:
        iconGrid.append(o.new(fdtype, node))
        iconGrid[a].grid(row = i, column = j)
        j += 1
        a += 1
        if (j >= 3):
            j = 0
            i += 1
    return ([a, i, j])

def print_dir():
    global mainCanva, a
    a = i = j = 0
    for (path, dirs, files) in os.walk(PWD.get()):
        a, i, j = print_list(dirs, 1, i, j)
        a, i, j = print_list(files, 0, i, j)
    return

def print_dir_b(self):
    global mainCanva
    mainCanva = clear_win()
    print_dir()


# Widgets
pathInput = Entry(tk, font = 30, width = 400, textvariable = PWD)
pathInput.grid(sticky = "ew")

mainCanva = Canvas(tk, width = 400, bg = "#212121")
mainCanva.grid(sticky = "nsew")

sc = Scrollbar(mainCanva)
sc.grid(row = 0, column = 1)

o = IconGrid(mainCanva)
print_dir()

tk.bind('<Return>', print_dir_b)
tk.mainloop()

#   TODO
# Put a scrollbar
# Put an adaptive item number (columns)
# Finish the design
# Make forward button