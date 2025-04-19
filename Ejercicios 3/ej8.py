#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = (input("Ingrese su nombre: " ))
numero = (input("Ingrese 1 para Mayuscula, 2 para Minusculas, 3 para Primer letra en Mayuscula"))

print("Opción ingresada:", {numero})

if numero == "1":
    print("Tu nombre en mayusculas es: ", nombre.upper())
elif numero == "2":
    print("Tu nombre en minusculas es: ", nombre.lower())
elif numero =="3":
    print("Tu nombre que comienza en mayusculas es: ", nombre.title())
else:
    print("No elegista una opcion correcta, solo podes elegir 1, 2 y 3")
             

