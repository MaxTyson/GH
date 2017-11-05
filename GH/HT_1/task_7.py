# 7. Write a script to concatenate all elements in a list into a string and print it.

testList = [2, 'k', 17, 'Geek', '_', 'Hub', '+', 'Pyth', 0, 'n']
concatenated = ''
for value in testList:
	concatenated += str(value)
print('Concatenated word is: ',concatenated)