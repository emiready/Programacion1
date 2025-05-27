# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Ingrese el primer numero: "))

numero2 = int(input("Ingrese el segundo numero: "))

acum = 0 

for c in range (numero1 + 1 , numero2 ):
    acum += c

print ("La suma de todos los numeros es: ", acum)