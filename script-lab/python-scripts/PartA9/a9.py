class Student():
	"""docstring for Student"""
	name = ""
	age = 0
	marks_list = []

	def __init__(self, name, age, marks_list):
		self.name = name
		self.age = age
		self.marks_list = marks_list
		
	def accept():
		name = input("Enter name: ")
		age = int(input("Enter age: "))
		l = input("Enter marks")
		l = l.split(" ")
		marks_list = list(map(int, l))
		return Student(name,age,marks_list)

	def display(self):
		print("Name:",self.name)
		print("Age:",self.age)
		print("Marks list:",self.marks_list)

s1 = Student("ajay",44,[53,55,66])
s1.display()

s3 = Student.accept()
s3.display()