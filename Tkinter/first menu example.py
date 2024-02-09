from tkinter import *
from tkinter import messagebox

screen=Tk()
screen.title("example #2")
screen.geometry("300x300")

menubar = Menu(screen)
screen.config(menu=menubar)
screen["bg"] = "grey"
commandsmenu = Menu(menubar, tearoff=0)


def death():
    screen.destroy()
    #closes down the window

def saving():
    messagebox.showinfo("Loading...", "Saving...")
    #saving button pop up

menubar.add_cascade(label="Settings", menu=commandsmenu)

commandsmenu.add_command(label="Quit", command=death)
#closes down the window when you press quit
commandsmenu.add_command(label="Save (Ctrl+s)", command=saving)
commandsmenu.add_separator()
commandsmenu.add_command(label="Back (Ctrl+z)")
commandsmenu.add_command(label="Copy (Ctrl+c)")
commandsmenu.add_command(label="Paste (Ctrl+v)")
commandsmenu.add_command(label="Select all (Ctrl+a)")

##########

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)

def no_help():
    messagebox.showinfo("No Help Here", "lol")
   
helpmenu.add_command(label="NO", command=no_help)

##########

def red():
    messagebox.showinfo("Colour: Red", "Strawberries :/")

def green():
    messagebox.showinfo("Colour: Green", "Kiwis :)")

def green():
    messagebox.showinfo("Colour: Blue", "Blueberries :(")

red = Button(screen, text="RED", fg="white", bg="red", command=red)
red.grid(row=1, column=1)


green = Button(screen, text="GREEN", fg="white", bg="green", command=red)
green.grid(row=1, column=3)

blue = Button(screen, text="BLUE", fg="white", bg="blue", command=red)
blue.grid(row=1, column=5)