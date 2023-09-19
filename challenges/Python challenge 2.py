#python challenge 2

age = int(input("How old are you? ::: "))
#asks user for age

if age >= 18:
    print("You are able to vote!")

elif age < 18:
    print("You aren't old enough to vote")
#options for age groups

else:
    print("The value you've entered is incorrect")
#error message