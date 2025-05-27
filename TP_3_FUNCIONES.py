# funciones para reutilizar

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

def hola_mundo():
    print ("Hola Mundo") 

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Ej: si el usuario ingresa “Marcos”, el programa imprimira “Hola Marcos!”.

def saludar():
    nombre = input  ("Hola, ingresa tu nombre por favor")

    print  (f"Buenos dias {nombre}, como estas?")   

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

def presentacion():
    nombre = input   ("Hola, ingresa tu nombre por favor") 
    apellido = input   ("Hola, ingresa tu apellido por favor")
    edad = input   ("Hola, ingresa tu edad por favor")
    residencia = input   ("Hola, ingresa tu lugar de residencia por favor")

    print  (f"Soy {nombre} { apellido}, tengo {edad} años y vivo en {residencia}.")    
 
#4 ) CALCULAR   EL AREA DEL CIRCULO   ARREGLAR
#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
#que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.


def calcular_area_circulo(radio):
    pi = 3.14159
    return pi * radio ** 2

def calcular_perimetro_circulo(radio):
    pi = 3.14159
    return 2 * pi * radio





# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de hs correspondientes.
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.



def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas




# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un nro como parámetro y imprima la tabla de multiplicar de ese nro del 1 al 10. 
# Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)





# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

#peso = float(input("\n8. Ingresá tu peso en kg: "))
#altura = float(input("Ingresá tu altura en metros: "))
#imc = calcular_imc(peso, altura)
#print(f"Tu IMC es: {imc:.2f}")



# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente enFahrenheit.
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.


def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32



# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. 
# Solicitar los números al usuario y mostrar el resultado usando esta función.


def calcular_promedio(a, b, c):
    return (a + b + c) / 3



#Programa principal para correr las funciones 



hola_mundo()
saludar()
presentacion()

radio = float(input("4. Ingresá el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

segundos_ingresados = int(input("5. Ingresá los segundos a convertir: "))
horas = segundos_a_horas(segundos_ingresados)
print(f"{segundos_ingresados} segundos equivalen a {horas} horas.")

num = int(input("6. Ingresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)

a = float(input("\n7. Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

peso = float(input("\n8. Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

celsius = float(input("\n9. Ingresá la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f} °F")

n1 = float(input("\n10. Ingresá el primer número: "))
n2 = float(input("Ingresá el segundo número: "))
n3 = float(input("Ingresá el tercer número: "))
promedio = calcular_promedio(n1, n2, n3)
print(f"El promedio es: {promedio:.2f}")























