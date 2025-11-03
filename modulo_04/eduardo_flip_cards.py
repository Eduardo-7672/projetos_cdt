'''
Primicia - jogo de Cartas Viradas com Pygame

'''

import pygame
# Bibliotecas padrão
import random
# Bibliotecas do sistema
import time
# Bibliotecas do sistema contador
import os
# Bibliteocas de salvamento (pontuação)
import sys
# Função para resolver caminhos de recursos

def resolver_caminho_recurso (caminho_relativo):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath
    return os.path.join(base_path, caminho_relativo)

pygame.init()
LARGURA, ALTURA =800, 600
COR_FUNDO = (20, 20, 20)
COR_TEXTO = (255, 255, 255)

caminho_imagens = "imagens"
NOMES-IMAGENS = [
     "imagem1.png", "imagem2.png", "imagem3.png", 
     "imagem4.png", "imagem5.png", "imagem6.png",
]
VERSO_NOME = "verso.png"


TAMANHO_CARTA = (100, 100)
ALTURA_PLACAR = 50
AREA_JOGO_Y = ALTURA_PLACAR

Caminho_verso = resolver_caminho_recurso(os.path.join(caminho_imagens, VERSO_NOME))
try:
    VERSO_CARTA_IMG = pygame.image.load(caminho_verso)
    VERSO_CARTA_IMG = pygame.transform.scale(imagem_surface, TAMANHO_CARTA)
   except pygame.error as e:
    print(f"ERRO: Não foi possivel carregar o verso da carta: {e}")
    exit()

    dados_imagens = []
    for nome_arquivo in NOMES_IMAGENS:
        img_path = resolver_caminho_recurso(os.path.join(caminho_imagens, nome_arquivo))
        try:
            imagem_surface = pygame.image.load(img_path)
            imagem_surface = pygame.transform.scale(imagem_surface, TAMANHO_CARTA)
            dados_imagens.append((imagem_surface, nome_arquivo))
        except pygame.error as e:
            print(f"AVISO: Imagem {nome_arquivo} não carregada: {e}")

            todas_imagens_com_id = dados_imagens * 2
            random.shuffle(todas_imagens_com_id)


            class Carta:
               def __init__(self, imagem_e_id, x, y):
                   self.imagem_frente = imagem_e_id[0]
                   self.id_par = imagem_e_id[1]
                   self.imagem_Verso = VERSO_CARTA_IMG
                   self.rect = pygame.Rect(x, y, TAMANHO_cARTA[0], TAMANHO_cARTA[1])
                   self.virada = False
                   self.encontrada = False
                   