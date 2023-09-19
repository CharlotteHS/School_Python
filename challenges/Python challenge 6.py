#python challenge 6

values = ["respect", "excellence", "friendship"]

print("Please type in all lowercase")
name = input("Enter one olympic value here::: ")

if name in values:
    print("You are correct")

else:
    print("That was incorrect")
    again = input("Try again::: ")

    if again in values:
        print("You are correct")

    else:
        print("You are incorrect")