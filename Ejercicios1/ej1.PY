# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
#print ("Hola Mundo") 


#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Ej: si el usuario ingresa “Marcos”, el programa imprimira “Hola Marcos!”.

#nombre = input   ("Hola, ingresa tu nombre por favor")

#print  (f"Buenos dias {nombre}, como estas?")   

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

# nombre = input   ("Hola, ingresa tu nombre por favor")
# apellido = input   ("Hola, ingresa tu apellido por favor")
# edad = input   ("Hola, ingresa tu edad por favor")
# residencia = input   ("Hola, ingresa tu lugar de residencia por favor")

# print  (f"Soy {nombre}{ apellido}, tengo {edad} años y vivo en {residencia}.")     


# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área ysu perímetro.

# import math

# radio = float (input ("Hola, ingrese el radio, para poder calcular el area y el perimetro correspondiente:    "))

#calculos

# perimetro = 2 * math.pi * radio

# area = math.pi * radio ** 2

# print (f"El area del circulo es {area} y el perimetro es {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla acuántas horas equivale.

# horas =  int( input(f"Ingrese la cantidad de hs para calcular los segundos "))

# segundos = horas * 3600 


# print (f"{horas} horas equivalen a {segundos}")

# # 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.



# numero = int (input (f"Ingrese un numero por favor, para poder calcular las tablas correspondientes:  "))

# print (f"Si hacemos {numero} * 1 = el resultado es {numero * 1}")
# print (f"Si hacemos {numero} * 2 = el resultado es {numero * 2}")
# print (f"Si hacemos {numero} * 3 = el resultado es {numero * 3}")
# print (f"Si hacemos {numero} * 4 = el resultado es {numero * 4}")
# print (f"Si hacemos {numero} * 5 = el resultado es {numero * 5}")
# print (f"Si hacemos {numero} * 6 = el resultado es {numero * 6}")
# print (f"Si hacemos {numero} * 7 = el resultado es {numero * 7}")
# print (f"Si hacemos {numero} * 8 = el resultado es {numero * 8}")
# print (f"Si hacemos {numero} * 9 = el resultado es {numero * 9}")
# print (f"Si hacemos {numero} * 10 = el resultado es {numero * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

# numero1 = int(input("Ingrese un numero por favor "))
# numero2 = int(input("Ingrese otro numero por favor "))

# suma = numero1 + numero2
# resta  = numero1 - numero2
# multiplicacion = numero1 * numero2
# division = numero1 / numero2

# print(f"La suma de los numeros es: {suma}")
# print(f"La resta de los numeros es: {resta}")
# print(f"La multiplicacion de los numeros es: {multiplicacion}")
# print(f"La division de los numeros es: {division}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:
# 𝐼𝑀𝐶 = peso en kg / altura en m2


# altura = float(input("Ingrese su altura por favor (en metros.centimetros)"))
# peso = float(input("Ingrese su peso por favor  (en kilos)"))
# masamuscular = float (peso/altura**2)

# print (f"El indice de masa muscular es {masamuscular}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 

# celsius= float(input(f"Ingrese la temperatura Celsius a convertir: "))

# farenheit= float( 9/5 * celsius + 32)

# print(f" {celsius} grados Celsius equivalen a {farenheit} grados Farenheit.")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.


# numero1 = int(input("Ingrese un numero por favor "))
# numero2 = int(input("Ingrese un segundo numero por favor "))
# numero3 = int(input("Ingrese un tercer numero por favor "))

# promedio = float((numero1 + numero2 + numero3) / 3)

# print(f"El promedio de los 3 numeros ingresados es: {promedio}.")