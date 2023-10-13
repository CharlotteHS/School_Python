#superheros

heros = ["Batman", "Wonder Woman", "Superman", "Spiderman"]
#array

print("Current pilot: ",heros[0])
print("Current co-pilot::: ",heros[1])
#printing out roles

heros[2] = ("Hit Girl")
#changing superman to hit girl

heros.append("Iron Man")
heros.append("The Hulk")
#adding more heros

print("Heros currently in the alliance::: ",(heros))

print("Which hero would you like to replace?")
print("Pick a number from 0 to 5")

replace = int(input("::: "))
change = input("Enter the name of your hero::: ")

heros[replace] = (change)
#heros is found using the number and is changed to the input

print("Here is the updated list::: ",(heros))
