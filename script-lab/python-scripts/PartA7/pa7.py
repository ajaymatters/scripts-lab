def AtomicDictionary():
	atomic = {"H":"Hydrogen", "He":"Helium", "N":"Nitrogen"};

	x = input("Enter symbol ")
	y = input("Enter element name ")

	if x in atomic.keys():
		print("Key already exists. Value will be updated")
	else:
		print("New Key with Value added")

	atomic[x] = y

	print(atomic)

	print("Number of elements in dict:",len(atomic))

	x = input("Enter symbol for searching ")
	if x in atomic.keys():
		print("Element exists in dict with value "+ atomic[x])
	else:
		print("Element not present in dict")