from database.QueryBuilder import QueryBuilder


class Partido:

    querybuilder = None

    def __init__(self):
        self.querybuilder = QueryBuilder()

    nome_tabela_partidos = "partidos"
    coluna_numero = "numero"
    coluna_nome = "nome"

    max_partidos = 99
    nome_min_caracteres = 1
    nome_max_caracteres = 99
    numero_caracteres = 2

    def inserir_partido(self, dados_partido):
        numero = dados_partido[self.coluna_numero]
        nome = dados_partido[self.coluna_nome]
        if not self.verificar_existencia_vaga():
            return "Não há vaga para um novo partido."
        if not self.verificar_norma_numero(numero):
            return "O numero inserido não está conforme a norma."
        if not self.verificar_norma_nome(nome):
            return "O nome inserido não está conforme a norma."
        if self.verificar_existencia_numero(numero):
            return "O número inserido já está em uso."
        if self.verificar_existencia_numero(nome):
            return "O nome inserido já está em uso."
        self.querybuilder.insert(self.nome_tabela_partidos, dados_partido)
        if self.verificar_existencia_registro(numero, nome):
            return "O partido foi registrado com sucesso."
        else:
            return "Não foi possível registrar o partido."

    def verificar_existencia_vaga(self):
        count = self.querybuilder.count_all(self.nome_tabela_partidos)
        return count < self.max_partidos

    def verificar_norma_numero(self, numero):
        return numero.isnumeric() and len(numero) == self.numero_caracteres and numero != '00'

    def verificar_norma_nome(self, nome):
        return self.nome_min_caracteres <= len(nome) <= self.nome_max_caracteres

    def verificar_existencia_numero(self, numero):
        dict_condition = {self.coluna_numero: numero}
        count = self.querybuilder.count_where(self.nome_tabela_partidos, dict_condition)
        return count

    def verificar_existencia_nome(self, nome):
        dict_conditions = {self.coluna_nome: nome}
        count = self.querybuilder.count_where(self.nome_tabela_partidos, dict_conditions)
        return count

    def verificar_existencia_registro(self, numero, nome):
        colunas = self.coluna_nome
        dict_conditions = {self.coluna_numero: numero}
        resultado = self.querybuilder.select_where(self.nome_tabela_partidos, colunas, dict_conditions)
        if resultado:
            return resultado[0][self.coluna_nome] == nome
        return False

    def listar_todos_partidos(self):
        colunas = "numero, nome"
        lista_partidos = self.querybuilder.select_all(self.nome_tabela_partidos, colunas)
        return lista_partidos

    def deletar_todos_partidos(self):
        self.querybuilder.delete_all(self.nome_tabela_partidos)
        lista_partidos = self.listar_todos_partidos()
        if not lista_partidos:
            return "Os partidos foram apagados com sucesso."
        else:
            return "Não foi possível apagar todos os partidos."

    def deletar_partido(self, dict_partido):
        numero = dict_partido[self.coluna_numero]
        nome = dict_partido[self.coluna_nome]
        if not self.verificar_existencia_registro(numero, nome):
            return "O partido não consta na lista de registro."
        dict_conditions = {self.coluna_numero: numero}
        self.querybuilder.delete_where(self.nome_tabela_partidos, dict_conditions)
        if not self.verificar_existencia_registro(numero, nome):
            return "O partido foi apagado com sucesso."
        else:
            return "Não foi possível executar a operação."
