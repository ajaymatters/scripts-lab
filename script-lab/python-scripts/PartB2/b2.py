class Sentence_reverse():
	"""docstring for Sentence_reverse"""
	def __init__(self, sentence):
		self.vowel_count = sum([1 if letter.lower() in ['a','e','u','i','o'] else 0 for letter in sentence])
		self.sentence = ' '.join(reversed(sentence.split()))


s1 = Sentence_reverse(input("Enter the sentence: "))
s2 = Sentence_reverse(input("Enter the sentence: "))
s3 = Sentence_reverse(input("Enter the sentence: "))

print(sorted([(c.vowel_count,c.sentence) for c in (s1,s2,s3)], key = lambda x:x[0], reverse=True))		