#Imports
#Imports locales
from Palabras import palabras
from Visual import puntos_vida_visual
#Imports generales
#Import para usar el random.choice que nos permitirá escoger una palabra aleatoriamente.
import random
import string



#Función que elige la palabra aleatoriamente, que será llamada en la función principal.
def palabra_ok(palabras):
    #Escoge palabra aleatoriamente (p=palabra escogida)
    p = random.choice(palabras)  

    #En caso de contener guión/un espacio, seguirá seleccionando palabras para evitar así un posible error.
    while '-' in p or ' ' in p:
        p = random.choice(palabras)

    return p.upper()

#Función principal
def hangman():

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("         ¿Ahorcado? ¿El juego?         ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    p = palabra_ok(palabras)
    #Letras que deben adivinarse (forman la palabra escogida)
    letras_restantes = set(p)  
    #Letras del abecedario
    abc = set(string.ascii_uppercase)
    #Letras adivinadas correctamente
    letras_adivinadas = set()  

    puntos_vida = 5

    #Siempre que letras_restantes>0 y puntos_vida>0, pedir respuesta al jugador
    while len(letras_restantes) > 0 and puntos_vida > 0:
        
        print(f"\n Te quedan {puntos_vida} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        #Actual estado de la palabra a adivinar
        p_list = [letra if letra in letras_adivinadas else '-' for letra in p]
        #Se imprime la representacion visual de las vidas que se poseen
        print(puntos_vida_visual[puntos_vida])
        #Se imprime la representacion escrita de las vidas que se poseen
        print(f'\nTus puntos de vida son: {puntos_vida}')
        print(f"\n Palabra: {' '.join(p_list)}") #Se muestran las letras introducidas, separadas por espacios

        #Jugador introduce otra letra
        letra_player = input('\n Escoge una letra: ').upper()

        #Si letra introducida(letra_player) = abecedario + letra introducida(letra_player) != no ingresada,
        #letra introducida(letra_player) se añade al conjunto de letras ingresadas.
        if letra_player in abc - letras_adivinadas:
            letras_adivinadas.add(letra_player)
            #Letra en la palabra  = se resta la letra en las letras_restantes.
            if letra_player in letras_restantes:
                letras_restantes.remove(letra_player)
                print('')
            # No letra en la palabra = -1 a puntos_vida.
            else:
                puntos_vida = puntos_vida - 1
                print(f"\n La letra elegida: {letra_player} no es correcta. No está en la palabra.")
        #Si la letra escogida ya fue usada = Mensaje de error / Letra inválida = Mensaje de error.
        elif letra_player in letras_adivinadas:
            print("\n Letra usada anteriormente. Por favor, inténtalo de nuevo.")
        else:
            print("\n Letra inválida.")

    #Se controla el fin del juego.
    #Siendo dos opciones posibles: 
    #Vida==0---->Fin del juego, mensaje de derrota
    #letras_restantes=letras_adivinadas(equivalente, ya lo que se controlan son los puntos_vida)----> Fin del juego, mensaje de victoria
    if puntos_vida == 0:
        print(puntos_vida_visual[puntos_vida])
        print(f"¡Ahorcadín, ahorcadín! Morriches. D-E-P. La palabra que tenías que adivinar era: {p}")
    else:
        print(f'¡Soberbio! ¡Acertaste la palabra correcta: {p}!')


if __name__ == '__main__':
    hangman()