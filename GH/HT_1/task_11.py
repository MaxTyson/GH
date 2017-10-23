# 11. Write a script to remove duplicates from Dictionary.

dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic2 = {7: 70, 2: 20, 8: 80, 9: 90, 10: 100, 6: 60}
print('*'*20 + ' Input ' + '*'*20)
print('dictionary №1 : ', dic1)
print('dictionary №2 : ', dic2)

for i in dic1:
	if i in dic2:
		dic2.popitem()

print('*'*20 + ' Output ' + '*'*20)
print('dictionary: №1 ', dic1)
print('dictionary: №2 ', dic2)