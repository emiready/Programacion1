# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. • Luego, pedí un nombre y mostrale el número asociado, si existe. Ejemplo:

agenda = {}

print ("Carga 5 contactos")

for i in range (5):
    nombre = input(f"Ingrese el nombre del contacto: {i + 1}" )
    numero = input(f"Ingrese el numero del contacto: {nombre}" )
    agenda[nombre] = numero 

buscar= input("\n Ingrese el nombre del contacto que quieres buscar: ")

if buscar in agenda:
    print(f"El número de {buscar} es: {agenda[buscar]}")
else:
    print(f"No se encontró el contacto llamado {buscar}.")







