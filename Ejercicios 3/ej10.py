    #Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.
    # El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
    
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("¿En qué mes estás? (1-12): "))
dia = int(input("¿Qué día del mes es? (1-31): "))

# Para simplificar el análisis, convertimos mes y día a una sola "fecha numérica"
fecha = mes * 100 + dia  # Por ejemplo, 21 de marzo será 321

if hemisferio == "S":
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Verano"
    elif 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    elif 921 <= fecha <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Fecha no válida"

elif hemisferio == "N":
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Invierno"
    elif 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    elif 921 <= fecha <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Fecha no válida"
else:
    estacion = "Hemisferio no válido"

print("Estás en:", estacion)
