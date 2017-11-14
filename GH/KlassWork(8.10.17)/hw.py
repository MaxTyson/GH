answer_file = open('answers.txt', 'r')
stud_answers = open('work.txt', 'r')
correct_answers = {}

def answers_to_list(answer_file):
	# function parses correct answers to dictionary
	for num_line, line in enumerate(answer_file):
		if num_line + 1 < 10:
			correct_answers[num_line + 1] = line[2:-1]
		else: correct_answers[num_line + 1] = line[3:]


def check_classwork(stud_answers):
	# function checks klasswork and return student's score
	answers_to_list(answer_file)
	points = 0; iteration = 0
	for num_line, line in enumerate(stud_answers):
		if '>>' in line:
			iteration += 1
			if line[3:-1] == correct_answers[iteration]:
				points += 1

	points <= 4 and print(points, ' points. Bad result!') or '\\n'
	(4 < points and points < 8) and print(points, ' points. Middle result!') or '\\n'
	points >= 8 and print(points, ' points. Excellent result!')	

check_classwork(stud_answers)

answer_file.close()
stud_answers.close()
