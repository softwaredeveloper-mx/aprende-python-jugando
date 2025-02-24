monstruos = {}

def agregar_monstruo(nombre, poder):
    monstruos[nombre] = poder
    print(f"{nombre} con poder {poder} agregado.")

def mostrar_monstruos():
    print("Lista de monstruos:")
    for nombre, poder in monstruos.items():
        print(f"- {nombre}: {poder}")


bContinuar = True
while bContinuar:
    nombre = input("¿Cual nombre que quieres agregar? Teclea fin si ya no quieres agregar mas ")    
    if nombre == "fin":
        bContinuar = False
    else:
        poder = input("¿Cual poder para ese nombre?")
        agregar_monstruo(nombre, poder)
mostrar_monstruos()

bContinuar = True
while bContinuar:
    item = input("¿Cual elemento quieres Eliminar? Teclea fin si ya no quieres eliminar mas ")
    if item == "fin":
        bContinuar = False
    else:
        del(monstruos[item])
mostrar_monstruos()