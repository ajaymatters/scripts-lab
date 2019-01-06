class Sentence_recursive:
	def __init__(self, sentence):
		self.vowel_count = sum([1 if letter.lower() in ['a','e','i','o','u'] else 0 for letter in sentence])
		self.rev = ' '.join(list(reversed(sentence.split())))
		# mylist = sentence.split()
		# mylist = mylist.reverse()
		# rev_sentence = ' '.join(mylist)


s1 = Sentence_recursive(input("Write the first sentence"))
s2 = Sentence_recursive(input("Write the 2nd sentence"))
s3 = Sentence_recursive(input("Write the 3rd sentence"))

print(sorted([(c.rev,c.vowel_count) for c in [s1,s2,s3]], key=lambda s:s[1], reverse=True))
