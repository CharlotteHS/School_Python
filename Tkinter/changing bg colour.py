from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.geometry("450x450")
screen.title("Tkinter #2")

screen["bg"] = "black"
#background colour
#screen.configure(bg="black")

def true():
    messagebox.showinfo("FACT","You're on a computer")

fact = Button(screen, text="Fact", fg="white", bg="green", command=true)
fact.place(x=200, y=100)

###

def otoh():
    #on the other hand
    messagebox.showinfo("or","nothing to see here")

fact = Button(screen, text="or", fg="white", bg="black", command=otoh)
fact.place(x=205, y=130)

###

def false():
    messagebox.showinfo("FAKE","We're in America")

fact = Button(screen, text="Fake", fg="white", bg="red", command=false)
fact.place(x=200, y=160)

screen.mainloop()