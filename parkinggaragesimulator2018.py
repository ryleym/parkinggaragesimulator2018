from datetime import datetime, timedelta
from random import random, randint, uniform
import random
import string
import time
cars = []

curr_time = datetime.now();
close_time = curr_time + timedelta(hours=12);
print('close_time: ', close_time);
while (datetime.now().timestamp() <= close_time.timestamp() or len(cars) != 0):
	entry = randint(0,1)
	if (entry == 1 and len(cars) != 500):
		tag = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)]);
		entry_time = datetime.now();
		exit_time = entry_time + timedelta(hours=uniform(0,12))
		if (exit_time.timestamp() <= close_time.timestamp()):
			cars.append({'parking_tag': tag, 'entry_time': entry_time, 'exit_time': exit_time});
			print('car enter: ', {'parking_tag': tag, 'entry_time': entry_time, 'exit_time': exit_time})
		#print('cars: ')
		#for car in cars:
			#print(car);
	for car in cars:
		if (car['exit_time'].timestamp() < datetime.now().timestamp()):
			print('car exit: ', car)
	cars = [car for car in cars if car['exit_time'].timestamp() >= datetime.now().timestamp()]
	print(len(cars));
	time.sleep(10);
		
