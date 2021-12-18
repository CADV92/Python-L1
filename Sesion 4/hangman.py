import os
import random

ahorcado = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }

def clear_display():
	os.system('clear')


def replace_letters(word):
	chr = ['Á','É','Í','Ó','Ú']
	chr_norm = ['A','E','I','O','U']
	new_word = []
	for lttr in word.upper():
		if lttr in chr:
			new_word.append(chr_norm[chr.index(lttr)])
		else:
			new_word.append(lttr)
	return ''.join(new_word)
			

def get_words():
	with open('./Sesion 4/archivos/data.txt', 'r', encoding='utf-8') as f:
		words = [word.upper() for word in f]
	word = random.choice(words)
	word = replace_letters(word)
	return word


def redraw_display(word,letter_match):
	clear_display()
	print('-*- HANGMAN GAME -*-')
	masked_word = [i if i in letter_match else '_' for i in word][:-1]
	# print(word)
	print(' '.join(masked_word))
	return masked_word


def input_letters(word):
	life = 7
	letter_match = []
	while True:
		masked_word = redraw_display(word, letter_match)
		print(ahorcado[life])
		if not '_' in masked_word:
			print('FELICIDADES!')
			break

		letter = input(">>> ").upper()

		if letter in word:
			# print("Letra correcta")
			letter_match.append(letter)
		else:
			# print('Letra incorrecta!')
			life -= 1
		
		if life == 0:
			print('\nAHORCADO!')
			print('>>> Respuesta:', word)
			break
	print('\nGAME OVER...')


def run():
	clear_display()
	word = get_words()
	input_letters(word)

if __name__ == '__main__':
	run()