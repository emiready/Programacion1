# como funciona un acumulador

numero_objetivo = 4

acumulador = 0

for numero in range (1, numero_objetivo + 1):
    acumulador = acumulador + numero 
    
print ("El numero acumulado desde el 1 al 10 es ", acumulador)


# while con un umbral

umbral  = 10
numero = 0

while numero < umbral:
    numero_ingresado = int(input("Ingrese un numero por favor: "))
    numero = numero + numero_ingresado 
    
print ("El numero ingresado es ", numero)


#prueba de una sumatoria mas

cantidad_inputs = 4
sumatoria = 0

for cont in range (1, cantidad_inputs + 1 ):
    print("Ingrese un numero por favor: ", cont)
    numero_input = int(input())
    sumatoria = numero_input + sumatoria

print ("El numero que da la sumatoria es: ",sumatoria)

print ("El numero promedio es: ",sumatoria/cont)