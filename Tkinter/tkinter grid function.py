from tkinter import *
from tkinter import messagebox
#importing...

screen = Tk()
screen.geometry("400x400")
screen.title("Grid Function Testing")
#basic stuff :]

def dis1():
    messagebox.showinfo("Idiot", "Your already in settings")
settings = Button(screen, text="Settings", command=dis1)
settings.grid(row =1, column=1)
#you cant have this as .place, they clash, idk why yet

def dis2():
    messagebox.showinfo("Audio", "STM codes acoustically")
audio = Button(screen, text="Audio", command=dis2)
audio.grid(row = 2, column = 2)
#diagnal :)

screen.mainloop()