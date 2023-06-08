#Imports
#Imports generales
#Imports para uso de imagenes (Pillow)

"""Si da error el import o el código,
los pasos previos a la ejecución del .py es una reinstalación limpia de Pillow:
1. pip uninstall PIL | pip uninstall Pillow
2. pip install Pillow"""

from PIL import Image 
from PIL import ImageTk

def reescalado(tLargo, tAncho) :
    
    imagen = Image.open('QR001.jpg')
    #print(f"El tamaño actual de la imagen es el siguiente : {imagen.size}" )

    imagen_res = imagen.resize((tLargo, tAncho)) 
    imagen_res.save('ImagenReescalada_' + str(tLargo) + 'x' + str(tAncho) + '.jpeg')

option = input("¿Quieres reescalar la imagen (Si/No): ")

if option == "Si":
    print(f"Por favor introduce las dimensiones deseadas.")
    tLargo = int(input('Introduce el largo deseado: '))
    tAncho = int(input('Introduce el ancho deseado: '))
    reescalado(tLargo, tAncho)
elif option == "No":
    quit()
else:
    print("Error, pon Sí o No")
    quit()



