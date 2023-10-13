#Geraldine school code


while True:

    username = input("Enter your username here: ")
    if username == "Tswan":
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

def Sinput():
    #s1 = str["id no.", "name", "sirname", "dob", "home address", 
    # "home phone", "gender", "tutor group", "email" ]

    print("Please enter the students information")
    Id = input("ID: ")
    name = input("Firstname: ")
    last = input("Lastname: ")
    dob = input("d.o.b: ")
    address = input("Home Address: ")
    phone = input("Home Phone: ")
    gender = input("Gender: ")
    group = input("Form Group: ")
    email = input("School Email: ")

s1 = []
s2 = []
s3 = []
s4 = []

Sinput()

print("Currently adding student info")
s1.append(Sinput) 

print("Student 1's information: ",(s1))