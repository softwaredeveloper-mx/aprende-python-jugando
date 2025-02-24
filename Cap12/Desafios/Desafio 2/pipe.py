import pygame
import random

from settings import config

tubo_img = pygame.image.load("pipe.png")  # Imagen del tubo
tubo_img = pygame.transform.scale(tubo_img, (60, 600))

class Tubo:
    def __init__(self, pantalla, x):
        self.x = x
        self.altura = random.randint(150, 400)
        self.espacio = 150
        self.velocidad = 3
        self.pantalla = pantalla

    def actualizar(self):
        self.x -= self.velocidad

    def dibujar(self):
        self.pantalla.blit(tubo_img, (self.x, self.altura))  # Tubo de abajo
        self.pantalla.blit(pygame.transform.flip(tubo_img, False, True), (self.x, self.altura - self.espacio - 600))  # Tubo de arriba

    def colision(self, pajaro):
        pajaro_rect = pygame.Rect(pajaro.x, pajaro.y, 40, 30)
        tubo_rect_abajo = pygame.Rect(self.x, self.altura, 60, 600)
        tubo_rect_arriba = pygame.Rect(self.x, self.altura - self.espacio - 600, 60, 600)
        
        return pajaro_rect.colliderect(tubo_rect_abajo) or pajaro_rect.colliderect(tubo_rect_arriba)

