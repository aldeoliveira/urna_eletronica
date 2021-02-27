from candidaturas.Candidatura import Candidatura
from database.QueryBuilder import QueryBuilder


class Voto:
    """
    Modelo que armazena o voto.
    """

    querybuilder = None
    candidaturas = None
    nome_tabela = "votos"
    nome_coluna = "numero"

    def __init__(self):
        self.querybuilder = QueryBuilder()
        self.candidaturas = Candidatura()

    def verificar_norma_numero(self, numero):
        pass

    def inserir_voto(self, numero):
        """Método ainda não testado!"""
        if not self.verificar_existencia_candidatura(numero):
            numero = "00000"
        voto_dict = {self.nome_coluna: numero}
        self.querybuilder.insert(self.nome_tabela, voto_dict)

    def verificar_existencia_candidatura(self, numero):
        """Método ainda não testado!"""
        tabela = self.candidaturas.nome_tabela_candidaturas
        coluna_numero = self.candidaturas.coluna_numero
        condicao = {coluna_numero: numero}
        if self.querybuilder.count_where(tabela, condicao):
            return True
        return False

    def obter_nome_candidato(self, numero):
        """Método ainda não testado!"""
        tabela_candidaturas = self.candidaturas.nome_tabela_candidaturas
        coluna_nome_candidato = self.candidaturas.coluna_candidato
        coluna_numero = self.candidaturas.coluna_numero
        dict_condicao = {coluna_numero: numero}
        nome_candidato = self.querybuilder.select_where(tabela_candidaturas, coluna_nome_candidato, dict_condicao)
        return nome_candidato

    def obter_nome_partido(self, numero):
        """Método ainda não testado!"""
        tabela_candidaturas = self.candidaturas.nome_tabela_candidaturas
        coluna_nome_partido = self.candidaturas.coluna_partido
        coluna_numero = self.candidaturas.coluna_numero
        dict_condicao = {coluna_numero: numero}
        nome_partido = self.querybuilder.select_where(tabela_candidaturas, coluna_nome_partido, dict_condicao)
        return nome_partido
