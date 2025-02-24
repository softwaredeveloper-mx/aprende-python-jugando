class Dragon:
    # El constructor: se ejecuta al crear un dragón
    def __init__(self, nombre, color, poder):
        self.nombre = nombre  # Nombre del dragón
        self.color = color    # Color del dragón
        self.poder = poder    # Poder especial del dragón

    # Método para que el dragón se presente
    def presentarse(self):
        print(f"¡Soy {self.nombre}, un dragón {self.color} con el poder de {self.poder}!")

# Crear dragones usando la clase
dragon1 = Dragon("Firagon", "rojo", "lanzar fuego")
dragon2 = Dragon("Glacius", "azul", "crear hielo")

# Los dragones se presentan
dragon1.presentarse()
dragon2.presentarse()
