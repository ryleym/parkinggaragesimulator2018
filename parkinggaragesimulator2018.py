from datetime import datetime, timedelta
from random import random, randint, uniform
import random
import string
import time
import matplotlib.pyplot as plt
import requests

cars = []
x = []
y = []
curr_time = datetime.now();
close_time = curr_time + timedelta(hours=18);
print('close_time: ', close_time);
while (datetime.now().timestamp() <= close_time.timestamp() or len(cars) != 0):
	entry = randint(0,1)
	if (entry == 1 and len(cars) != 1000):
		tag = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)]);
		entry_time = datetime.now();
		exit_time = entry_time + timedelta(hours=uniform(0, 18))
		if (exit_time.timestamp() <= close_time.timestamp()):
			cars.append({'parking_tag': tag, 'entry_time': entry_time, 'exit_time': exit_time});
			requests.post('http://zero5.co:3002/garages/5ae68dba20242561359123ec/cars', {'parking_tag': tag});
			x.append(datetime.now());
			y.append(len(cars));
		#print('cars: ')
		#for car in cars:
			#print(car);
	i = 0;
	for car in cars:
		if (car['exit_time'].timestamp() < datetime.now().timestamp()):
			i += 1;
			requests.put('http://zero5.co:3002/garages/5ae68dba20242561359123ec/cars', {'parking_tag': car['parking_tag']});
			x.append(datetime.now());
			y.append(len(cars) - i);
	cars = [car for car in cars if car['exit_time'].timestamp() >= datetime.now().timestamp()]
	print(len(cars));
	time.sleep(15);
