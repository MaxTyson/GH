'''
	Створити пустий клас, який називається Thing. Потім створіть об'єкт 
example цього класу. Виведіть типи зазначених об'єктів.
	Створіть новий клас Thing2 і призначте йому атрибут letters зі значенням 
'abc' . Виведіть на екран значення атрибута letters.
	Створіть ще один клас Thing3 . Присвойте значення 'xyz' атрибуту об'єкта, 
який називається letters. Виведіть на екран значення атрибута letters . 
	Створіть клас, який називається DefaultClass що має атрибути об'єкту name, 
symbol number . Виведіть атребути.
	Створіть словник з наступними ключами і значеннями: 'name': 'Vasya', 
'l_name': 'Pupkin', 'age': 20 . Далі створіть об'єкт з ім'ям user класу 
DefaultClass1за допомогою цього словника.
	Для класу DefaultClass1 визначте метод з ім'ям print_info() , що виводить 
на екран значення атрибутів об'єкта (name , l_name та age ).
'''

''' Step №1 '''
class Thing:
	pass
first = Thing()
print('Step №1: object type is - ', type(first))

''' Step №2 '''
class Thing2:
	leters = 'abc'
second = Thing2()
print('Step №2: leters = ', second.leters)

''' Step №3 '''
class Thing3:
	leters = 'xyz'
third = Thing3()
print('Step №3: leters = ', third.leters)

''' Step №4 '''
class DefaultClass:
	name = 'Python'
	symbol = '№'
	number = 1
	print('Step №4: (name, symbol and number)', name, symbol, number)
fours = DefaultClass()

''' Step №5-6 '''
defaultDict = {
	'name' : 'Vasia',
	'l_name' : 'Pupkin',
	'age' : 20
}
class DefaultClass1:
	def __init__(self, name, l_name, age):
		self.name = name
		self.l_name = l_name
		self.age = age
	def print_info(self):
		print('Step №5-6: Name - {}, l_name - {}, age - {}'.format(self.name, self.l_name, self.age))

user = DefaultClass1(defaultDict['name'], defaultDict['l_name'], defaultDict['age'])
user.print_info()

''' Step №7 '''
class Person:
	def __init__(self, name, l_name):
		self.name = name
		self.l_name = l_name
class Junior(Person):
	exp = 0
	def print_info(self):
		print('Programmer: {} {}, experience time is {} years.'.format(self.name, self.l_name, self.exp))
class Programmer(Junior):
	exp = 2
	
print('Step №7: ')
prog = Programmer('Maxim', 'Nazarenko')
prog.print_info()