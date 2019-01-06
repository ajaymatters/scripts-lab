import functools

my_list = [1,2,3,4,5,6]

new_list = [x*3 for x in my_list]

print(my_list)
print(new_list)

print("Sum of original list:",functools.reduce(lambda x,y : x+y,my_list))
print("Sum of new list:",functools.reduce(lambda x,y : x+y,new_list))