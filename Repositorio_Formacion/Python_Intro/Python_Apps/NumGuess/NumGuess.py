#Importamos random para el NumGuess del usuario y para el número que intenta adivinar la máquina en el CompNumGuess
import random

#NumGuess por el usuario, la máquina genera el número con un random, entre el 1 y el número establecido en x.
#En este caso establecemos que x sea 10 en la llamada del método.
def num_guess(x):

    r_n = random.randint(1, x)
    guess = 0

    while guess != r_n:
        guess = int(input(f'\n\n Adivina el número entre 1 y {x}: '))
        if guess < r_n:
            print('\n\n Casi pero no, dale más arriba.')
        elif guess > r_n:
            print('\n\n Te has pasado un poco. Tranquilo y reinténtalo.')

    print('\n\nEnhorabuena has adivinado el número correctamente.' +
    '\n\n El número adivinado es:' + f'{r_n}')

#Llamamos a la función
num_guess(10)

#------------------------------------------------------------------------------------------------------------------
#Para hacer la ejecución continua y que no se mezclen ambos procesos de estas distintas funciones, procedemos a separarlos mediante una línea.
print('\n')
print('\n ------------------------------------------------------------------------------------------------------------------')
print('\n Ahora que has adivinado el número, me toca a mí, piensa un número.')
print('\n ------------------------------------------------------------------------------------------------------------------')
print('\n')
#------------------------------------------------------------------------------------------------------------------


#NumGuess por la máquina, el usuario es el que piensa el número, y la máquina reacciona según la respuesta dada.
#Siendo el comportamiento el siguiente: 
# c = la máquina ha acertado (correcto)
# a = número más alto (alto)
# b = número más bajo (bajo)

def comp_num_guess(x):

    n_bajo = 1
    n_alto = x
    respuesta = ''

    while respuesta != 'c':
        if n_bajo != n_alto:
            comp_guess = random.randint(n_bajo, n_alto)
        else:
            comp_guess = n_bajo  
        respuesta = input(f'¿Es el número {comp_guess} correcto? Sí es así pulsa c'
        + f'\n Si me he pasado, pulsa a'
        + '\n Si me he quedado corto, pulsa b').lower()
        if respuesta == 'a':
            n_alto = comp_guess - 1
        elif respuesta == 'l':
            n_bajo = comp_guess + 1

    print(f'He adivinado tu número: {comp_guess}, ¡la próxima intentalo mejor!')

#Llamamos a la función
comp_num_guess(10)
