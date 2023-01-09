#Imports
#Imports generales
#Import para generar registros aleatorios
import random
#Import para medir los tiempos de búsqueda
import time

#Función de búsqueda naive o búsqueda 'ingenúa' (con su lista y su objetivo)
def naive_s(list, targ):
    for i in range(len(list)):
        if list[i] == targ:
            return i
    return -1

#Función de búsqueda binaria (con lista, objetivo, inicio y final)
def binary_s(list, targ, low_limit=None, high_limit=None):
    
    #Inicio de la lista generada en la búsqueda
    if low_limit is None:
        low_limit = 0 
    #Final de la lista generada en la búsqueda
    if high_limit is None:
        high_limit = len(list) - 1 

    if high_limit < low_limit:
        return -1

    p_m = (low_limit + high_limit) // 2

    if list[p_m] == targ:
        return p_m
    elif targ < list[p_m]:
        return binary_s(list, targ, low_limit, p_m-1)
    else:
        return binary_s(list, targ, p_m+1, high_limit)


if __name__=='__main__':
    
    #Creamos una sorted list de 10k registros (numeros generados por random)
    tamaño = 10000
    s_list = set()

    while len(s_list) < tamaño:
        s_list.add(random.randint(-3*tamaño, 3*tamaño))

    s_list = sorted(list(s_list))

    #Tiempo de búsqueda ingenua.
    inicio = time.time()
    for targ in s_list:
        naive_s(s_list, targ)#Llamamos a la función pasandole la sorted list
    fin = time.time()
    print(f"Tiempo búsqueda 'naive' (s): {fin - inicio} ")#Se imprime en consola el tiempo que ha tardado

    #Tiempo búsqueda binaria.
    inicio = time.time()
    for targ in s_list:
        binary_s(s_list, targ)#Llamamos a la función pasandole la sorted list
    fin = time.time()
    print(f"Tiempo búsqueda 'binaria' (s): {fin - inicio}")#Se imprime en consola el tiempo que ha tardado