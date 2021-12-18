def read():
	numbers = []
	with open('./Sesion 4/archivos/numbers.txt', 'r') as f:
		for line in f:
			numbers.append(int(line))
	print(numbers)

def write(modo='w'):
	names = ['Juanjo', 'Manuel', 'Andrea', 'Jhonatan', 'Christian']
	with open('./Sesion 4/archivos/names.txt', modo) as f:
		for name in names:
			f.write(name+'\n')

def main():
	write()

if __name__ == '__main__':
	main()