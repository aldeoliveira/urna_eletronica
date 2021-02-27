import pygame

WIDTH = 1024
HEIGHT = WIDTH//2
URNA_WIDTH = WIDTH
URNA_HEIGHT = HEIGHT
URNA_TOPLEFT = (0, 0)

PROPORCAO_DISPLAY = 3/5

BORDA_EXTERNA = 48
BORDA_INTERNA = 12

DISPLAY_POS_X = BORDA_EXTERNA
DISPLAY_POS_Y = BORDA_EXTERNA
DISPLAY_POSICAO = (DISPLAY_POS_X, DISPLAY_POS_Y)
DISPLAY_DIM_X = URNA_WIDTH * PROPORCAO_DISPLAY - (BORDA_EXTERNA + BORDA_INTERNA)
DISPLAY_DIM_Y = URNA_HEIGHT - 2 * BORDA_EXTERNA
DISPLAY_DIMENSOES = (DISPLAY_DIM_X, DISPLAY_DIM_Y)

NUMEROS_DIMENSAO_X = DISPLAY_DIM_X * 0.8
NUMEROS_DIMENSAO_Y = DISPLAY_DIM_Y * 0.2
CENTRO_NUMEROS_Y = DISPLAY_DIM_Y * 0.7
NUMEROS_POSICAO_X = DISPLAY_POS_X + (DISPLAY_DIM_X / 2 - NUMEROS_DIMENSAO_X / 2)
NUMEROS_POSICAO_Y = DISPLAY_POS_Y + (CENTRO_NUMEROS_Y - NUMEROS_DIMENSAO_Y / 2)

NUMEROS_DIMENSOES = (NUMEROS_DIMENSAO_X, NUMEROS_DIMENSAO_Y)
NUMEROS_POSICAO = (NUMEROS_POSICAO_X, NUMEROS_POSICAO_Y)
QUANTIDADE_NUMEROS = 5
ESPESSURA_RETANGULOS = 5
DIST_ENTRE_RETANGULOS = ESPESSURA_RETANGULOS

BRANCO = pygame.Color("White")
DARK_BLUE = pygame.Color("dark blue")

RECUO = DISPLAY_DIM_X / 10
LINHA = DISPLAY_DIM_Y / 10

POSICAO_TEXTO_PARTIDO = (DISPLAY_POS_X + RECUO, DISPLAY_POS_Y + LINHA)
POSICAO_TEXTO_CANDIDATO = (DISPLAY_POS_X + RECUO, DISPLAY_POS_Y + 2*LINHA)


class Tela:

    numeros_em_exibicao = []
    nome_do_candidato = None
    nome_do_partido = None

    def desenhar_tela(self, screen):
        self.desenhar_fundo(screen)
        self.desenhar_numeros(screen)
        self.escrever_nome_partido(screen)
        self.escrever_nome_candidato(screen)

    def desenhar_fundo(self, screen):
        pygame.draw.rect(screen, DARK_BLUE, pygame.Rect(DISPLAY_POSICAO, DISPLAY_DIMENSOES))

    def desenhar_numeros(self, screen):
        retangulo_dim_x = (NUMEROS_DIMENSAO_X - DIST_ENTRE_RETANGULOS * (QUANTIDADE_NUMEROS - 1)) / QUANTIDADE_NUMEROS
        retangulo_dim_y = NUMEROS_DIMENSAO_Y
        for r in range(QUANTIDADE_NUMEROS):
            posicao_x_topleft = NUMEROS_POSICAO_X + retangulo_dim_x * r + DIST_ENTRE_RETANGULOS * r
            posicao_y_topleft = NUMEROS_POSICAO_Y
            dimensoes = (retangulo_dim_x, retangulo_dim_y)
            posicao_topleft = (posicao_x_topleft, posicao_y_topleft)
            rect_retangulo = pygame.Rect(posicao_topleft, dimensoes)
            self.desenhar_retangulo(rect_retangulo, screen)
            posicao_centro = rect_retangulo.center
            fonte = pygame.font.Font('freesansbold.ttf', 40)
            if r+1 <= len(self.numeros_em_exibicao):
                numero = self.numeros_em_exibicao[r]
                numero_objeto = fonte.render(str(numero), True, BRANCO)
                numero_rect = numero_objeto.get_rect()
                numero_rect.center = posicao_centro
                screen.blit(numero_objeto, numero_rect)

    def desenhar_retangulo(self, rect_retangulo, screen):
        pygame.draw.rect(screen, BRANCO, rect_retangulo, ESPESSURA_RETANGULOS)

    def escrever_nome_partido(self, screen):
        if self.nome_do_partido:
            texto = 'partidos: {0}'.format(self.nome_do_partido)
        else:
            texto = 'partidos:'
        posicao_topleft = POSICAO_TEXTO_PARTIDO
        self.exibir_texto(screen, texto, posicao_topleft)

    def escrever_nome_candidato(self, screen):
        if self.nome_do_candidato:
            texto = 'candidatos: {0}'.format(self.nome_do_candidato)
        else:
            texto = 'candidatos:'
        posicao_topleft = POSICAO_TEXTO_CANDIDATO
        self.exibir_texto(screen, texto, posicao_topleft)

    def exibir_texto(self, screen, texto, posicao_topleft):
        fonte = pygame.font.Font('freesansbold.ttf', 28)
        texto_objeto = fonte.render(texto, True, BRANCO)
        rect_texto = texto_objeto.get_rect()
        rect_texto.topleft = posicao_topleft
        screen.blit(texto_objeto, rect_texto)

    def resetar_tela(self):
        self.numeros_em_exibicao = []
        self.nome_do_candidato = []
        self.nome_do_partido = []
