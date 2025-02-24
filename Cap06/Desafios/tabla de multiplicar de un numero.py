
numerovalido = False

while not numerovalido:
    numero = int(input("Dame un número del 1 al 10: "))
    if numero >= 1 and numero <=10:
        numerovalido = True
    else:
        print("Te comenté que me dieras un número del 1 al 10")
    

contador = 1
while contador <= 10:
    print(str(numero) + ' X ' + str(contador) + ' = ' + str(numero * contador))
    contador = contador + 1