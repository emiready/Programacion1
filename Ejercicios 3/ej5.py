#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contraseña = input("Ingrese su contraseña, por favor: ")

if len(contraseña) > 7 and len (contraseña) < 15:
    print("Ha ingresado una constraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
    
    
    