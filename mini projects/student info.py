#Geraldine school code


while True:

    username = input("Enter your username here: ")
    if username == "SwanT":
        password = input("Enter your password here: ")
        #constants

        if password == "placeholder":
            print("Correct")
            break

        else:
            print("Incorrect, please try again")


print("""
      (A) Student Information
      (B)Log out
      """)
optA = input("Enter: ")
if optA == "A" or "a":
    print("Entering Student Menu")

def Smenu():
    s1 = str["id no.", "name", "sirname", "dob", "home address", "hone phone", "gender", "tutor group", "email" ]