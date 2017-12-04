'''Створити клас Calc, який буде мати атребут last_result та 4 методи. 
Методи повинні виконувати математичні операції з 2-ма числами, 
а саме додавання, віднімання, множення, ділення.
Якщо під час створення екземпляру класу звернутися до атребута 
last_result він повинен повернути пусте значення
Якщо використати один з методів - last_result повенен повернути 
результат виконання попереднього методу.
Додати документування в клас''' 

class Calc:
    ''' Class to create elemantary calculator '''
    last_result = 0
    def calcSum(self, x, y):
        ''' method prints summ of 2 numbers '''
        self.last_result = x + y
        print('{} + {} = {}'.format(x, y, self.last_result))

    def calcMinus(self, x, y):
        ''' method prints subtraction of 2 numbers '''
        self.last_result = x - y
        print('{} - {} = {}'.format(x, y, self.last_result))

    def calcMultiplication(self, x, y):
        ''' method prints multiplication of 2 numbers '''
        self.last_result = x * y
        print('{} * {} = {}'.format(x, y, self.last_result))

    def calcDivision(self, x, y):
        ''' method prints division of 2 numbers '''
        self.last_result = x / y
        print('{} / {} = {}'.format(x, y, self.last_result))

''' make c - instance of a class Calc '''
c = Calc()

''' Examples '''
print(c.last_result)
c.calcSum(2,3)
c.calcMinus(10, 6)
c.calcMultiplication(4, 30)
c.calcDivision(10, 5)