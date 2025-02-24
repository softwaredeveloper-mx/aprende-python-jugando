import json

class Heroe:
    def __init__(self, nombre, clase, nivel=1, hp=100):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.hp = hp
        
    def atacar(self, objetivo):
        daño = self.nivel * 10
        objetivo.hp -= daño
        print(f"{self.nombre} ataca a {objetivo.nombre} causando {daño} puntos de daño.")
        if objetivo.hp <= 0:
            print(f"{objetivo.nombre} ha sido derrotado.")
        else:
            print(f"A {objetivo.nombre} le quedan {objetivo.hp} puntos de vida.")        

    def presentarse(self):
        print(f"¡Soy {self.nombre}, un {self.clase} de nivel {self.nivel} con {self.hp} puntos de vida!")

def guardar_heroe(heroe, nombre_archivo="heroes.json"):
    with open(nombre_archivo, "w") as archivo:
        json.dump(heroe.__dict__, archivo)
        print(f"Héroe guardado en {nombre_archivo}")
            
def cargar_heroe(nombre_archivo="heroes.json"):
    try:
        with open(nombre_archivo, "r") as archivo:
            datos = json.load(archivo)
        heroe = Heroe(datos["nombre"], datos["clase"], datos["nivel"], datos["hp"])
        print(f"Héroe {heroe.nombre} cargado desde {nombre_archivo} =>")
        print(f"{heroe.__dict__}")
        return heroe
    except FileNotFoundError:
        print("No se encontró el archivo. Crea un nuevo héroe.")
        return None
    
def batalla(heroe1, heroe2):
    while heroe1.hp > 0 and heroe2.hp > 0:
        heroe1.atacar(heroe2)
        if heroe2.hp > 0:
            heroe2.atacar(heroe1)    

# Crear héroe o cargar desde archivo
print("1. Crear un nuevo héroe")
print("2. Cargar un héroe existente")
opcion = input("Elige una opción (1/2): ")

if opcion == "1":
    heroe = Heroe("Artemis", "Arquera", nivel=3, hp=120)
    guardar_heroe(heroe)
elif opcion == "2":
    heroe = cargar_heroe()
    if heroe is None:
        heroe = Heroe("Artemis", "Arquera", nivel=3, hp=120)

# Crear enemigo y jugar
enemigo = Heroe("Dragón de Fuego", "Enemigo", nivel=5, hp=150)
batalla(heroe, enemigo)

# Guardar héroe después de la batalla
guardar_heroe(heroe)
