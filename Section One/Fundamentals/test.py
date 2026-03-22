print("hello world")
print("AI/ML batch \n2.0")

# Variables in Python
name = "Vanshaj"
age = 23
PI = 3.14
print("My name is: ", name)
print(age)
print(PI)

print(type(name))
print(type(age))
print(type(PI))

# Operators
#Arithmetic Operators
a = 10
b = 5
print(a+b) # 15
print(a-b) # 5
print(a*b) # 50
print(a/b) # 2.0
print(a%b) # 0
print(a**b) # 100000

# Relational Operators
print(a > b) # True
print(a >= b) # True
print(b <= a) # True
print(a == b) # False
print(a!=b) # True

# Assignment Operators
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