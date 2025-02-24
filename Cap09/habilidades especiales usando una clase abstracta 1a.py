from abc import ABC, abstractmethod

# Clase abstracta
class Criatura(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def habilidad_especial(self):
        pass  # Las clases derivadas deben implementar este método

# Clase derivada: Dragón
class Dragon(Criatura):    
    def habilidad_especial(self):
        print(f"{self.nombre} lanza una llamarada de fuego.")        
    
# Clase derivada: Unicornio
class Unicornio(Criatura):
    def habilidad_especial(self):
        print(f"{self.nombre} usa su cuerno mágico para curar.")

firagon = Dragon("Firagon")
firagon.habilidad_especial()

estrella = Unicornio("Estrella")
estrella.habilidad_especial()
