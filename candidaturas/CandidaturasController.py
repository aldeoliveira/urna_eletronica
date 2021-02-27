from .Candidatura import Candidatura


class CandidaturasController:

    candidatura_model = None

    def __init__(self):
        self.candidatura_model = Candidatura()

    def registrar_candidatura(self, numero_partido, numero_candidato):
        status = self.candidatura_model.inserir_candidatura(numero_partido, numero_candidato)
        return status

    def remover_candidatura(self, numero):
        pass

    def remover_todas_candidaturas(self):
        pass
