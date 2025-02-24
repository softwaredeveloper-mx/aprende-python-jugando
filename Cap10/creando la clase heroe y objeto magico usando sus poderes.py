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
        
    def usar_habilidad(self):
        if self.clase == "Guerrero":
            print(f"{self.nombre} usa 'Golpe Poderoso'!")
        elif self.clase == "Mago":
            print(f"{self.nombre} lanza 'Bola de Fuego'!")
        elif self.clase == "Arquera":
            print(f"{self.nombre} dispara 'Flecha Veloz'!")
        else:
            print(f"{self.nombre} no tiene habilidades especiales.")

heroe1 = Heroe("Thoran", "Guerrero")
heroe1.usar_habilidad()

heroe2 = Heroe("Zyra", "Mago")
heroe2.usar_habilidad()

