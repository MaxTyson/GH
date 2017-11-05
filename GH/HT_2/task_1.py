# 1. (таких ф-цій потрібно написати 3 -> різними варіантами) Написати функцію season, приймаючу 1 аргумент — номер місяця (від 1 до 12), 
# яка буде повертати пору року, якій цей місяць належить (зима, весна, літо або осінь).

#1
def season(month_num):
	if month_num < 1 or month_num > 12:
		return False
	elif month_num == 1:
		return 'January'
	elif month_num == 2:
		return 'February'
	elif month_num == 3:
		return 'March'
	elif month_num == 4:
		return 'April'
	elif month_num == 5:
		return 'May'
	elif month_num == 6:
		return 'June'
	elif month_num == 7:
		return 'July'
	elif month_num == 8:
		return 'August'
	elif month_num == 9:
		return 'September'
	elif month_num == 10:
		return 'October'
	elif month_num == 11:
		return 'November'
	elif month_num == 12:
		return 'December'
	else: return False
print(season(int(input('Enter number of month: '))))

#2
month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
def season2(month_num):
	return(month[month_num])
#print(season2(int(input('Enter number of month: '))))

#3
month2 = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
def season3(month_num):
	return(month2[month_num - 1])
# print(season3(int(input('Enter number of month: '))))