import pygame
    
from nubes import Fondo
from settings import config
from pipe import Tubo
from bird import Pajaro
from puntaje import Puntaje

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

# Definir los tubos
tubos = [Tubo(pantalla,config.ancho + 100)]

# Crear el pajaro
pajaro = Pajaro(pantalla)

# Puntaje
puntaje = Puntaje(pantalla, pajaro)
puntaje.mostrar_puntaje()
    
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
    
    # Actualizar Pajaro
    pajaro.actualizar()
    pajaro.dibujar()
    
    
     # Manejo de los tubos
    for tubo in tubos:
        tubo.actualizar()
        tubo.dibujar()
        
        # cada vez que se mueve algun tubo => checamos si hay colisión
        if tubo.colision(pajaro):
            print("¡Perdiste!")
            ejecutando = False            
                
        puntaje.actualizar(tubo) 
        
    if tubos[-1].x < config.ancho - 200:
        tubos.append(Tubo(pantalla,config.ancho))

    if tubos[0].x < -60:
        tubos.pop(0)

     
    # Mostrar puntaje
    puntaje. mostrar_puntaje()
    
    
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()   