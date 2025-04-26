# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor,
# pero debe poder procesar 100 números cambiando solo un valor).

numeros = 100
suma = 0

for c in range (numeros):
    numeros_promediar = int(input("Ingrese un numero por favor : "))
    suma += numeros_promediar

print ("El promedio de los numeros ingresados es: ", (suma/numeros))