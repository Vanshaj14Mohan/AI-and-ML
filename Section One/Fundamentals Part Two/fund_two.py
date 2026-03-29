# Conditional Statements in Python: 
color = str(input("Enter the color: "))

if color == "Red":
    print("Stop")
elif color == "Yellow":
    print("Look")
elif color == "Green":
    print("Go")
else:
    print("Wrong color entered")

age = int(input("Enter the age: "))

if (age < 13):
    print("A child")
elif (age >= 13 and age <18):
    print("A teenager")
else:
    print("An adult")

username = input("Enter Username: ")
password = input("Enter Password: ")

if(username == "Admin" and password == "Admin@1234"):
    print("Welcome User")
elif (username != "Admin"):
    print("Incorrect username")
else:
    print("Wrong Password")

# Check if number n is multiple of 5 or not
n = 5
if(n %5 == 0):
    print("Multiple of 5")
else:
    print("Not a multiple of 5")
