from datetime import datetime, timedelta
from random import random, randint, uniform
import random
import string
import time
cars = []

while (True):
	entry = randint(0,1)
	if (entry == 1 and len(cars) != 50):
		tag = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)]);
		entry_time = datetime.now();
		exit_time = entry_time + timedelta(hours=uniform(0,1))
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
	time.sleep(1);
		
