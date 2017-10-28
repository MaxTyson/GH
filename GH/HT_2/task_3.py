# Створіть 3 різних функції(на ваш вибір), кожна з цих функцій повинна повертати якийсь результат. 
# Також створіть четверу ф-цію, яка в тілі викликає 3 попередніб обробляє повернутий ними результат 
# та також повертає результат. Таким чином ми будемо викликати 1 функцію, а вона в своєму тілі ще 3

days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
seasons = ('Winter', 'Spring', 'Summer', 'Autumn')

def day(day_num):
	# function returns name of day of the week from tuple
	if (day_num < 1) or (day_num > 7):
		return False
	return(days[day_num - 1])

def month(month_num):
	# function returns name of month from tuple
	if (month_num < 1) or (month_num > 12):
		return False
	return(months[month_num - 1])

def season(season_num):
	# function returns name of season from tuple
	if (season_num < 1) or (season_num > 4):
		return False
	return(seasons[season_num - 1])

def date(day_num, month_num):
	# function prints names of day, month and seasons which belongs it
	if day(day_num) != False:
		if month(month_num) != False:
			if month_num > 2 and month_num < 6:
				season = seasons[1]
			elif month_num > 5 and month_num < 9:
				season = seasons[2]
			elif month_num > 8 and month_num < 12:
				season = seasons[3]
			else: 
				season = seasons[0]
	print('Today is {}, it\'s {}, beautiful {}.'.format(day(day_num), month(month_num), season))
	return(day, month, season)

# test program: enter day's number(1-7) and month's number(1-12)
date(7, 10)
