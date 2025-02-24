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
            
    def atacar(self, objetivo):
        daño = self.nivel * 10
        objetivo.hp -= daño
        print(f"{self.nombre} ataca a {objetivo.nombre} causando {daño} puntos de daño.")
        if objetivo.hp <= 0:
            print(f"{objetivo.nombre} ha sido derrotado.")
        else:
            print(f"A {objetivo.nombre} le quedan {objetivo.hp} puntos de vida.")
            
    def presentarse(self):
        print(f"Soy {self.nombre}")
        self.usar_habilidad()            
            
heroe1 = Heroe("Artemis", "Arquera", nivel=3, hp=120)
heroe2 = Heroe("Thoran", "Guerrero", nivel=2, hp=150)

while heroe1.hp > 0 and heroe2.hp > 0:
    heroe1.atacar(heroe2)
    if heroe2.hp > 0:
        heroe2.atacar(heroe1)
