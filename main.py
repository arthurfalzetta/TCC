import pygame
from constantes import *
from agente import Agente

pygame.init()
screen = pygame.display.set_mode((LARGURA_MAPA, ALTURA_MAPA))
clock = pygame.time.Clock()
runnig = True
dt = 0


agentes = [Agente(100,100) for _ in range(20)]
resource_pos = pygame.Vector2(700,300)

while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False

    screen.fill((0,0,0))

    for agente in agentes:
        agente.mover(dt, resource_pos)
        agente.desenhar(screen)
    

    pygame.draw.circle(screen, (0,255,0), resource_pos, 15)


    pygame.display.flip()

    dt = clock.tick(60)/1000

pygame.quit()