    # 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.


numero = int(input("Ingrese el  numero por favor: "))

cont = 0



while numero != 0 :    
    
    numero = numero // 10 
    cont = cont + 1 
    
print ("La cantidad de cifras del numero es: ", cont)
    
        