class State:
	def __init__(self, name, capital_city, population):
		self.name = name
		self.capital_city = capital_city
		self.population = population
	
	def show_info(self):
		print(f'Capital City: {self.capital_city}, Population: {self.population}')

georgia = State('Georgia', 'Atlanta', 10060000)
florida = State('Florida', 'Tallahassee', 20270000)
california = State('California', 'Sacremento', 37250000)
massachusetts = State('Massachusetts', 'Boston', 6540000)
texas = State('Texas', 'Austin', 28990000)

states = [georgia, florida, california, massachusetts, texas]
ask = input('What state do you want? ').title()
for state in states:
	if ask == state.name:
		state.show_info()
		break
else:
	print('State not found. Check what you have searched.')
