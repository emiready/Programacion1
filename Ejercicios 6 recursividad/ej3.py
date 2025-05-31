#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1) . Prueba esta función en un algoritmo general. 

base = int(input("Ingrese la base por favor: "))
exponente = int(input("Ingrese el exponente por favor: "))


def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return  base * potencia(base, exponente - 1)


     
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es {resultado}")



