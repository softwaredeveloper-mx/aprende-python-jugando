import configparser

class Configuracion:
    def __init__(self, archivo):
        config = configparser.ConfigParser()
        config.read(archivo)
        self.ancho = int(config['Pantalla']['Ancho'])
        self.alto = int(config['Pantalla']['Alto'])
        
config = Configuracion('config.ini')        

        
        
            