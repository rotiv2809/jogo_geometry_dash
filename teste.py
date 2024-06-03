import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Linha Crescendo ao Longo do Tempo')

# Configurações da linha
line_color = (255, 0, 0)  # Vermelho
line_start_pos = (100, 300)
line_end_pos = [100, 300]  # Usando lista para permitir modificação
line_growth_speed = 5  # Velocidade de crescimento da linha em pixels por quadro

# Controle da taxa de atualização
clock = pygame.time.Clock()
FPS = 60

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza a posição final da linha
    line_end_pos[0] += line_growth_speed  # Incrementa a posição x da linha
    if line_end_pos[0] > WIDTH:  # Verifica se a linha atingiu a borda direita da tela
        line_end_pos[0] = WIDTH

    # Limpa a tela com preto
    screen.fill((0, 0, 0))
    
    # Desenha a linha na tela
    pygame.draw.line(screen, line_color, line_start_pos, line_end_pos, 2)
    
    # Atualiza a tela
    pygame.display.flip()
    clock.tick(FPS)

# Encerra o Pygame
pygame.quit()
sys.exit()
