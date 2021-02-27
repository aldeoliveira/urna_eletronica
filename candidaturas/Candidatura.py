from database.QueryBuilder import QueryBuilder
from partidos.Partido import Partido
from candidatos.Candidato import Candidato


class Candidatura:

    """
    Esta classe guarda as candidaturas para a eleição.
    Cada candidatura contem:
     - Um número de cinco dígitos, que é o número da candidatura, que identifica o votos
     - O nome do candidato, que será mostrado ao eleitor no momento da escolha
     - O nome do partido, que será mostrado ao eleitor no momento da escolha
    """

    querybuilder = None
    partido_model = None
    candidato_model = None
    nome_tabela_candidaturas = "candidaturas"
    coluna_numero = "numero_candidatura"
    coluna_partido = "nome_partido"
    coluna_candidato = "nome_candidato"

    def __init__(self):
        self.querybuilder = QueryBuilder()
        self.partido_model = Partido()
        self.candidato_model = Candidato()
        self.nome_tabela_partidos = self.partido_model.nome_tabela_partidos
        self.nome_tabela_candidatos = self.candidato_model.nome_tabela_candidatos

    def inserir_candidatura(self, numero_partido, numero_candidato):
        # dict_candidatura = {"numero_partido": "--", "numero_candidato": "---"}
        # numero_partido = dict_candidatura[self.coluna_partido]
        # numero_candidato = dict_candidatura[self.coluna_candidato]
        numero_candidatura = self.gerar_numero_candidatura(numero_candidato, numero_partido)
        if self.verificar_coincidencia(numero_candidatura):
            return "Já existe uma candidatura com esse número."
        if not self.verificar_existencia_partido(numero_partido):
            return "Não há um partido no registro com esse número."
        if not self.verificar_existencia_candidato(numero_partido, numero_candidato):
            return "Não há um candidato no registro com esse número."
        nome_partido = self.obter_nome_partido(numero_partido)
        nome_candidato = self.obter_nome_candidato(numero_partido, numero_candidato)
        dict_candidatura = {self.coluna_numero: numero_candidatura, self.coluna_partido: nome_partido,
                            self.coluna_candidato: nome_candidato}
        self.querybuilder.insert(self.nome_tabela_candidaturas, dict_candidatura)
        if self.verificar_presenca_candidatura(dict_candidatura):
            return "A candidatura foi registrada com sucesso."
        else:
            return "Não foi possível registrar a candidatura."

    def gerar_numero_candidatura(self, numero_candidato, numero_partido):
        numero_candidatura = numero_partido + numero_candidato
        return numero_candidatura

    def verificar_coincidencia(self, numero_candidatura):
        dict_conditions = {self.coluna_numero: numero_candidatura}
        count = self.querybuilder.count_where(self.nome_tabela_candidaturas, dict_conditions)
        return count

    def verificar_existencia_partido(self, numero_partido):
        count = self.partido_model.verificar_existencia_numero(numero_partido)
        return count

    def verificar_existencia_candidato(self, numero_partido, numero_candidato):
        count = self.candidato_model.verificar_existencia_numero(numero_partido, numero_candidato)
        return count

    def obter_nome_partido(self, numero):
        coluna_numero = self.partido_model.coluna_numero
        coluna_nome = self.partido_model.coluna_nome
        dict_conditions = {coluna_numero: numero}
        colunas = coluna_nome
        resultado_dict = self.querybuilder.select_where(self.nome_tabela_partidos, colunas, dict_conditions)
        nome_partido = resultado_dict[0][coluna_nome]
        return nome_partido

    def obter_nome_candidato(self, numero_partido, numero_candidato):
        coluna_numero_partido = self.candidato_model.coluna_numero_partido
        coluna_numero_candidato = self.candidato_model.coluna_numero_candidato
        coluna_nome_candidato = self.candidato_model.coluna_nome_candidato
        dict_conditions = {coluna_numero_partido: numero_partido, coluna_numero_candidato: numero_candidato}
        res_dict = self.querybuilder.select_where(self.nome_tabela_candidatos, coluna_nome_candidato, dict_conditions)
        nome_candidato = res_dict[0][coluna_nome_candidato]
        return nome_candidato

    def verificar_presenca_candidatura(self, dict_candidatura):
        count = self.querybuilder.count_where(self.nome_tabela_candidaturas, dict_candidatura)
        return count
