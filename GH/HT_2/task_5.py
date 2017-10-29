import re
regex = re.compile(r'[a-zA-Z]')
string = 'jhsjfdh,b43g53h4AAdf76dfhnasd899sdf-ds=z$x7&J5bgvh-bg)b3'

def str_diagnostic(some_str):
	# function diagnostics eny string for nubmers, symbols and characters
	sum_num = 0; all_sym = ''; all_char = ''; all_num = ''; 
	length = len(some_str); numbers = 0; symbols = 0; characters = 0;
	# finding all symbols and use it
	for i in some_str:		
		if i.isdigit():
			numbers += 1
			sum_num += int(i)
			all_num += str(i)
		elif regex.search(i):
			symbols += 1
			all_sym += str(i)
		else:
			characters += 1
			all_char += str(i)
	# do tasks
	if length >= 30 and length <= 50:
		print('Length = {}, where {} symbols and {} numbers.'.format(length, symbols, numbers))
	elif length < 30:
		print('Length = {}. Summ of all numbers is {}, all symbols: {}'.format(length, sum_num, all_sym))
	elif length > 50:
		print('Length = {}. Symbols: {}, Numbers: {}, Characters: {}'.format(length, all_sym, all_num, all_char))
	else: 
		print('Hello, GeekHub!')
	return(length, symbols, numbers, characters)

# use function
str_diagnostic(string)