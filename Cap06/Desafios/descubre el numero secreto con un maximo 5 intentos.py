# Número secreto definido
numSecreto = 5

# Pedimos al usuario que adivine el número
for i in range(1, 6):
    numero = int(input("Adivina el número secreto (entre 1 y 5): "))
    # Comprobamos si la respuesta es correcta
    if int(numero) == numSecreto:  
        print("¡Correcto, adivinaste el número secreto!")
        break
    else:      
        if i == 5:
            print("¡Se te acabaron las oportunidades!. Suerte para la próxima")
        else:
            print("¡Incorrecto, buen intento!. Intentale de nuevo")
            
        
            

