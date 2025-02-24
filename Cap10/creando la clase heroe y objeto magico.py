class ObjetoMagico:
    def __init__(self, nombre, bonificacion_hp):
        self.nombre = nombre
        self.bonificacion_hp = bonificacion_hp


class Heroe:
    def __init__(self, nombre, clase, nivel=1, hp=100):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.hp = hp
        self.objetos = []  # Lista de objetos equipados

    def equipar_objeto(self, objeto):
        self.objetos.append(objeto)
        self.hp += objeto.bonificacion_hp
        print(f"{self.nombre} ha equipado {objeto.nombre} y ahora tiene {self.hp} puntos de vida.")

espada_magica = ObjetoMagico("Espada de Luz", 30)
heroe1 = Heroe("Artemis", "Arquera")
heroe1.equipar_objeto(espada_magica)
