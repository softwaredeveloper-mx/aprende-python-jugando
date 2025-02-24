numero_secreto = 7
adivinado = False

while not adivinado:
    respuesta = int(input("Adivina el número secreto (entre 1 y 10): "))
    if respuesta == numero_secreto:
        print("¡Correcto! Adivinaste el número secreto.")
        adivinado = True
    elif respuesta < numero_secreto:
        print("Demasiado bajo, intenta de nuevo.")
    else:
        print("Demasiado alto, intenta de nuevo.")
