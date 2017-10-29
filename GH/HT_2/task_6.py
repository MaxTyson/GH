def web_site_test():
	# test you web-site
	front_end = input('Enter which language you use to make interface (JavaScript, HTML, HTML+CSS): ')
	beck_end = input('What a beck-end language you use? (PHP, Python, Java, or eny language) ')
	print('Designe: ', second_func(front_end))
	print('Functional: ', third_func(beck_end))

def second_func(fe_leng):
	# front-end language
	if fe_leng == 'JavaScript' or fe_leng == 'JS':
		return 'Wow! Denamic pages, coool!'
	elif fe_leng == 'HTML':
		return 'Hm... It\'s not modern, dude)'
	elif fe_leng == 'HTML+CSS':
		return 'So, ok! Not bed interface)'

def third_func(be_lang):
	# beck-end language
	if be_lang == 'PHP':
		return 'You web-site is so bed!'
	elif be_lang == 'Python':
		return 'You have the best web-site in Cherkassy!'
	elif be_lang == 'Java':
		return 'This web-site so slowly!'
	else:
		return 'Realy? Is it web-site? I don\'t think so)))'

web_site_test()