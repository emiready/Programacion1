
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True  # Una palabra vacía o de un solo carácter siempre es palíndroma
    if palabra[0] != palabra[-1]:
        return False  # Si los extremos no coinciden, no es palíndromo
    return es_palindromo(palabra[1:-1])  # Llamada recursiva descartando los extremos

# Ejemplo de uso
texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(texto):
    print(f"La palabra '{texto}' es un palíndromo.")
else:
    print(f"La palabra '{texto}' no es un palindromo.")
