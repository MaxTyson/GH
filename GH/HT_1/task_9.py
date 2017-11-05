# 9. Write a script to remove an empty tuple(s) from a list of tuples.
# 		Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# 		Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

sampleData = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print('*'*20 + ' Input ' + '*'*20)
print(sampleData)

localList = []
for item in sampleData:
	if len(item) > 0:
		localList.append(item)
sampleData = localList

print('*'*20 + ' Output ' + '*'*20)
print(sampleData)