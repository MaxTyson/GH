# 4. Write a script to concatenate N strings.

n = int(input('Input quantity of strings numbers, n = '))
strings = ''

while n > 0:
	strings += (input('Enter string ({} pcs left): '.format(n)))
	n -= 1
print('You strings was concatenated: {}'.format(strings))