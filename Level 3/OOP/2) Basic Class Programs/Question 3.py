Dog = __import__('Question 2').Dog

class Person:
	def __init__(self, name, age, petlist):
		self.name = name
		self.age = age
		self.petlist = petlist
	
	def show_petlist(self):
		for pet in self.petlist:
			print(pet.name)
	
	def add_pet(self, pet):
		self.petlist.append(pet)

matthew = Dog('Matthew', 'blue', 'yellow', 'golden retriever', 2)
colt = Dog('Colt', 'red', 'black', 'bulldog', 12)
cloudy = Dog('Cloudy', 'green', 'white', 'poodle', 6)

jim = Person('Jim Hori', 93, [matthew])
jim.show_petlist()

xi = Person('Xi Jhu', 27, [cloudy])
xi.add_pet(colt)
xi.show_petlist()
