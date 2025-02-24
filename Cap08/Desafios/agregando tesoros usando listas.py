cofre = []

def agregar_tesoro(tesoro):
    cofre.append(tesoro)
    print(f"{tesoro} agregado al cofre.")

def eliminar_tesoro(tesoro):
    if tesoro in cofre:
        cofre.remove(tesoro)
        print(f"{tesoro} eliminado del cofre.")
    else:
        print(f"{tesoro} no está en el cofre.")

def mostrar_cofre():
    print("Contenido del cofre:", cofre)

bContinuar = True
while bContinuar:
    item = input("¿Cual elemento quieres agregar? Teclea fin si ya no quieres agregar mas ")
    if item == "fin":
        bContinuar = False
    else:
        agregar_tesoro(item)
mostrar_cofre()

bContinuar = True
while bContinuar:
    item = input("¿Cual elemento quieres Eliminar? Teclea fin si ya no quieres eliminar mas ")
    if item == "fin":
        bContinuar = False
    else:
        eliminar_tesoro(item)
mostrar_cofre()


