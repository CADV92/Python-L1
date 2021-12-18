import random

def adivina_numero(x, rand=True):
	num_aleatorio = random.randint(1,x)

	# print(f'NUESTRO NUMERO ALEATORIO --> {num_aleatorio}')

	predecidos = []
	prediccion = 0
	while prediccion != num_aleatorio:
		try:
			prediccion = int(input(f"Adivina el número entre 1 y {x}: "))
		except:
			print('ERROR -> SOLO PUEDES INGRESAR NÚMEROS ENTEROS!\n')
			continue

		if prediccion in predecidos:
			print('\nIntenta con un valor diferente!')
			continue

		predecidos.append(prediccion)

		# Evaluando predicciones
		if prediccion < num_aleatorio:
			print('Es muy pequeño, prueba otra vez!')
		elif prediccion > num_aleatorio:
			print('Es muy grande, prueba otra vez!')
	
	print('FELICITACIONES!!!\n-*- GANASTE -*-')
	print(f'Adivinaste el número aleatorio:\n[+] {num_aleatorio}')

def main():
	print('--------------------')
	print(' Adivina el número! ')
	print('--------------------\n')
	adivina_numero(10)

if __name__ == '__main__':
	main()