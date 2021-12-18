from functools import reduce
import time

my_list = range(1,99999)
time_start = time.time()
allMultiplied = reduce(lambda a, b: a * b, my_list)
time_end = time.time()
print('Reduce:',time_end-time_start)

# print(allMultiplied)


time_start = time.time()

totalizador = 1
for num in my_list:
	totalizador *= num

time_end = time.time()
print('Tradicional:',time_end-time_start)

print(allMultiplied==totalizador)
