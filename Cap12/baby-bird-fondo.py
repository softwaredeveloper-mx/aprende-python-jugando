import pygame
    
from nubes import Fondo
from settings import config



# Inicializar pygame
pygame.init()

# Definir tamaño de la pantalla
pantalla = pygame.display.set_mode((config.ancho, config.alto))

# Definir el fondo
fondo = Fondo(pantalla)

pygame.display.set_caption("Baby Bird")

# Definir colores
BLANCO = (255, 255, 255)

# Control de FPS
clock = pygame.time.Clock()

# Ciclo o Bucle para escuchar eventos y actualizar pantalla
ejecutando = True
while ejecutando:    
    pantalla.fill(BLANCO)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                pajaro.saltar()
    
    # Actualizar fondo
    fondo.actualizar()
    fondo.dibujar()
          
    pygame.display.update()
    clock.tick(30)

pygame.quit()