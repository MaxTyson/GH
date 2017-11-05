# 8. Write a script to replace last value of tuples in a list. 
# 		Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# 		Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

sampleList = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
num = 0

for obj in sampleList:
	new_list = []
	for iterator in obj:
		new_list.append(iterator)
	new_list[-1] = 100
	new_tuple = tuple(new_list)
	sampleList[num] = new_tuple
	num += 1
print('*'*20 + ' Output ' + '*'*20)
print(sampleList)