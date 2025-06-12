


#Ingreso de años de nacimiento
anios = []
cantidad = int(input("¿Cuántas personas hay en el grupo? "))

for i in range(cantidad):
    anio = int(input("Ingresá el año de nacimiento de la persona " + str(i + 1) + ": "))
    anios.append(anio)
#Contar si son pares e impares
pares = 0
impares = 0

for anio in anios:
    if anio % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Cantidad de años pares:", pares)
print("Cantidad de años impares:", impares)

#Verificar si todos nacieron después del 2000
todos_despues_2000 = True

for anio in anios:
    if anio <= 2000:
        todos_despues_2000 = False

if todos_despues_2000:
    print("Grupo Z")

#Función para saber si un año es bisiesto
def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 != 0 or anio % 400 == 0:
            return True
    return False

#Verificar si hay algún año bisiesto
hay_bisiesto = False

for anio in anios:
    if es_bisiesto(anio):
        hay_bisiesto = True

if hay_bisiesto:
    print("Tenemos un año especial")

#Calcular edades actuales y producto cartesiano
anio_actual = 2025
edades = []

for anio in anios:
    edad = anio_actual - anio
    edades.append(edad)

print("Producto cartesiano (año, edad):")
for anio in anios:
    for edad in edades:
        print((anio, edad))
