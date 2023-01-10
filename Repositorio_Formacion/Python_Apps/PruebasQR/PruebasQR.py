#Imports
#Imports generales
#Imports para usar los QRCodes
#Previa instalacion con pip install qrcode
import qrcode

def generar_qr(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants. ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black")
    img.save("QR001.png")
    
url = input("Introduce tu dirección web: ")

#Llamamos a la función
generar_qr(url)
print('Tu QR se ha generado')