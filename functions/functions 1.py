#Functions

import time as datetime
programs = ["Coronation Street","Eastenders","Emmerdale","Hollyoaks"]
times = ["20:00","19:30","19:00","18:30"]
#lists

#time function
def display_time():
    print("========================================")
    print("Welcome to the TV Listings Program")
    print("Today's date:",datetime.strftime("%x"))
    print("Current time:",datetime.strftime("%X"))
    print("========================================")

#display function
def display_program():
    print()
    print(program,"is on tomorrow at",time)
    print("Press 'Enter' to get the next program")
    input()
    print()


for tv in range(4):
    #created a loop to reduce amount of code needed
    #created a variable (tv) which automatically starts at 0 and increases with each loop
    display_time()
    program = programs[tv]
    time = times[tv]
    display_program()

#Finish
input("Press enter to close this program")
