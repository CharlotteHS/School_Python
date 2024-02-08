from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.geometry("450x450")
screen.title("Tkinter #2")

screen["bg"] = "black"
#background colour
#screen.configure(bg="black")

def show():
    messagebox.showinfo("FACT","You're in school")

fact = Button(screen, text="Fact", fg="white", bg="green", command=show)
fact.place(x=200, y=100)