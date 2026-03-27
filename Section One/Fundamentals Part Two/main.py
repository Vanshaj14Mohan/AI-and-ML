# Conditional Statements: 
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