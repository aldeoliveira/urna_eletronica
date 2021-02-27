from partidos import PartidosController
from testes import Listas

listas = Listas

todos_partidos = [listas.dict_estrategistas, listas.dict_romanticos, listas.dict_inovadores, listas.dict_ofensivos,
                  listas.dict_classicos, listas.dict_complicadores]


def teste_registrar_partido():
    partidos_controller = PartidosController.PartidosController()
    dict_partido = listas.dict_estrategistas
    status = partidos_controller.registrar_partido(dict_partido)
    assert status == "O partido foi registrado com sucesso."


def teste_apagar_todos_partidos():
    partidos_controller = PartidosController.PartidosController()
    status = partidos_controller.apagar_todos_partidos()
    assert status == "Os partidos foram apagados com sucesso."


def teste_listar_todos_partidos():
    partidos_controller = PartidosController.PartidosController()
    partidos_para_listar = partidos_controller.listar_todos_partidos()
    assert partidos_para_listar == []


def teste_apagar_partido():
    partidos_controller = PartidosController.PartidosController()
    registrar_todos_partidos()
    partido_apagar = listas.dict_estrategistas
    partidos_controller.apagar_partido(partido_apagar)
    assert "O partido foi apagado com sucesso."


def registrar_todos_partidos():
    partidos_controller = PartidosController.PartidosController()
    for dict_partido in todos_partidos:
        partidos_controller.registrar_partido(dict_partido)
