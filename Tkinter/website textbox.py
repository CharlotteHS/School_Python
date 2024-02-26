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

tos = IntVar()
consent = IntVar()
    #creating the variables
tickbox1 = Checkbutton(screen, text="ToS", width = 30, variable = tos)
tickbox1.grid(row=3, column=1, padx=1, pady=1)
    #
tickbox2 = Checkbutton(screen, text="Consent to save this information?", width = 30, variable = consent)
tickbox2.grid(row=4, column=1, padx=1, pady=1)

def cont():
    messagebox.showinfo("Loading...", "Signing in")

sign_in = Button(screen, text="Sign In", command=cont)
sign_in.grid(row=5, column=1, padx=1, pady=5)

news = Label(screen, text="Would you like to recieve our newsletters?")
news.grid(row=6, column=1, padx=1, pady=1)
    #Creating a little heading thing

news = StringVar()
circle_tickbox = Radiobutton(screen, text="Yes", variable = news, value=1)
circle_tickbox.grid(row=7, column=1, padx=1, pady=1)

circle_tickbox2 = Radiobutton(screen, text="No", variable = news, value=2)
circle_tickbox2.grid(row=8, column=1, padx=1, pady=1)


screen.mainloop()