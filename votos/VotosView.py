import pygame
from VotosController import VotosController
from Tela import Tela
from Teclado import Teclado

FPS = 15
WIDTH = 1024
HEIGHT = WIDTH//2

URNA_WIDTH = WIDTH
URNA_HEIGHT = HEIGHT
URNA_TOPLEFT = (0, 0)

PROPORCAO_DISPLAY = 3/5
PROPORCAO_TECLADO = 1 - PROPORCAO_DISPLAY

PRETO = pygame.Color("black")
BRANCO = pygame.Color("white")
AMARELO = pygame.Color("yellow")
VERDE = pygame.Color("green")
DARK_GREY = pygame.Color("dark grey")
LIGHT_GREY = pygame.Color("light grey")


class VotosView:
    """
    Gerencia os inputs do eleitor.
    """

    running = None
    dict_botoes = {}
    numeros_inseridos = []
    urna = None
    teclado = Teclado()
    tela = Tela()
    votos_controller = VotosController()

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
        screen.fill(pygame.Color("black"))
        self.running = True
        self.dict_botoes = self.obter_botoes()
        while self.running:
            self.desenhar_interface(screen)
            self.eleitor_inputs()
            pygame.time.Clock().tick(FPS)
            pygame.display.flip()

    def eleitor_inputs(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.left_click(pos)

    def left_click(self, pos):
        for nome_botao in self.dict_botoes.keys():
            botao = self.dict_botoes[nome_botao]
            rect_botao = botao.rect_botao
            if pygame.Rect.collidepoint(rect_botao, pos):
                self.clicou_botao(nome_botao)

    def clicou_botao(self, nome_botao):
        if nome_botao.isnumeric():
            numero = nome_botao
            self.incluir_numero(numero)
        elif nome_botao == 'Branco':
            self.clicou_branco()
        elif nome_botao == 'Corrige':
            self.clicou_corrige()
        elif nome_botao == 'Confirma':
            self.clicou_confirma()

    def incluir_numero(self, numero):
        if len(self.numeros_inseridos) < 5:
            self.numeros_inseridos.append(int(numero))
            self.atualizar_numeros_na_tela(self.numeros_inseridos)
        if self.numeros_inseridos == 5:
            self.exibir_dados()

    def clicou_branco(self):
        votos_controller = VotosController.VotosController()
        voto_branco = [0, 0, 0, 0, 0]
        votos_controller.registrar_voto(voto_branco)

    def clicou_corrige(self):
        self.numeros_inseridos = []
        self.atualizar_numeros_na_tela(self.numeros_inseridos)

    def clicou_confirma(self):
        votos_controller = VotosController.VotosController()
        if len(self.numeros_inseridos) == 5:
            votos_controller.registrar_voto(self.numeros_inseridos)
            self.reset()

    def reset(self):
        self.numeros_inseridos = []
        self.tela.resetar_tela()

    def desenhar_interface(self, screen):
        self.desenhar_urna(screen)
        self.tela.desenhar_tela(screen)
        self.teclado.desenhar_teclado(screen)

    def desenhar_urna(self, screen):
        posicao = URNA_TOPLEFT
        dimensoes = (URNA_WIDTH, URNA_HEIGHT)
        urna_cor = pygame.Color("light grey")
        pygame.draw.rect(screen, urna_cor, pygame.Rect(posicao, dimensoes))

    def obter_botoes(self):
        self.teclado.instanciar_botoes()
        return self.teclado.dict_botoes

    def exibir_dados(self):
        nome_candidato, nome_partido = self.votos_controller.buscar_dados(self.numeros_inseridos)
        print(nome_candidato, nome_partido)
        self.exibir_nome_partido(nome_partido)
        self.exibir_nome_candidato(nome_candidato)

    def atualizar_numeros_na_tela(self, numeros):
        self.tela.numeros_em_exibicao = numeros

    def exibir_nome_partido(self, nome):
        self.tela.nome_do_partido = nome

    def exibir_nome_candidato(self, nome):
        self.tela.nome_do_candidato = nome


votos_view = VotosView()
votos_view.main()
