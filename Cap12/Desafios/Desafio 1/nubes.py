import pygame
from settings import config

fondo_img = pygame.image.load('background.png')  # Imagen de fondo con nubes
fondo_img = pygame.transform.scale(fondo_img, (config.ancho, config.alto)) # ajustar al ancho y alto deseado

class Fondo:
    def __init__(self, pantalla):
        self.x1 = 0
        self.x2 = config.ancho
        self.velocidad = 1  # Movimiento lento del fondo
        self.pantalla = pantalla

    def actualizar(self):
        self.x1 -= self.velocidad
        self.x2 -= self.velocidad

        if self.x1 <= -config.ancho:
            self.x1 = config.ancho

        if self.x2 <= -config.ancho:
            self.x2 = config.ancho

    def dibujar(self):
        self.pantalla.blit(fondo_img, (self.x1, 0))
        self.pantalla.blit(fondo_img, (self.x2, 0))

