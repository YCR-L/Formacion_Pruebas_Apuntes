#Imports
#Imports generales
#Import para usar el random.choice que nos permitirá escoger una opción aleatoriamente.
import random
#Imports no usados en la versión final
#import string


def PPTgamePlay():
    #Imprimimos el mensaje de inicio/'menú'
    user_player = input("Escoge una opción: \n" + "\n 1. 'Piedra' = piedra \n"+ "\n 2. 'Papel' = papel \n"+ "\n 3. 'Tijeras' = tijeras \n" + "\n ¡Que gane el 'mejor'! \n").lower()
    #La máquina elige uno aleatoriamente
    machine = random.choice(['piedra', 'papel', 'tijeras'])
        
    #Se imprime la elección de la máquina
    print('La máquina ha elegido: ' + machine)
  #Se valoran los resultados para dar un mensaje de final de juego.

    #Mensaje de empate.
    if user_player == machine:
        return '¡Igualados!'

    #Mensaje de victoria.
    if win(user_player, machine):
        return '¡Ganaste!'

    #Si no es victoria ni empate, mensaje de derrota.
    return '¡Derrota!, has sido fácil de ganar, la verdad....'

#Función que comprueba que el jugador(player) haya ganado al oponente, en este caso la máquina (opp), devolviendo un true.
def win(player, opp):
    #Devuelve True si gana el player
    if ((player == 'piedra' and opp == 'tijeras') #Piedra>Tijera
        or (player == 'tijeras' and opp == 'papel') #Tijera>Papel
        or (player == 'papel' and opp == 'piedra')): #Papel>Piedra
        return True
    

print(PPTgamePlay())