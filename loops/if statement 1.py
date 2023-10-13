#if statement challenges

needed = (20)
piggy_bank = (10.50)
#labelled the constants

extra = float(input("How much extra money do you have? ::: £"))
#the input is labelled as a float because its money

total = piggy_bank + extra
#the total is found by combining the constant and the users input

#prints out the correct statement depending on if the users total is in the range
if total >= needed:
    print("We have enough! :)")
else:
    print("Sorry, we need more :(")

