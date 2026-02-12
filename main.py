import pygame
from constantes import *

pygame.init()
screen = pygame.display.set_mode((LARGURA_MAPA, ALTURA_MAPA))
clock = pygame.time.Clock()
runnig = True
dt = 0

posicao_criatura = pygame.Vector2(LARGURA_MAPA/2, ALTURA_MAPA/2)

while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False

    screen.fill((0,0,0))

    pygame.draw.circle(screen, 'red', posicao_criatura, 20)


    pygame.display.flip()

    dt = clock.tick(60)/1000

pygame.quit()