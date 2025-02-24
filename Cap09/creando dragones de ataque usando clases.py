class Dragon:
    def __init__(self, nombre, color, poder):
        self.nombre = nombre
        self.color = color
        self.poder = poder

    def presentarse(self):
        print(f"¡Soy {self.nombre}, un dragón {self.color} con el poder de {self.poder}!")

    def atacar(self, objetivo):
        print(f"{self.nombre} ataca a {objetivo} usando {self.poder}!")

dragon1 = Dragon("Firagon", "rojo", "lanzar fuego")
dragon1.presentarse()
dragon1.atacar("un castillo")
