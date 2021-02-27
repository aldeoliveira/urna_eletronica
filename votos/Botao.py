import pygame

FONTE = 'freesansbold.ttf'


class Botao:
    """
    Desenhar os botões do teclado da urna.
    """

    def __init__(self, posicao_topleft, dimensoes, cor_botao, texto_botao, tamanho_texto, cor_texto):
        self.rect_botao = pygame.Rect(posicao_topleft, dimensoes)
        self.cor_botao = cor_botao
        self.texto_botao = texto_botao
        self.tamanho_texto = tamanho_texto
        self.cor_texto = cor_texto

    def desenhar_botao(self, screen):
        pygame.draw.rect(screen, self.cor_botao, self.rect_botao)
        self.desenhar_nome_botao(screen)

    def desenhar_nome_botao(self, screen):
        fonte = pygame.font.Font(FONTE, self.tamanho_texto)
        texto = fonte.render(self.texto_botao, True, self.cor_texto)
        rect_texto = texto.get_rect()
        rect_texto.center = self.rect_botao.center
        screen.blit(texto, rect_texto)
