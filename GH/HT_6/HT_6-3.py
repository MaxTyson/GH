'''
	Напишіть програму, де клас «геометричні фігури» (figure) містить властивість 
color з початковим значенням white і метод для зміни кольору фігури, а його
підкласи «овал» (oval) і «квадрат» (square) містять методи __init__ для 
завдання початкових розмірів об'єктів при їх створенні.
	Видозмініть програму так, щоб метод __init__ мався в класі «геометричні 
фігури» та приймав кольор фігури при створенні екземпляру, а методи 
__init__ підкласів доповнювали його та додавали початкові розміри.
'''

class Figure:
	def __init__(self, color):
		self.color = color
		color = 'white'
	def changeColor(self, new_color):
		self.color = new_color

class Oval(Figure):
	def __init__(self, color, size):
		Figure.__init__(self, color)
		self.size = size
	def printOval(self):
		print('Oval is {} and {}.'.format(self.color, self.size))

class Square(Figure):
	def __init__(self, color, size):
		Figure.__init__(self, color)
		self.size = size
	def printSquare(self):
		print('Square is {} and {}.'.format(self.color, self.size))


o = Oval('red', 'big')
o.printOval()
o.changeColor('blue')
print('Oval\'s color changed!')
o.printOval()

s = Square('green', 'small')
s.printSquare()