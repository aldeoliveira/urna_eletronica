import pygame
import Botao

PRETO = pygame.Color("black")
BRANCO = pygame.Color("white")
AMARELO = pygame.Color("yellow")
VERDE = pygame.Color("green")
DARK_GREY = pygame.Color("dark grey")
LIGHT_GREY = pygame.Color("light grey")

WIDTH = 1024
HEIGHT = WIDTH//2
URNA_WIDTH = WIDTH
URNA_HEIGHT = HEIGHT
URNA_TOPLEFT = (0, 0)

PROPORCAO_DISPLAY = 3/5
PROPORCAO_TECLADO = 1 - PROPORCAO_DISPLAY

BORDA_EXTERNA = 48
BORDA_INTERNA = 12

TECLADO_POS_X = URNA_WIDTH * PROPORCAO_DISPLAY + BORDA_INTERNA
TECLADO_POS_Y = BORDA_EXTERNA
TECLADO_POSICAO = (TECLADO_POS_X, TECLADO_POS_Y)
TECLADO_DIM_X = URNA_WIDTH * PROPORCAO_TECLADO - (BORDA_INTERNA + BORDA_EXTERNA)
TECLADO_DIM_Y = URNA_HEIGHT - 2 * BORDA_EXTERNA
TECLADO_DIMENSOES = (TECLADO_DIM_X, TECLADO_DIM_Y)

BORDA_TECLADO_X = TECLADO_DIM_X // 10
BORDA_TECLADO_Y = TECLADO_DIM_Y // 10

BORDA_ENTRE_TECLAS = TECLADO_DIM_X // 20

BOTAO_DIMENSAO_X = (TECLADO_DIM_X - BORDA_ENTRE_TECLAS * 4) // 3
BOTAO_DIMENSAO_Y = (TECLADO_DIM_Y - BORDA_ENTRE_TECLAS * 6) // 5
BOTAO_DIMENSOES = (BOTAO_DIMENSAO_X, BOTAO_DIMENSAO_Y)

TAMANHO_FONTE_NUMERICO = 42
TAMANHO_FONTE_OUTRO = 18


class Teclado:

    dict_botoes = {}

    def desenhar_teclado(self, screen):
        teclado_cor = pygame.Color("dark grey")
        teclado = pygame.Rect(TECLADO_POSICAO, TECLADO_DIMENSOES)
        pygame.draw.rect(screen, teclado_cor, teclado)
        self.desenhar_botoes(screen)

    def desenhar_botoes(self, screen):
        for key in self.dict_botoes:
            botao = self.dict_botoes[key]
            botao.desenhar_botao(screen)

    def instanciar_botoes(self):
        classe_botao = Botao.Botao
        dimensoes = BOTAO_DIMENSOES
        tamanho_numerico = TAMANHO_FONTE_NUMERICO
        tamanho_outro = TAMANHO_FONTE_OUTRO
        posicao = self.calcular_posicao
        self.dict_botoes['1'] = classe_botao(posicao(0, 0), dimensoes, PRETO, '1', tamanho_numerico, BRANCO)
        self.dict_botoes['2'] = classe_botao(posicao(0, 1), dimensoes, PRETO, '2', tamanho_numerico, BRANCO)
        self.dict_botoes['3'] = classe_botao(posicao(0, 2), dimensoes, PRETO, '3', tamanho_numerico, BRANCO)
        self.dict_botoes['4'] = classe_botao(posicao(1, 0), dimensoes, PRETO, '4', tamanho_numerico, BRANCO)
        self.dict_botoes['5'] = classe_botao(posicao(1, 1), dimensoes, PRETO, '5', tamanho_numerico, BRANCO)
        self.dict_botoes['6'] = classe_botao(posicao(1, 2), dimensoes, PRETO, '6', tamanho_numerico, BRANCO)
        self.dict_botoes['7'] = classe_botao(posicao(2, 0), dimensoes, PRETO, '7', tamanho_numerico, BRANCO)
        self.dict_botoes['8'] = classe_botao(posicao(2, 1), dimensoes, PRETO, '8', tamanho_numerico, BRANCO)
        self.dict_botoes['9'] = classe_botao(posicao(2, 2), dimensoes, PRETO, '9', tamanho_numerico, BRANCO)
        self.dict_botoes['0'] = classe_botao(posicao(3, 1), dimensoes, PRETO, '0', tamanho_numerico, BRANCO)
        self.dict_botoes['Branco'] = classe_botao(posicao(4, 0), dimensoes, BRANCO, 'Branco', tamanho_outro, PRETO)
        self.dict_botoes['Corrige'] = classe_botao(posicao(4, 1), dimensoes, AMARELO, 'Corrige', tamanho_outro, PRETO)
        self.dict_botoes['Confirma'] = classe_botao(posicao(4, 2), dimensoes, VERDE, 'Confirma', tamanho_outro, PRETO)

    def calcular_posicao(self, l, c):
        posicao_x = TECLADO_POS_X + BORDA_ENTRE_TECLAS * (c + 1) + BOTAO_DIMENSAO_X * c
        posicao_y = TECLADO_POS_Y + BORDA_ENTRE_TECLAS * (l + 1) + BOTAO_DIMENSAO_Y * l
        posicao = (posicao_x, posicao_y)
        return posicao
