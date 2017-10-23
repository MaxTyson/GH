# 1 .Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 
# 		Sample data : 1, 5, 7, 23
# 		Output : 
# 		List : [‘1', ' 5', ' 7', ' 23'] 
# 		Tuple : (‘1', ' 5', ' 7', ' 23')

inputData = input('Enter comma-separated numbers and press "Enter": ')
# inputData = "1, 5, 7, 23"
print('**************** Input ******************')
print(inputData)
list_result = []

inputData = inputData.split(',')
tuple_result = tuple(inputData)


for num in inputData:
	list_result.append(num)
print('**************** Output ******************')
print('This is tuple: {}'.format(tuple_result))
print('And this is list: {}'.format(list_result))