import time

nueva_lista = range(0,1000000)

time_start = time.time()
squares = []
for val in nueva_lista:
	squares.append(val**2)

time_end = time.time()
print('Estructura clásica:',time_end-time_start)
print(squares[:10],'\n')


# con map
time_start = time.time()
squares = list(map(lambda x: x**2,nueva_lista))
time_end = time.time()
print('Estructura map:',time_end-time_start)
print(squares[:10],'\n')


# compresión de listas
time_start = time.time()
squares = [val**2 for val in nueva_lista]
time_end = time.time()
print('Compresión de lista:',time_end-time_start)
print(squares[:10],'\n')
