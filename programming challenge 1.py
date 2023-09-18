#Programming Challenges

print("Welcome to the meal price splitter")
#welcome message

people_value = int(input("How many people need to pay? ::: "))
bill_value = float(input("How much was the bill? ::: "))
#stating the variables that the user will input
#each value has been cast

price_each = str(bill_value / people_value)
#changing both variables into a string so they can be put together and divided

print("Each person should pay: £" + price_each)
#printing out the result of dividing the two variables