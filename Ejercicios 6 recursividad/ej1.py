#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el 
# factorial de todos los números enteros entre 1 y el número que indique el usuario.

n = int(input("iNgrese un numero por favor: "))

def fact(n):
    if n == 0 :
        return 1
    else:
        return n * fact(n - 1)

     
   
print (f"El factorial es {fact(n)}")