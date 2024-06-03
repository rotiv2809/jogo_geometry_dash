import pygame
import os
import sys

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
        self.line_end_pos = [100,300]
        self.laser_speed_y = 5
        self.line_growth_speed = 5
        
    def inverter(self):
        self.direcao *= -1
        
    def mover(self):
        self.tempo += 1
        deslocamento = self.velocidade*self.tempo
        self.y += deslocamento*self.direcao
    
    def desenhar(self, tela):
        #chegamos na parte de descobrir como desenhar algo pra sempre em python
        pass
    
def main():
    laser = Laser(100, 300)
    screen = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    clock = pygame.time.Clock()
    FPS = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    laser.inverter()
        laser.line_end_pos += laser.line_growth_speed
        
        screen.fill((0,0,0))
        
        pygame.draw.line(screen, laser.line_color, (laser.x, laser.y), laser.line_end_pos,2)
    
        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()
    sys.exit()
    
if __name__ == '__main__':
    main()