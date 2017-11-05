# 6. Write a script to check whether a specified value is contained in a group of values. 
# 		Test Data : 
# 		3 -> [1, 5, 8, 3] : True
# 		-1 -> (1, 5, 8, 3) : False

testData = [1, 5, 8, 3]
print(testData)
number = int(input('Enter a number: '))
for i in testData:
	if i == number:
		print('True, number {} is present in list.'.format(i))
