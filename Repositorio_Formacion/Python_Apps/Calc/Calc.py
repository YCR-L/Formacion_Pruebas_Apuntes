#Definimos las funciones que realizarán cada una de las operaciones:

#Suma
def sumar(a, b):
    ans = a + b
    print("\nEl resultado de la suma de ambos números es:" + str(ans) + "\n")
#Resta
def restar(a, b):
    ans = a - b
    print("\nEl resultado de la resta de ambos números es:" + str(ans) + "\n")
#Multiplicación
def multiplicar(a, b):
    ans = a*b
    print("\nEl resultado de la multiplicación de ambos números es:" + str(ans) + "\n")
#Division
def dividir(a, b):
    ans = a / b
    print("\nEl resultado de la división de ambos números es:" + str(ans) + "\n")


while True:
    #Menú a base de prints en consola
    print("\n¡Bienvenido! Soy la calculadora básica, te ayudaré en lo que pueda ;)")
    print("\nSuma (S)")
    print("Resta (R)")
    print("Multiplicación (M)")
    print("División (D)")
    print("Cerrar")
    #Solicitud de opción
    e = input("\n¿Como quieres operar? Elige una opción: ")

    #Suma
    if e == "S" or e == "s":

        print("\n ---Has elegido: Suma---")
        a = int(input("\nIntroduzca el primer operador: "))
        b = int(input("Introduzca el segundo operador: "))
        #Se llama a la función
        sumar(a, b)

    #Resta
    elif e == "R" or e == "r":

        print("\n ---Has elegido: Resta---")
        a = int(input("\nIntroduzca el primer operador: "))
        b = int(input("Introduzca el segundo operador: "))
        #Se llama a la función
        restar(a, b)

    #Multiplicación
    elif e == "M" or e == "m":

        print("\n ---Has elegido: Multiplicación---")
        a = int(input("\nIntroduzca el primer operador: "))
        b = int(input("Introduzca el segundo operador: "))
        #Se llama a la función
        multiplicar(a, b)

    #División
    elif e == "D" or e == "d":

        print("\n ---Has elegido: Division---")
        a = int(input("\nIntroduzca el primer operador: "))
        b = int(input("Introduzca el segundo operador: "))
        #Se llama a la función
        dividir(a, b)

    #Salida
    elif e == "Cerrar" or e == "cerrar":

        print("¡Has cerrado la calculadora! Se cerrará el proceso")
        quit()

