import pygame

from settings import config

class Puntaje:
    def __init__(self, pantalla, pajaro):
        self.puntaje = 0
        self.fuente = pygame.font.Font(None, 36)
        self.pantalla = pantalla
        self.pajaro = pajaro
        self.tubosContados = []
        self.paso = False

    def actualizar(self, tubo):
        #print("tubo x= %s pajaro x = %s" % (tubo.x,self.pajaro.x))
        if tubo.x <= self.pajaro.x and not(tubo in self.tubosContados):            
            self.puntaje += 1
            self.tubosContados.append(tubo)
            self.paso = True
        else:
            self.paso = False

    def mostrar_puntaje(self):
        texto = self.fuente.render(f"Puntaje: {self.puntaje}", True, (255, 255, 255))
        self.pantalla.blit(texto, (10, 10))
