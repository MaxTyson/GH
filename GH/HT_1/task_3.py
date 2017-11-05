# 3. Write a script to sum of the first n positive integers.

examleList = [-2, -100, 4.3, -3, 10, 20, 3, -1, 0, 55.5, 12]
global_n = int(input('Input quantity of positive numbers, n = '))
n = global_n
result = 0

def isInt(number):
	# function checks a number for integrity
	if type(number) is int:
		return True
	else:
		return False

for number in examleList:
	if number >= 0 and isInt(number) == True:
		result += number
		n -= 1
		if n <= 0:
			break

print('Sum of the first {} positive integers is {}.'.format(global_n, result))