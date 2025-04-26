# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese

numero = int(input("Ingrese un numero por favor : "))
acum = 0
  
while numero != 0:
    numero = int(input("Ingrese otro por favor : "))
    acum   += numero
    
    
print("El numero sumado acumulado es: ", acum)
    
    