from operator import itemgetter

def cel_to_far(mylist):
	c = int(input("Enter the Celsius value : "))
	f = c*(9/5) + 32
	c2f = (c,f)
	mylist.append(c2f)
	print("The Fahrenheit value is ",f)
	return mylist


def far_to_cel(mylist):
	f = int(input("Enter the Fahrenheit value : "))
	c = (f - 32)*(5/9)
	f2c = (f,c)
	mylist.append(f2c)
	print("The Celsius value is ",c)
	return mylist

def kel_to_cel(mylist):
	k = int(input("Enter the Kelvin value :	"))
	c = k - 273
	k2c = (k,c)
	mylist.append(k2c)
	print("The Celsius value is ",c)
	return mylist

def cel_to_kel(mylist):
	c = int(input("Enter the Celsius value :"))
	k = c + 273
	c2k = (c,k)
	mylist.append(c2k)
	print("The Kelvin value is ",k)
	return mylist

mylist = []
loop_var = 0

while loop_var == 0:
	my_input = int(input("""Enter any of the choice below :
		1 To convert Celsius to Fahrenheit
		2 To convert Fahrenheit to Celsius
		3 To convert Kelvin to Celsius
		4 To convert Celsius to Kelvin
		7 To show the records sorted according to "from value"
		8 To show the records sorted according to "to value"
		9 To exit
		"""))

	if my_input == 1:
		mylist = cel_to_far(mylist)

	elif my_input == 2:
		mylist = far_to_cel(mylist)

	elif my_input == 3:
		mylist = kel_to_cel(mylist)

	elif my_input == 4:
		mylist = cel_to_kel(mylist)

	elif my_input == 5:
		print(sorted(mylist, key=itemgetter(0)))

	elif my_input == 6:
		print(sorted(mylist, key=itemgetter(1)))

	else:
		loop_var = 1
