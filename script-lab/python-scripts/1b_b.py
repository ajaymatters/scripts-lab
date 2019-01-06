
words = dict()

with open('abc.txt') as f:
	# read_data = f.read()
	for word in (word for line in f for word in line.split()):
		if word in words:
			words[word] += 1
		else:
			words[word] = 1

words = dict(sorted(words.items(), key=lambda x:x[1], reverse=True))

for k,v in words.items():
	print(k,v)


