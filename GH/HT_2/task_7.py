def calc(num1, oper, num2):
	# standart calculator
	oper = str(oper)
	if oper == '+':
		return sum(num1, num2)
	elif oper == '-':
		return (num1 - num2)
	elif oper == '*':
		return (num1 * num2)
	elif oper == '/':
		return (num1 / num2)
	else:
		return False
# example
print('Result: ', calc(11, '/', 29))