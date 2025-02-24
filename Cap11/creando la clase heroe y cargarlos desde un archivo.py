import json

class Heroe:
    def __init__(self, nombre, clase, nivel=1, hp=100):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.hp = hp

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

cargar_heroe()