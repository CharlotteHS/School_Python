#website sign in
from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.title("Website Sign up")
screen.geometry("400x400")

menubar = Menu(screen)
screen.config(menu=menubar)
help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)


app = Frame(screen)
app.grid()
    #setting a grid the size of the screens frame

name = Label(screen, text="Name:")
name.grid(row=0, column=0)
input_one = Text(width=20, height=1)
input_one.grid(row=0, column=1, padx=10, pady=4)

last = Label(screen, text="Surname:")
last.grid(row=1, column=0)
input_one = Text(width=20, height=1)
input_one.grid(row=1, column=1, padx=10, pady=4)

age = Label(screen, text="Age:")
    #can try and get a toggle to pick the day, month, and year
age.grid(row=2, column=0)
input_one = Text(width=20, height=1)
input_one.grid(row=2, column=1, padx=10, pady=4)

def cont():
    messagebox.showinfo("Loading...", "Signing in")

sign_in = Button(screen, text="Sign In", command=cont)
sign_in.grid(row=3, column=1, padx=0, pady=5)

screen.mainloop()