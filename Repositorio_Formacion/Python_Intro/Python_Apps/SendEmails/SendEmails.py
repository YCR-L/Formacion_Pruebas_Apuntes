#Imports
#Imports generales necesarios
from email.message import EmailMessage
from webapp2 import password
import ssl
import smtplib

remitente = ' ejemplo@gmail.com'
#se introduce la contraseña generada por el servicio de correo, en este caso google (se necesita 2fa para poder realizar esto)
rem_pass = password 
destinatario = 'hixir64997@tohup.com'

subject = "Prueba Correo"
body = "Correo de prueba"

message = EmailMessage()
message['From'] = remitente
message['To'] = destinatario
message[' subject'] = subject
message.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(remitente, rem_pass)
    smtp.sendmail(remitente, destinatario, message.as_string())