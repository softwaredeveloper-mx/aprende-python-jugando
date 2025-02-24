import pygame

from settings import config

# Cargar imagen del pájaro
pajaro_img = pygame.image.load("bird.png")  # Cargar imagen del pájaro
pajaro_img = pygame.transform.scale(pajaro_img, (40, 30))

class Pajaro:
    def __init__(self, pantalla):
        self.x = 50
        self.y = config.alto / 2
        self.velocidad = 0
        self.gravedad = 0.5
        self.salto = -8
        self.pantalla = pantalla

    def actualizar(self):
        self.velocidad += self.gravedad
        self.y += self.velocidad

        # Evitar que el pájaro salga de la pantalla
        if self.y > config.alto - 30:
            self.y = config.alto - 30
            self.velocidad = 0

    def saltar(self):
        self.velocidad = self.salto

    def dibujar(self):
        self.pantalla.blit(pajaro_img, (self.x, self.y))

