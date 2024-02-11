import pygame
import time
import random

pygame.init()

# Configurações do jogo
largura = 800
altura = 600
tamanho_bloco = 20
velocidade = 15

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# Inicialização da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Relógio para controlar a taxa de atualização
relogio = pygame.time.Clock()

# Função para desenhar a cobra na tela
def desenhar_cobra(cobra, tamanho_bloco):
    for segmento in cobra:
        pygame.draw.rect(tela, branco, [segmento[0], segmento[1], tamanho_bloco, tamanho_bloco])

# Função principal do jogo
def jogo():
    jogo_ativo = True

    # Posição inicial da cobra
    cobra = [[largura / 2, altura / 2]]
   
    # Velocidade inicial da cobra
    velocidade_x = 0
    velocidade_y = 0

    # Posição inicial da comida
    comida = [random.randrange(0, largura - tamanho_bloco, tamanho_bloco),
              random.randrange(0, altura - tamanho_bloco, tamanho_bloco)]

    while jogo_ativo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_ativo = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    velocidade_x = -tamanho_bloco
                    velocidade_y = 0
                elif evento.key == pygame.K_RIGHT:
                    velocidade_x = tamanho_bloco
                    velocidade_y = 0
                elif evento.key == pygame.K_UP:
                    velocidade_x = 0
                    velocidade_y = -tamanho_bloco
                elif evento.key == pygame.K_DOWN:
                    velocidade_x = 0
                    velocidade_y = tamanho_bloco

        # Atualiza a posição da cobra
        cobra[0][0] += velocidade_x
        cobra[0][1] += velocidade_y

        # Verifica se a cobra colidiu com as bordas
        if cobra[0][0] < 0 or cobra[0][0] >= largura or cobra[0][1] < 0 or cobra[0][1] >= altura:
            jogo_ativo = False

        # Verifica se a cobra colidiu consigo mesma
        for segmento in cobra[1:]:
            if cobra[0] == segmento:
                jogo_ativo = False

        # Verifica se a cobra comeu a comida
        if cobra[0] == comida:
            comida = [random.randrange(0, largura - tamanho_bloco, tamanho_bloco),
                      random.randrange(0, altura - tamanho_bloco, tamanho_bloco)]
        else:
            # Remove a última parte da cauda para manter o tamanho constante
            cobra.pop()

        # Desenha a tela
        tela.fill(preto)
        desenhar_cobra(cobra, tamanho_bloco)
        pygame.draw.rect(tela, vermelho, [comida[0], comida[1], tamanho_bloco, tamanho_bloco])

        # Atualiza a tela
        pygame.display.update()

        # Controla a taxa de atualização
        relogio.tick(velocidade)

    pygame.quit()

# Inicia o jogo
jogo()