from random import randint, uniform
from datetime import datetime

int_list_100k = []; flo_list_100k = []
def random_list():
	# function fills up empty listst with random values
	while len(int_list_100k) < 10:
		float_num = uniform(0, 99)
		flo_list_100k.append(float_num)
		int_num = randint(0, 99)
		int_list_100k.append(int_num)
	return int_list_100k, flo_list_100k
random_list()

# print out ansorted lists
print(int_list_100k)
print('**' * 30)
print(flo_list_100k)
print('**' * 30)

def sort_insertion(array):
	time_before = datetime.now()
	for item in range(len(array)):
		min_item = array[item]; max_item = item
		while max_item > 0 and array[max_item-1] > min_item:
			array[max_item] = array[max_item-1]
			max_item = max_item - 1
		array[max_item] = min_item
	sort_time = datetime.now() - time_before # check sorting time
	
	print('\nInsertion-sort! array = {} numbers, sort time = {}. \n{}'.format(len(array), sort_time, array))

def sort_selection(array):
	time_before = datetime.now()
	for item in range(len(array) - 1):
		for item2 in range(item + 1, len(array)):
			if array[item] > array[item2]:
				array[item], array[item2] = array[item2], array[item]
	sort_time = datetime.now() - time_before # check sorting time
	
	print('\nSelection-sort! array = {} numbers, sort time = {}. \n{}'.format(len(array), sort_time, array))

def sort_buble(array):
	time_before = datetime.now()
	for item in range(len(array)):
		for item2 in range(len(array) - 1):
			if array[item2] > array[item2 + 1]:
				array[item2], array[item2 + 1] = array[item2 + 1], array[item2]
	sort_time = datetime.now() - time_before # check sorting time
	
	print('\nBuble-sort! array = {} numbers, sort time = {}. \n{}'.format(len(array), sort_time, array))

# Printing results
if (sort_insertion(int_list_100k) == int_list_100k.sort(key=None, reverse=False)) & (sort_selection(int_list_100k) == int_list_100k.sort(key=None, reverse=False)) & (sort_buble(int_list_100k) == int_list_100k.sort(key=None, reverse=False)):
	print('Integer sorted success!') # if sorting results equal to standart sorting

if (sort_insertion(flo_list_100k) == flo_list_100k.sort(key=None, reverse=False)) & (sort_selection(flo_list_100k) == flo_list_100k.sort(key=None, reverse=False)) & (sort_buble(flo_list_100k) == flo_list_100k.sort(key=None, reverse=False)):
	print('Flout sorted success!') # if sorting results equal to standart sorting
