"""Apuntes 
Introductorios
Python"""


#HelloWorld

print("Hello World")


#Variables

ejemploString = "Prueba, que no solución."
ejemploInt = 123

print(ejemploString)


#Concatenación Variables

print (f"{ejemploInt}-{ejemploString}")
"""Ojo, esta concatenación puede dar errores,
 ya que "ejemploInt" y "ejemploString" son tipos diferentes de datos,
 por lo que lo correcto sería 'Stringificar' el numeral con la función str()"""
print (f"{str(ejemploInt)}-{ejemploString}")


#Variables de entrada de datos
respuesta = input("¿Cómo te llamas?")

print(respuesta)

#Condicionales y bucles 1

#IF
respuestaIf = input("¿Sí?")
respuestaIfInt = int(input ("¿Es menor de 10?"))

if respuestaIf == "Sí":
    print("Has respondido 'Sí'")
else:
    print("No has respondido 'Sí'")


if respuestaIfInt < 10:
    print("Sí, es menor de 10, concretamente es" + respuestaIfInt)
else:
    print("No, no es menor de 10, concretamente es" + respuestaIfInt)



#Funciones

def mostrarMenor10(respuestaIfInt):
    if respuestaIfInt < 10:
        print("Sí, es menor de 10, concretamente es" + respuestaIfInt)
    else:
        print("No, no es menor de 10, concretamente es" + respuestaIfInt)


#Arrays
#               0         1            2            3
animales = ['Gaviota', 'Tortuga', 'Salamandra', 'Yo, ¡ups!']
print(animales[3])


#Condicionales y bucles 2

#FOR
for animal in animales:
    print("-" + animal)
