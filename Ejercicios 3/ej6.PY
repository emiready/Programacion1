from statistics import mode, median, mean 
import random



lista_aleatoria = [random.randint(1,50) for i in range (20)]


print(f"La lista elegida es: ", lista_aleatoria)

print(f"La moda es: ", mode(lista_aleatoria))

print(f"La mediana es: ", median(lista_aleatoria))

print(f"El promedio es: ", mean(lista_aleatoria))

