# Clase base
class Criatura:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def presentarse(self):
        print(f"Soy {self.nombre}, una criatura del tipo {self.tipo}.")

# Clase derivada: Dragón
class Dragon(Criatura):
    def __init__(self, nombre, color, poder):
        super().__init__(nombre, "Dragón")  # Llama al constructor de la clase base
        self.color = color
        self.poder = poder

    def lanzar_poder(self):
        print(f"{self.nombre} lanza su poder de {self.poder}.")

# Clase derivada: Unicornio
class Unicornio(Criatura):
    def __init__(self, nombre, magia):
        super().__init__(nombre, "Unicornio")
        self.magia = magia

    def usar_magia(self):
        print(f"{self.nombre} usa su magia especial de {self.magia}.")

firagon = Dragon("Firagon", "rojo", "lanzar fuego")
firagon.presentarse()
firagon.lanzar_poder()

estrella = Unicornio("Estrella", "sanación")
estrella.presentarse()
estrella.usar_magia()