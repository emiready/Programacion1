# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745



numero_ingresado = int(input("Ingrese un numero por favor: "))
numero_invertido = 0


 

while numero_ingresado != 0:
    digito  = numero_ingresado % 10 
    numero_invertido  = numero_invertido * 10 + digito
    numero_ingresado = numero_ingresado // 10 


print ("El numero invertido es ", numero_invertido)
