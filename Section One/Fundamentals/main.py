# PYTHON FUNDAMENTALS PART 1: 

print("hello world")
print("AI/ML batch \n2.0")

# Variables in Python
print("Variables in Python")
name = "Vanshaj"
age = 23
PI = 3.14
print("My name is: ", name)
print(age)
print(PI)

print(type(name))
print(type(age))
print(type(PI))

print("----------------------------------")

# Operators
print("Operators in Python")
#Arithmetic Operators
print("Arithmetic Operators")
a = 10
b = 5
print(a+b) # 15
print(a-b) # 5
print(a*b) # 50
print(a/b) # 2.0
print(a%b) # 0
print(a**b) # 100000

# Relational Operators
print("Relational Operators")
print(a > b) # True
print(a >= b) # True
print(b <= a) # True
print(a == b) # False
print(a!=b) # True

# Assignment Operators
print("Assignment Operators")
c = 2
c+= 2
print(c) # 4
d = 10
d *= 2
print(d) # 20
d -= 5
print(d) # 15
c%= 2
print(c) # 0

# Logical Operators
print("Logical Operators")
#not , and, or
#Using not
print(not (5 >8)) # True
val = False
print(not val) # True
print(not (4 < 8)) # False
#Using and 
print((5 > 8) and (9 > 8)) # False
print((4 >3) and (7 > 5)) # True
#Using or
print((4 >3) or (7 >9)) # True
print((4> 5) or (5>7)) # False

print("----------------------------------")

# Type conversion and Type Casting
print("Type Conversion and Type Casting")
ans1 = int(10 + 9.0)
ans2 = 5 + 10.0
print(ans1, type(ans1)) # 19 <class 'int'>
print(ans2, type(ans2)) # 15.0 <class 'float'>

test_one = bool(0)
print(test_one, type(test_one)) # False <class 'bool'>
test = bool(10) # Except 0 in boolean everything is True
print(test, type(test)) # True <class 'bool'>

# Taking User Input
user1 = int(input("Enter user1 id: "))
print(user1)
user2 = int(input("Enter user2 id: "))
print(user2)

# Average of two numbers
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
avg = (num1+num2)/2
print("Average is: ", avg)

print("----------------------------------")