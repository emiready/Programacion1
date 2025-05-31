#Nombramos para que esta hecho el programa. 
print("_____________________________________________________")
print("|                                                   |")
print("|Calculadora binario a decimal & decimal a binario  |")
print("|___________________________________________________|")

#Inicializamos en Y para que ingrese al bucle
continuar = "Y"

#Este While se utiliza para saber si queremos realizar el calculo o no.
while continuar.upper() == "Y":
    
    #Inicializamos la variable tipoCalculo, para preguntar que calculo deseamos realizar.
    tipoCalculo = None
    
    #Validación del tipo de calculo. Utilizamos try y except para capturar los errores.
    while tipoCalculo not in [1, 2]:
        try:        
            tipoCalculo = int(input("Elija una opción: \n1)Binario a decimal \n2)Decimal a binario\n> "))
            if tipoCalculo not in [1, 2]:
                print("Ingresa un número válido (1 o 2).")

        except ValueError:
            print("Por favor ingresa una opcion válida")

    #Segun el dato ingresado realizamos la logica solicitada.        
    if tipoCalculo == 1:
        
        
        #definicion de variables (esto se puede meter en el "menú"?)
        esBinario = False
        while not esBinario:
            binario=(input("Ingresá el número binario a convertir:"))
            esBinario = all(digito in "01" for digito in binario)
            if not esBinario:
                print("El número ingresado no es binario. (Deben estar compuestos por 0 y 1)")

        digitos=0
        binario = int(binario)
        numero= binario
        decimal=0
        
        #calculo de la cantidad de digitos del numero binario para iterar
        while  numero >= 1 :
            numero = numero / 10
            digitos = digitos + 1
        
        #conversion de binario a digital acumulando los terminos 2^n
        for n in range(0,digitos):
            decimal=decimal+((binario//10**n)%10)*(2**n)
            #muestro el valor calculado
        print(f"El número binario {binario} corresponde al número decimal {decimal}")
        
       
    #Segun el dato ingresado realizamos la logica solicitada.        

    elif tipoCalculo == 2:
        print("Logica para decimal a binario")
        
       # Validación para que ingrese un número decimal válido 
       
        validDecimal = False
        while not validDecimal:
            entrada = input("Ingresá un número decimal: ")
            try:
                decimal = int(entrada)
                if decimal < 0:
                    print("Por favor ingresa un número decimal positivo.")
                else:
                    validDecimal = True
            except ValueError:
                print("Por favor ingresa un número decimal válido.")

        binario = ""
        numOriginal = decimal

        #Calculos decimal a binario
        if decimal == 0:
            binario = "0"
        else:
            while decimal > 0:
                resto = decimal % 2
                binario = str(resto) + binario
                decimal //= 2
    
        print(f"El número {numOriginal} en binario es: {binario}")

    #Consultamos si desean realizar otra operación o finaliza el programa
    continuar = input("Deseas realizar otra operación? (Y = Si| N = No)\n> ")



