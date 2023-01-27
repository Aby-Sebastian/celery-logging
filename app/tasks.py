from __future__ import absolute_import, unicode_literals

from celery import shared_task

import csv
import random
import string


@shared_task
def generate_file(filename, data_count):
	
	header = ["SNo", "Name"]
	row_list = []
	
	for i in range(1,data_count+1):
		# get random string of length 6 without repeating letters
		result_str = ''.join(random.sample(string.ascii_lowercase, 8))
		data=[i,result_str]
		print(data)
		row_list.append(data)
	print(row_list)
	with open('data/'+filename + '.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		# write the header
		writer.writerow(header)
		# write the data
		writer.writerows(row_list)
	return filename + " created"