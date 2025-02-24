from abc import ABC,abstractmethod

class Personaje(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        
    @abstractmethod
    def accion(self):
        pass
    
class Heroe(Personaje):    
    def accion(self):
        print(f"Soy {self.nombre} y hago el bien sin mirar a quien")

class Villano(Personaje):    
    def accion(self):
        print(f"Soy {self.nombre} y hago el mal sin mirar a cual")      

heroe01 = Heroe("superman")
heroe02 = Heroe("batman")
villano01 = Villano("guazon")
villano02 = Villano("acertijo")

heroe01.accion()
heroe02.accion()
villano01.accion()
villano02.accion()