import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGEM_LASER = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png')))


pygame.font.init()
pygame.display.set_caption('Laser Reflexivo')
#!

FONTE_PONTOS = pygame.font.SysFont('arial', 50)

class Laser:
    IMG = IMAGEM_LASER
    ANGULO_DESLOCAMENTO = 60
    VELOCIDADE = 10
    WIDTH = 2
    HEIGHT = 2
    
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.direcao = 1
        self.tempo = 0
        self.laser_color = (255, 0, 0)  # Cor vermelha
        self.laser_width = 5
        self.laser_height = 10
        self.laser_x = self.WIDTH
        self.laser_y = self.HEIGHT
        self.laser_speed_y = 5
        
    def inverter(self):
        self.direcao *= -1
        
    def mover(self):
        self.tempo += 1
        deslocamento = self.velocidade*self.tempo
        self.y += deslocamento*self.direcao
    
    def desenhar(self, tela):
        #chegamos na parte de descobrir como desenhar algo pra sempre em python
        