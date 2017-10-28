# 2. Написати функцію, яка буде приймати декілька значень, одне з яких значення за замовченням(повинна бути перевірка на наявність), 
# і у випадку якщо воно є додати його до іншого агрументу, якщо немає - придумайте логіку що робити программі.
days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def week(day, country='en'):
	if (day < 1) or (day > 7):
		return False
	if country == 'en':
		return(days[day-1])
	elif country == 'ua':
		return(days[day])

print(week(1))
print(week(1, 'ua'))