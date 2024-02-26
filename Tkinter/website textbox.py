#website sign in
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

screen = Tk()
screen.title("Website Sign up")
screen.geometry("400x400")

menubar = Menu(screen)
screen.config(menu=menubar)
help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)

def Q():
    messagebox.showinfo("Loading... :)", "nvm idk/idc")

def death():
    screen.destroy()

help_menu.add_command(label="Help", command=Q)
help_menu.add_separator()
help_menu.add_command(label="Exit", command=death)



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

days = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", 
        "15", "16", "17", "17", "18", "19", "20", "21", "22", "23", "24", "25", 
        "26", "27", "28", "29", "30", "31"]
months =["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
years = ["2012", "2011", "2010", "2009", "2008", "2007", "2006","2005"]

age = Label(screen, text="Age:")
age.grid(row=2, column=0)

d_age = ttk.Combobox(screen, values = days)
#creates a togglebox which can select the variables from your list
d_age.set("Day:")
d_age.grid(row=2, column=1, padx=1, pady=1)
#
m_age = ttk.Combobox(screen, values = months)
m_age.set("Month:")
m_age.grid(row=3, column=1, padx=1, pady=1)
#
y_age = ttk.Combobox(screen, values = years)
y_age.set("Year:")
y_age.grid(row=4, column=1, padx=1, pady=1)


tos = IntVar()
consent = IntVar()
    #creating the variables
#this allows you to tick of multiple things
tickbox1 = Checkbutton(screen, text="ToS", width = 30, variable = tos)
tickbox1.grid(row=5, column=1, padx=1, pady=1)

tickbox2 = Checkbutton(screen, text="Consent to save this information?", width = 30, variable = consent)
tickbox2.grid(row=6, column=1, padx=1, pady=1)

def cont():
    #continue
    messagebox.showinfo("Loading...", "Signing in")

sign_in = Button(screen, text="Sign In", command=cont)
sign_in.grid(row=7, column=1, padx=1, pady=5)

news = Label(screen, text="Would you like to recieve our newsletters?")
news.grid(row=8, column=1, padx=1, pady=1)
    #Creating a little heading thing

news = StringVar()
#you can only tick one option + they're circles not squares
circle_tickbox = Radiobutton(screen, text="Yes", variable = news, value=1)
circle_tickbox.grid(row=9, column=1, padx=1, pady=1)

circle_tickbox2 = Radiobutton(screen, text="No", variable = news, value=2)
circle_tickbox2.grid(row=10, column=1, padx=1, pady=1)
#
#
#
#For some reason when you first open the screen both radio buttons are selected, dunno how to fix if fixable

screen.mainloop()