
# *******************************  id() function in python *********************************************** #

# Immutablility

x = 45

print(type(x) , id(x))

x = 12.23

print(type(x) , id(x))

x = 43.21

print(type(x) , id(x))

# *******************************  type() function in python *********************************************** #

# Immutablility

x = 45
a = 45
b = 45
c = 45

print(type(x) , id(x))
print(type(a) , id(a))
print(type(b) , id(b))
print(type(c) , id(c))

b = 12

print(type(x) , id(x))
print(type(a) , id(a))
print(type(b) , id(b))
print(type(c) , id(c))


# *******************************  type casting in python  *********************************************** #

# int() 
x = int(input("Number : ")) # str
y = int(input("Number : "))

z = x + y

print(z)

# float()
x = float(input("Number : ")) # str
y = float(input("Number : "))

z = x + y

print(z)


# *******************************  Logical and relational operator in python *********************************************** #

# Relational < <= > >= == !=
# Logical and , or , not

x = 45

y = 35

a = x<100 or y>100 # True/False
print(a)


# *******************************  arithmatic operator in python *********************************************** #

x = 45

print(x)

x += 1

print(x)

x +=34

print(x)

x -= 12

print(x)

x **=12

print(x)


# Membership Operator  in , not in
# Identity Operator   is , is not


# *******************************  use of operator in print in python *********************************************** #

print("Indore\n"*10) # Indore Indore Indore Indore Indore Indore Indore Indore ..........

abc = "Ujjain"*5

print(abc)

# *******************************  str() function in python *********************************************** #

# concate

x = 34

y = "Raj "

z = str(x) + y

print(z)

# *******************************  if statement in python *********************************************** #

# Decision Making Statements
	# IF Statement

x = 450

print("Good Evening !!! ")

if x>100:
	print("Hello Student !")
	print("Hi  !")

print("Thanks !!! ")





				
