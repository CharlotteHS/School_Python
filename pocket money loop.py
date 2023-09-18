#pocket money

money = 0.01
total = 0
#variables

for week in range(1,27):
    #creates a variable
    #prints out 1 to 26

    print("It's week", week)
    print("You will get £", money)
    total = money + total
    money = money * 2
    #multiplying the money each week

print("Your total at the end of the 26 weeks is", round(total,2))
#using 'round' followed by a number rounds it to that number of decimal places
#printing out the total