class Heroe:
    def __init__(self, nombre, clase, nivel=1, hp=100):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.hp = hp

    def presentarse(self):
        print(f"¡Soy {self.nombre}, un {self.clase} de nivel {self.nivel} con {self.hp} puntos de vida!")

heroe1 = Heroe("Artemis", "Arquera", nivel=3, hp=120)
heroe1.presentarse()
