# 1 

i =1 
while i <2: 
    print("Iteracion exterior", i , end ="")
    j=1
    bandera =True
    while bandera:
        print("Iteracion interior: ",j, end ="")
        j *= 1        
        if j != 2:
            bandera = False 
    
    i= i 

i = 1 
while i < 2: 
    print("Iteracion exterior", i , end ="")
    j = 1
    bandera = True
    while bandera:
        print("Iteracion interior: ", j, end ="")
        j > 1  # <- Esta línea no tiene ningún efecto
        if j != 2:
            bandera = False 
    i = i + 1
