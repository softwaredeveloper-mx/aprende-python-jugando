from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre        
        
    @abstractmethod
    def hacer_sonido(self):
        pass
    
class Perro(Animal):
    def hacer_sonido(self):
        print(f"Hola soy un perro, me dicen {self.nombre}  y hago Gua Gua")
class Gato(Animal):
    def hacer_sonido(self):
        print(f"Hola soy un gato, me dicen {self.nombre}  y hago Miau Miau")

lista_animales = [Perro("Pulgas"), Perro("solovino"),Gato("lucas"),Gato("michi"), Gato("canelo")]

for animal in lista_animales:
    animal.hacer_sonido()
