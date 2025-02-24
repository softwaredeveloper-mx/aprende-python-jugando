# Número secreto definido
numSecreto = 5

# Pedimos al usuario que adivine el número
respuesta = input("Adivina el número secreto (entre 1 y 5): ")

# Comprobamos si la respuesta es correcta
if int(respuesta) == numSecreto:  
    print("¡Correcto, adivinaste el número secreto!")
else:  
    print("¡Incorrecto, buen intento!. Suerte para la próxima")
