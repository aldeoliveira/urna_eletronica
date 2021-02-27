from .Partido import Partido


class PartidosController:

    partido_model = None

    def __init__(self):
        self.partido_model = Partido()

    def registrar_partido(self, dict_partido):
        # dict_partido = {'numero': 'numero do partido', 'nome': 'nome do partido'}
        status = self.partido_model.inserir_partido(dict_partido)
        return status

    def apagar_todos_partidos(self):
        status = self.partido_model.deletar_todos_partidos()
        return status

    def listar_todos_partidos(self):
        lista_partidos = self.partido_model.listar_todos_partidos()
        return lista_partidos

    def apagar_partido(self, partido):
        status = self.partido_model.deletar_partido(partido)
        return status
