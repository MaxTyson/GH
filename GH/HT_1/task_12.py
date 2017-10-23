# 9. Write a script to remove an empty tuple(s) from a list of tuples.
# 		Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# 		Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

sampleData = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
num = 0
for i in sampleData:
	if len(i) == 0:
		del sampleData[num]
	num += 1

print('*'*20 + ' Output ' + '*'*20)
print(sampleData)

