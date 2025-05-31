

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique. 

def fibonacci_recursiva (posicion):
    if posicion == 0 :
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursiva(posicion-1) +fibonacci_recursiva(posicion-2)    

print ( fibonacci_recursiva(6))

