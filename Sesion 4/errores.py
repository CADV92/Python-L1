def suma(a,b):
	return a+b

def main():
	try:
		a = int(input('Ingrese el num1: '))
		b = int(input('Ingrese el num2: '))
	except ZeroDivisionError:
		print('Zero division')
	except ValueError:
		print('Ingrese solo NÚMEROS ENTEROS!')
	except:
		print('Excepción general')
	else: 
		print('\nSe calculó satisfactoriamente...\n')
		print(suma(a,b))
	finally:
		print('**SIEMPRE ME EJECUTO!**')

if __name__ == '__main__':
	
	main()