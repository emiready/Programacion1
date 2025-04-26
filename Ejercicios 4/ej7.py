# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
acum  = 0

numero_usuario = int(input("Ingrese un numero positivo por favor: "))

if numero_usuario > 0:
    for sum in range (0, numero_usuario):
        acum += sum

print ("La suma de los numeros es ", acum)