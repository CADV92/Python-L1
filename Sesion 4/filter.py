import time

nueva_lista = range(0,1000000)

time_start = time.time()
odd = []
for val in nueva_lista:
	if val%2 != 0:
		odd.append(val)

time_end = time.time()
print('Estructura clásica:',time_end-time_start)

# con filter
time_start = time.time()
odd = list(filter(lambda x: x%2 != 0,nueva_lista))
time_end = time.time()
print('Estructura filter:',time_end-time_start)