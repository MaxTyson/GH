import os
import re
import csv
import errno

unique_text_dict = {}
markers = ('CRITICAL', 'ERROR', 'WARNING')

def uniques_check(text):
	if text not in unique_text_dict:
		unique_text_dict[text] = 1
		return False
	else:
		unique_text_dict[text] += 1
		return True

def parsing_logs(filename):
	unique_logs = open('reports/unique.csv', 'w+')
	csv_writer_unique = csv.writer(unique_logs)

	with open(filename, 'r') as logs:
		with open('reports/all_data.csv', 'w+', newline='') as all_errors_file:
			csv_writer = csv.writer(all_errors_file)
			csv_writer.writerow([' ID |MARKER|     DATE_TIME      | DESCRIPTION ']) # title to table
			dt_pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}') # pattern for find date & time
			dc_pattern = re.compile(r': .*') # pattern for find description

			for line_id, line in enumerate(logs):
				for marker in markers:
					if marker in line:
						date_time = dt_pattern.search(line).group()
						description = dc_pattern.search(line).group()
						column = [line_id + 1, marker, date_time, description]
						csv_writer.writerow(column)

						uniques_check(description) == False and \
							csv_writer_unique.writerow(column)
	unique_logs.close()

def create_rep(str_rep_name):
	# create new repository
	try:
	    os.makedirs(str_rep_name)
	except OSError as error:
	    if error.errno != errno.EEXIST:
	        raise

create_rep('reports')
parsing_logs('openerp-server.log')
