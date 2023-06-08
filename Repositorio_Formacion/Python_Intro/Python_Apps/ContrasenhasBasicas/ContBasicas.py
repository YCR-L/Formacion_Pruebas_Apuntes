#Imports
#Imports generales
import string
import random

caracteres = list(string.ascii_letters + string.digits + " !@#$%^&*()")

def gen_cont_basica():
    
    contLargo = int(input("¿Cómo de larga quieres tenerla? (Longitud recomendada 8 carácteres"))
    
    random.shuffle(caracteres)
    
    contra = []
    
    for x in range(contLargo):
        contra.append(random.choice(caracteres))
        
    random.shuffle(contra)
    
    contra = "" .join(contra)
    print(contra)

eleccion = input("Bienvenido, ¿quieres una contraseña 'veraz'? (s/n): ")

if option == "s":
    gen_cont_basica()
elif option == "n":
    print("Muy bien, disfruta de tus 'maravillosas contraseñas'")
    quit()
else:
    print("Tío no es tan dificil decir Si o No. Teclea bien, anda")
    quit()
