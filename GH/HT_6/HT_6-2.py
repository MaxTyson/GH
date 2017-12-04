'''
	Створити клас Person, в якому буде присутнім метод __init__ який буде 
приймати * аргументів, які зберігатиме в відповідні змінні. Методи, 
які повинні бути в класі Person - show_age, print_name, show_all_information.
	Створіть 2 екземпляри класу Person та в кожному з екземплярів 
створіть атребут profession.
'''

class Person:
	''' Make class to printing some person's information '''
	def __init__(self, name, age, *args):
		''' initialisation pesrons '''
		self.name = name
		self.age = age
		
	def print_name(self):
		''' printing person's name '''
		print('Person\'s name is {}.'.format(self.name))

	def show_age(self):
		''' printing person's age '''
		print('Person\'s age is {}.'.format(self.age))

	def show_all_information(self):
		''' printing all person's info '''
		print('{}\'s age is {}, profession - {}.\n'.format(self.name, \
		self.age, self.profession))
		
# make some persons for example
author = Person(name = 'Maxim', age = 25)
poroh = Person(name = 'Petia', age = 53)

# add professions for persons
author.profession = 'Programmer'
poroh.profession = 'President'

# examples
author.print_name()
author.show_age()
author.show_all_information()
poroh.print_name()
poroh.show_age()
poroh.show_all_information()