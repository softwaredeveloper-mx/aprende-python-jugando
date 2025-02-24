# Pedimos la edad al usuario
edadTexto = input("Ingresa tu edad: ")

# definimos una cadena de texto comun para todas las respuestas
textorespuesta = "El precio de tu entrada es de "

if int(edadTexto) <= 12:
    print(textorespuesta + " $5") 
elif (int(edadTexto) > 12 and int(edadTexto) < 18):  
    print(textorespuesta + " $7")
else:  
    print(textorespuesta + " $8")
