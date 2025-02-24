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

heroe1 = Heroe("Artemis", "Arquera", nivel=3, hp=120)
heroe1.presentarse()
guardar_heroe(heroe1)

