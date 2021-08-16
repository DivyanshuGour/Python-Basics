# ****************************  Normal If statemnet in python ******************************* #

print("** Voting Program **")

age = int(input("Your Age : "))

if age>=18:
	print("You Can Give vote !")
	print("Go Your Nearest Center !")

print("** Thanks **")

# ****************************  Normal If Else statemnet in python ******************************* #

print("** Voting Program **")

age = int(input("Your Age : "))

if age>=18: # True block
	print("You Can Give vote !")
	print("Go Your Nearest Center !")	
else: # False Block
	print("You Can Not Give Vote !")
	print("Try Next Time !")

print("** Thanks **")


# ****************************  Nested If Else statemnet in python ******************************* #

print("** Voting Program **")

nat = input("Are You Indian (Y/N) : ")

if nat=='y' or nat=='Y':
	age = int(input("Your Age : "))
	if age>=18: # True block
		print("You Can Give vote !")
		print("Go Your Nearest Center !")	
	else: # False Block
		print("You Can Not Give Vote !")
		print("Try Next Time !")
else:	
	if nat=='n' or 	nat=='N':
		print("Not Allowed, Go Your Country !")
	else:
		print("Wrong Input !")		

print("** Thanks **")



# ****************************  Elif statemnet in python ******************************* #

wd = int(input("WeekDay : ")) # 12

if wd<1 or wd>7:
	print("\tWrong WD")
elif wd==1:
	print("\tMonday")
elif wd==2:
	print("\tTuesday")
elif wd==3:
	print("\tWednesday")
elif wd==4:
	print("\tThursday")
elif wd==5:					
	print("\tFriday")
elif wd==6:
	print("\tSaturday")
else:							
	print("\tSunday")						
	

# ****************************  Simple While loop in python ******************************* #

print("Start .... ")

x = 1
while x<11:
	print("\tIndore .....")
	x+=1


print("End .... ")



# ****************************  While with Else in python ******************************* #

print("Start .... ")

x = 1
while x<11:
	print("\tIndore .....")
	if x==5:
		break	
	x+=1
else:
	print("\tELSE....")	


print("End .... ")

