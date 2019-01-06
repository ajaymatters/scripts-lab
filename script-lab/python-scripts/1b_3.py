def recursive_max(mylist):
	if len(mylist) == 1:
		return mylist[0]
	else:
		m = recursive_max(mylist[1:])
		return m if m > mylist[0] else mylist[0]