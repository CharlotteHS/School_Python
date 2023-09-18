#if statement challenge

wrong = ['i', 'c']
#created list for lower case

print("Please write your answers in ALL CAPS")
print("Write 'I' for an insult and 'C' for a complement")
#statements telling the user what to do

choice = input("Choose an insult or a compliment::: ")
#input

if choice == "I":
    print("You're ugly")
elif choice == "C":
    print("You look really good today :)")
#using if and elif statements for multiple options
    
elif choice in wrong:
    print("Your input isnt upper case, learn to read")
#using 'in' refers back to the list to check if its lower case

else:
    print("You've done something wrong")
#if you haven't used a lower case or upper case 'c' or 'i'
