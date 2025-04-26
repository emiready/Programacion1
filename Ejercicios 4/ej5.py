# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random   

# primero debo crear las opciones y la eleccion aleatoria
numero_juego = random.randint (0,9)

#comienzo el contador de intentos en 0
cont= 0
acertado = False


while not acertado:
    
    numero = int(input("Ingrese un numero entre 0 y 9  por favor: "))
    cont = cont + 1 
    
    if numero == numero_juego:
        print ("EL NUMERO ES EL GANADOR, FELICITACIONES!")
        acertado = True
     
    else: 
        print ("Ingrese otro numero por favor perdedor")


print ("El numero de veces para ganar fue de: ", cont , "intentos.") 

