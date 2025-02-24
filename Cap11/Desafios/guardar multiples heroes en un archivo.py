import json

class Heroe:
    def __init__(self, nombre, clase, nivel=1, hp=100):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.hp = hp

    def __repr__(self):
        return f"Héroe({self.nombre}, {self.clase}, Nivel: {self.nivel}, HP: {self.hp})"

def guardar_todos_los_heroes(lista_heroes, nombre_archivo="heroes.json"):
    # Convertir cada héroe en un diccionario para almacenarlo
    datos = [heroe.__dict__ for heroe in lista_heroes]
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo)
    print(f"Todos los héroes guardados en {nombre_archivo}")

def cargar_todos_los_heroes(nombre_archivo="heroes.json"):
    try:
        with open(nombre_archivo, "r") as archivo:
            datos = json.load(archivo)
        # Reconstruir cada héroe a partir de los datos
        lista_heroes = [Heroe(d["nombre"], d["clase"], d["nivel"], d["hp"]) for d in datos]
        print("Héroes cargados:")
        for heroe in lista_heroes:
            print(f"  - {heroe}")
        return lista_heroes
    except FileNotFoundError:
        print("No se encontró el archivo. No hay héroes guardados.")
        return []

# Ejemplo de uso
h1 = Heroe("Artemis", "Arquera", nivel=3, hp=120)
h2 = Heroe("Thor", "Guerrero", nivel=5, hp=200)
lista_heroes = [h1, h2]

# Guardar todos los héroes
guardar_todos_los_heroes(lista_heroes)

# Cargar héroes desde el archivo
heroes_cargados = cargar_todos_los_heroes()
