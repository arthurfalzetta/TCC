import pygame
import random
from constantes import *


class Criatura:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x,y)
        self.vel = pygame.Vector2(random.uniform(-1,1), random.uniform(-1,1)).normalize()


        self.vel_max = random.uniform(100,300)
        self.tamanho = 15
        self.agressividade = random.random()

    def mover(self, dt):
        self.pos += self.vel * self.vel_max * dt


        if self.pos.x > LARGURA_MAPA: self.pos.x = 0
        if self.pos.x < 0: self.pos.x = LARGURA_MAPA
        if self.pos.y > ALTURA_MAPA: self.pos.y = 0
        if self.pos.y < 0: self.pos.y = ALTURA_MAPA


    def desenhar(self, screen):
        pygame.draw.circle(screen, (255,0,0), (int(self.pos.x), int(self.pos.y)), self.tamanho)
    
    