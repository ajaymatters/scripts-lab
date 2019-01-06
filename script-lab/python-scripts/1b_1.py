def read_elements():

	elements = input("Enter space separated values of elements").split()
	
	return elements

def remove_duplicates(mylist):
	# Another implementation :
	# 	from collections import OrderedDict
	#   list(OrderedDict.fromkeys(mylist))
	# list_dup = mylist
	return sorted(list(set(mylist)))

def even_list(n):
	return [x for x in range(1,n*2) if x%2 == 0]

list1 = read_elements()

print(remove_duplicates(list1))

evens = even_list(5)

print(sorted(evens,reverse=True))
