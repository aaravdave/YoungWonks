class Dog:
	def __init__(self, name, eye_color, fur_color, breed, age):
		self.name = name
		self.eye_color = eye_color
		self.fur_color = fur_color
		self.breed = breed
		self.age = age
	
	def show_info(self):
		print(f'My dog\'s name is {self.name}, and he/she is a {self.age} year old {self.breed}, with {self.eye_color} eyes and {self.fur_color} colored fur.')

matthew = Dog('Matthew', 'blue', 'yellow', 'golden retriever', 2)
colt = Dog('Colt', 'red', 'black', 'bulldog', 12)
cloudy = Dog('Cloudy', 'green', 'white', 'poodle', 6)

for dog in [matthew, colt, cloudy]:
	dog.show_info()
