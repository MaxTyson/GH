# 10. Write a script to concatenate following dictionaries to create a new one.
# 		Sample Dictionary : 
# 		dic1={1:10, 2:20} 
# 		dic2={3:30, 4:40} 
# 		dic3={5:50,6:60}
# 		Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1:10, 2:20} 
dic2 = {3:30, 4:40} 
dic3 = {5:50, 6:60}
result = {}

def allDictsInOne(oldDictionary, newDictionary):
	for index in oldDictionary:
		newDictionary.update(oldDictionary.items())

allDictsInOne(dic1, result)
allDictsInOne(dic2, result)
allDictsInOne(dic3, result)

print('*'*20 + ' Output ' + '*'*20)
print(result)