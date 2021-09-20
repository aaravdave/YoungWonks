class Phonebook:
	def __init__(self):
		self.people = {}
	
	def add_person(self, person, phone_number):
		self.people[person] = phone_number
	
	def remove_person(self, person):
		if person in self.people and input('Confirm deletion (y/n): ').lower() == 'y':
			self.people.pop(person)
	
	def display_person(self, person):
		if person in self.people:
			print(f'{person}: {self.people[person]}')
		else:
			print('Phone number not found.')

phonebook = Phonebook()

phonebook.add_person('John', '111-111-1111')
phonebook.add_person('Pi', '314-159-2653')
phonebook.add_person('Bill', '123-123-1234')
phonebook.remove_person('John')

phonebook.display_person('John')
phonebook.display_person('Pi')
phonebook.display_person('Bill')
