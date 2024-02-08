from tkinter import *
from tkinter import messagebox
#using the tkinter programming library

screen = Tk()
#using the tkinter module to set up a window
screen.geometry("450x450")
#sets dimensions
screen.title("Tkinter #1")
#appears at the top

button1 = Button(screen,text="Dont Click Me")
button1.pack(fill=X)
#makes a button at the to of the screen that stay there
#it takes up the entire top portion

b2 = Button(screen,text="Red ")
#creates a button which is labelled 'Red'
b2.place(x=200, y=100)
#the coordinates of the buttons

b3 = Button(screen,text="Green")
b3.place(x=197, y=130)

b4 = Button(screen,text="Blue")
b4.place(x=200, y=160)


def display_message():
    messagebox.showinfo(":)","Surprise!!")
    #title = ':)', message = 'Suprise!!'
    #if the button is pressed he procedure will run

b5 = Button(screen,text="Click me",command=display_message)
b5.place(x=189, y=200)

screen.mainloop()
#needed to run on the screen