



#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel 
#con un solo bloque. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita
#para construir toda la pirámide. 


#Ejemplos: contar_bloques(1) → 1 (1) contar_bloques(2) → 3 (2 + 1) contar_bloques(4) → 10 (4 + 3 + 2 + 1) 8) 


#Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva
# cuántas veces aparece ese dígito dentro del número. 

#Ejemplos: contar_digito(12233421, 2) → 3 contar_digito(5555, 5) → 4        contar_digito(123456, 7) → 0 

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

# Probamos contar_bloques
n = int(input("Ingrese la cantidad de bloques en el nivel más bajo de la pirámide: "))
print(f"Total de bloques necesarios: {contar_bloques(n)}")

# Probamos contar_digito
numero = int(input("Ingrese un número entero positivo para contar dígitos: "))
digito = int(input("Ingrese el dígito que desea contar (0-9): "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}")
