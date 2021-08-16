# ************************** Nested While Loop In Python ********************************** #

x=1
while x<6:
	y=1
	while y<=x:
		print("*",end=' ')
		y+=1
	print("")		
	x+=1

########### this program can be written as

x=1
while x<6:	
	print("* "*x)		
	x+=1

# ************************** chr() & ord() funxtion in python In Python ********************************** #

a = chr(65)
print(a)

b = ord(a)
print(b)

# ************************** Functions In Python ********************************** #

def fun1():
	print("Fun 1....")
	print("Good Evening !")

def add(a,b):
	c = a + b
	print("Result : " , c)
	
def mul(a,b):
	c = a * b
	return c

fun1()	

add(34,12)
add(2.3,3.4)
add(12,34.34)

c = mul(2,9)
z = c * 10
print("Z : ",z)


# ************************** Function with default argumnet In Python ********************************** #

# python not support to function overloading

# default argument
def add(a , b , c=5 , d=1):
	print(a,b,c,d)
	z = a + b + c + d
	print("Z : ",z)
	
add(2,5,4,6)	

add(6,5,9)

add(23,12)

add(3)

#########################

# default argument
def add(a , b , c=5 , d=1):
	print(a,b,c,d)
	z = a + b + c + d
	print("Z : ",z)

# named / keyword argument
add(6,5,d=9) # a=6,b=5,d=9
add(d=3,a=4,c=1,b=7)

add(7,4,d=3,c=1)


# ************************** Function with return In Python ********************************** #

def mul(a,b):
	c = a * b
	if c>100:
		return c
	else:
		return 'indore'
		
a = mul(12,45)				
print(a)

a = mul(2,7)
print(a)

############ function returns None object by default

def mul(a,b):
	c = a * b
	if c>100:
		return c
		
a = mul(12,45)				
print(a)

a = mul(2,7)
print(type(a))

z = None


# **************************  Check object is None or not In Python ********************************** #

def mul(a,b):
	c = a * b
	if c>100:
		return c
		
a = mul(2,4)				
#if a==None:
#if id(a)==id(None):
if a is None: ###   membership operator in python
	print("No Return Value !")
else:	
	print(a)






