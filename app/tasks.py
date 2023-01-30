from __future__ import absolute_import, unicode_literals

from celery import shared_task, current_task
from celery.utils.log import get_task_logger


import csv
import random
import string


logger = get_task_logger(__name__)


@shared_task
def generate_file(filename, data_count):
	
	header = ["SNo", "Name"]
	row_list = []
	
	for i in range(1,int(data_count)+int(1)):
		# get random string of length 6 without repeating letters
		result_str = ''.join(random.sample(string.ascii_lowercase, 8))
		data=[i,result_str]
		
		row_list.append(data)
	
	with open('data/'+filename + '.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		# write the header
		writer.writerow(header)
		# write the data
		writer.writerows(row_list)
	
	logger.info(f'{filename} created successfully')
	return filename + " created"


