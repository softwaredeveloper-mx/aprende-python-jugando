import json

def guardar_progreso(escena_actual, nombre_archivo="progreso.json"):
    with open(nombre_archivo, "w") as archivo:
        json.dump({"escena": escena_actual}, archivo)
    print(f"Progreso guardado en {nombre_archivo}")

def cargar_progreso(nombre_archivo="progreso.json"):
    try:
        with open(nombre_archivo, "r") as archivo:
            datos = json.load(archivo)
        print(f"Progreso cargado. Escena actual: {datos['escena']}")
        return datos["escena"]
    except FileNotFoundError:
        print("No se encontró un progreso guardado. Inicia una nueva aventura.")
        return None

def escena_inicial():
    print("Eres un valiente héroe en busca de un tesoro escondido.")
    print("Un sendero se divide en dos:")
    print("1. Tomar el camino oscuro.")
    print("2. Seguir el camino iluminado.")
    eleccion = input("¿Qué decides? (1/2): ")
    guardar_progreso("escena_inicial")
    if eleccion == "1":
        camino_oscuro()
    elif eleccion == "2":
        camino_iluminado()
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        escena_inicial()

def camino_oscuro():
    print("El camino oscuro está lleno de trampas.")
    print("Encuentras un cofre. ¿Quieres abrirlo?")
    print("1. Sí")
    print("2. No")
    eleccion = input("¿Qué decides? (1/2): ")
    guardar_progreso("camino_oscuro")
    if eleccion == "1":
        print("¡El cofre estaba encantado! Pierdes el juego.")
    elif eleccion == "2":
        print("Evitaste la trampa. Sigues adelante y encuentras el tesoro. ¡Ganaste!")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        camino_oscuro()
        
def camino_iluminado():
    print("El camino iluminado parece seguro, pero pronto encuentras un río caudaloso.")
    print("Tienes dos opciones:")
    print("1. Intentar cruzar el río nadando.")
    print("2. Buscar un puente cercano.")
    eleccion = input("¿Qué decides? (1/2): ")
    guardar_progreso("camino_iluminado")
    if eleccion == "1":
        print("El río era más peligroso de lo que parecía. Te arrastra la corriente. ¡Perdiste el juego!")
    elif eleccion == "2":
        print("Encuentras un puente, cruzas con seguridad y llegas al tesoro. ¡Ganaste!")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        camino_iluminado()
        

escena = cargar_progreso()
if escena == "camino_iluminado":
    camino_iluminado()
elif escena == "camino_oscuro":
    camino_oscuro()
else:
    escena_inicial()
