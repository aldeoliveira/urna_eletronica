from .Candidato import Candidato


class CandidatosController:

    candidato_model = None

    def __init__(self):
        self.candidato_model = Candidato()

    def registrar_candidato(self, candidato):
        status = self.candidato_model.inserir_candidato(candidato)
        return status

    def apagar_candidato(self, candidato):
        status = self.candidato_model.deletar_candidato(candidato)
        return status

    def apagar_todos_candidatos(self):
        status = self.candidato_model.deletar_todos_candidatos()
        return status

    def listar_todos_candidatos(self):
        status = self.candidato_model.listar_todos_candidatos()
        return status
