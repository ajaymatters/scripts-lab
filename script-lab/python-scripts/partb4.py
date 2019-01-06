from collections import Counter
from functools import reduce
import operator

with open('abc.txt') as f:
	wordcount = Counter(f.read().lower().split())

for key,value in wordcount.items():
	print(key,value)

print(wordcount.most_common(10))

y = []
for x in wordcount.most_common(10):
	y.append(len(x[0]))
	print(len(x[0]))

print("Average length of words:",reduce(operator.add,y)/len(y))

print("Square of odd length words:", [x**2 for x in y if x%2 == 1])
