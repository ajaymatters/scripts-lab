mylist = []

def celsius_to_fahrenheit():
	celsius = int(input("Enter the celsius value"))
	fahrenheit = celsius*(9/5) + 32;
	print("Celsius : {0} Fahrenheit : {1}".format(celsius,fahrenheit))
	mylist.append((celsius,fahrenheit))

def celsius_to_kelvin():
	celsius = int(input("Enter the celsius value"))
	kelvin = celsius + 273;
	print("Celsius : {0} Kelvin : {1}".format(celsius,kelvin))
	mylist.append((celsius,kelvin))

def fahrenheit_to_celsius():
	fahrenheit = int(input("Enter the fahrenheit value"))
	celsius = (fahrenheit - 32)*(5/9);
	print("Fahrenheit : {0} Celsius : {1}".format(fahrenheit,celsius))
	mylist.append((fahrenheit,celsius))

def fahrenheit_to_kelvin():
	fahrenheit = int(input("Enter the fahrenheit value"))
	kelvin = (fahrenheit + 459.67)*(5/9) ;
	print("Fahrenheit : {0} Kelvin : {1}".format(fahrenheit,kelvin))
	mylist.append((fahrenheit,kelvin))

def kelvin_to_celsius():
	kelvin = int(input("Enter the kelvin value"))
	celsius = kelvin - 273;
	print("Kelvin : {0} Celsius : {1}".format(kelvin,celsius))
	mylist.append((kelvin,celsius))

def kelvin_to_fahrenheit():
	kelvin = int(input("Enter the kelvin value"))
	fahrenheit = (kelvin)*(9/5) - 459.67;
	print("Kelvin : {0} Fahrenheit : {1}".format(kelvin,fahrenheit))
	mylist.append((kelvin,fahrenheit))


choice = 1

while choice:	
	scale_choice = int(input(""" \n Enter a choice
		1.Celsius to Fahrenheit
		2.Celsius to Kelvin
		3.Fahrenheit to Celsius
		4.Fahrenheit to Kelvin
		5.Kelvin to Celsius
		6.Kelvin to Fahrenheit
		7.Sort by 'from' values
		8.Sort by 'to' values
		9.Exit"""))
	if scale_choice == 1:
		celsius_to_fahrenheit()
	elif scale_choice == 2:
		celsius_to_kelvin()
	elif scale_choice == 3:
		fahrenheit_to_celsius()
	elif scale_choice == 4:
		fahrenheit_to_kelvin()
	elif scale_choice == 5:
		kelvin_to_celsius()
	elif scale_choice == 6:
		kelvin_to_fahrenheit()
	elif scale_choice == 7:
		print(sorted(mylist,key = lambda x: x[0]))
	elif scale_choice == 8:
		print(sorted(mylist,key = lambda x: x[1]))
	else:
		choice = 0