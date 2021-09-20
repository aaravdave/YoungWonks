class Zoo:
	def __init__(self, name):
		self.name = name
		self.population = {}
		self.food = {}
		self.habitat = {}
		self.animals = {}
	
	def add_animal(self, name, population, food, habitat):
		self.population[name] = population
		self.food[name] = food
		self.habitat[name] = habitat
		self.animals[name] = name
	
	def remove_animal(self, animal):
		if animal in self.animals:
			self.population.pop(animal)
			self.food.pop(animal)
			self.habitat.pop(animal)
			self.animals.pop(animal)
	
	def display_animals(self):
		for animal in self.animals:
			print(f'{animal}: {self.population[animal]} population, eats {self.food[animal]}, lives {self.habitat[animal]}')

californian_zoo = Zoo('Californian Zoo')
californian_zoo.add_animal('Lions', 4, 'meat', 'on land')
californian_zoo.display_animals()

new_york_zoo = Zoo('New York Zoo')
new_york_zoo.add_animal('Dolphins', 6, 'fish', 'in water')
new_york_zoo.add_animal('Ravens', 3, 'seeds', 'in air')
new_york_zoo.add_animal('Dinosaurs', 1, 'meat', 'on land')
new_york_zoo.remove_animal('Dinosaurs')
new_york_zoo.display_animals()
