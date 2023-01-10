#Se crea una lista con las preguntas, instanciando las preguntas y sus respuestas
quizzie = {
    "pregunta1": {
        "pregunta": "¿En qué empresa trabaja YCR?",
        "respuesta": "ATOS"
    },
    "pregunta2": {
        "pregunta": "¿Cuál es el hobby de YCR?",
        "respuesta": "Trastear y aprender"
    },
    "pregunta3": {
        "pregunta": "¿Donde vive YCR?",
        "respuesta": "A Coruña"
    },
    "pregunta4": {
        "pregunta": "¿Que le gusta a YCR?",
        "respuesta": "Viajar"
    },"pregunta5": {
        "pregunta": "¿Tiene YCR mascotas y otras responsabilidades ajenas al trabajo?",
        "respuesta": "Sí"
    },
}

#Variable donde se acumularán los puntos, sumandose por cada respuesta correcta
puntos = 0

#Bucle para avanzar por los items de la lista de preguntas
for key, value in quizzie.items():
    #se imprime la pregunta
    print("\n" + value['pregunta'])
    #se pide la respuesta
    respuesta = input("\n¿Cuál es la respuesta? ")

    #se comprueban las respuestas dadas
    #si es correcto, da mensaje de 'correcto' y suma el punto, mostrando a su vez la puntuación
    if respuesta.lower() == value['respuesta'] . lower():
        print('\n¡Muy bien!')
        puntos = puntos + 1
        print("\n Tus puntos actuales son: " + str(puntos))
        print("")
    else:
    #si es incorrecto/inválido, da mensaje de 'incorrecto', mostrando a su vez la puntuación
        print("\n¡Fallaste!")
        print("\La respuesta correcta es: " + value['respuesta'])
        print("\n Tus puntos actuales son: " + str(puntos))
        print("")

#Se imprime la puntuación final       
print("\nHas conseguido " + str(puntos) + " de los 5 puntos posibles" + "\nEn concreto, el porcentaje de acierto es: " + str(int(puntos/5 * 100)) + "%")