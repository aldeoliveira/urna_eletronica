from votos.Voto import Voto


class VotosController:

    voto = None

    def __init__(self):
        self.voto = Voto()

    def buscar_dados(self, lista_numeros):
        """Método ainda não testado!"""
        numeros = self.normatizar_numeros(lista_numeros)
        nome_candidato = self.voto.obter_nome_candidato(numeros)
        nome_partido = self.voto.obter_nome_partido(numeros)
        return nome_candidato, nome_partido

    def normatizar_numeros(self, lista_numeros):
        """Método ainda não testado!"""
        n = lista_numeros
        numeros = "{0}{1}{2}{3}{4}".format(n[0], n[1], n[2], n[3], n[4])
        return numeros

    def registrar_voto(self, lista_numeros):
        """Método ainda não testado!"""
        numeros = self.normatizar_numeros(lista_numeros)
        self.voto.inserir_voto(numeros)
