from database.QueryBuilder import QueryBuilder
from partidos.Partido import Partido


class Candidato:

    querybuilder = None
    partido_model = None

    def __init__(self):
        self.querybuilder = QueryBuilder()
        self.partido_model = Partido()

    nome_tabela_candidatos = "candidatos"
    coluna_numero_partido = "numero_partido"
    coluna_numero_candidato = "numero_candidato"
    coluna_nome_candidato = "nome"

    numero_partido_caracteres = 2
    numero_caracteres = 3
    nome_max_caracteres = 255
    nome_min_caracteres = 1
    max_candidatos_partido = 999

    def inserir_candidato(self, candidato_dict):
        numero_partido = candidato_dict[self.coluna_numero_partido]
        numero_candidato = candidato_dict[self.coluna_numero_candidato]
        nome_candidato = candidato_dict[self.coluna_nome_candidato]
        if not self.partido_model.verificar_norma_numero(numero_partido):
            return "O numero do partido não está de acordo com a norma."
        if not self.verificar_norma_numero(numero_candidato):
            return "O número do candidato não está de acordo a norma."
        if not self.verificar_norma_nome(nome_candidato):
            return "O nome do candidato não está de acordo com a norma."
        if not self.partido_model.verificar_existencia_numero(numero_partido):
            return "Não há um partido registrado com esse número."
        if not self.verificar_existencia_vaga(numero_partido):
            return "Não há vagas nesse partido para um novo candidato."
        if self.verificar_existencia_numero(numero_partido, numero_candidato):
            return "O número de candidato inserido já se encontra no registro."
        self.querybuilder.insert(self.nome_tabela_candidatos, candidato_dict)
        if self.verificar_existencia_registro(candidato_dict):
            return "O candidato foi registrado com sucesso."
        else:
            return "Não foi possível registrar o candidato."

    def deletar_candidato(self, candidato_dict):
        numero_partido = candidato_dict[self.coluna_numero_partido]
        numero_candidato = candidato_dict[self.coluna_numero_candidato]
        if not self.verificar_existencia_registro(candidato_dict):
            return "O candidato não está registrado."
        dict_conditions = {self.coluna_numero_partido: numero_partido, self.coluna_numero_candidato: numero_candidato}
        self.querybuilder.delete_where(self.nome_tabela_candidatos, dict_conditions)
        if not self.verificar_existencia_registro(candidato_dict):
            return "O registro foi apagado com sucesso."
        else:
            return "Não foi possível apagar o registro."

    def deletar_todos_candidatos(self):
        self.querybuilder.delete_all(self.nome_tabela_candidatos)
        if self.querybuilder.count_all(self.nome_tabela_candidatos):
            return "Não foi possível apagar todos os registros."
        else:
            return "Os registros foram apagados com sucesso."

    def verificar_norma_numero(self, numero):
        return numero.isnumeric() and len(numero) == 3 and numero != "000"

    def verificar_norma_nome(self, nome):
        return 0 < len(nome) <= 255

    def verificar_existencia_vaga(self, numero_partido):
        dict_conditions = {self.coluna_numero_partido: numero_partido}
        count = self.querybuilder.count_where(self.nome_tabela_candidatos, dict_conditions)
        return count < self.max_candidatos_partido

    def verificar_existencia_numero(self, numero_partido, numero_candidato):
        dict_conditions = {self.coluna_numero_partido: numero_partido, self.coluna_numero_candidato: numero_candidato}
        count = self.querybuilder.count_where(self.nome_tabela_candidatos, dict_conditions)
        return count

    def verificar_existencia_registro(self, candidato_dict):
        nome = candidato_dict[self.coluna_nome_candidato]
        numero_candidato = candidato_dict[self.coluna_numero_candidato]
        numero_partido = candidato_dict[self.coluna_numero_partido]
        colunas = self.coluna_nome_candidato
        dict_conditions = {self.coluna_numero_partido: numero_partido, self.coluna_numero_candidato: numero_candidato}
        candidato = self.querybuilder.select_where(self.nome_tabela_candidatos, colunas, dict_conditions)
        if candidato:
            return candidato[0][self.coluna_nome_candidato] == nome
        return False

    def listar_todos_candidatos(self):
        colunas = "{0}, {1}, {2}".format(self.coluna_numero_partido, self.coluna_numero_candidato,
                                         self.coluna_nome_candidato)
        candidatos = self.querybuilder.select_all(self.nome_tabela_candidatos, colunas)
        return candidatos
