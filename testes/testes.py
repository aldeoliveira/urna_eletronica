from partidos import PartidosController
from candidatos import CandidatosController
from candidaturas import CandidaturasController
from votos import VotosController

"""
Técnica de testes TDD (Test Driven Development)
 - Cria os testes antes da implementação

Unit test (teste unitário)
 - Testa uma parte do sistema

Integration Test (teste de integração)
 - Testa o sistema inteiro
 - Pode-se testar a comunicação entre sistemas
"""


"""
Incluir funcionalidades
 - Verificar se um número já está sendo usado por um partido
 - Inserir um número e retornar o nome do partido que está usando aquele número
 - Verificar se o número do partido tem dois dígitos
 - Criar um dicionário de mensagens de erro nos modelos
"""

col_numero = "numero"
col_nome = "nome"
col_num_partido = "numero_partido"
col_num_candidato = "numero_candidato"
col_nome_candidato = "nome"

dict_estrategistas = {"numero": "01", "nome": "Estrategistas"}
dict_complicadores = {"numero": "02", "nome": "Complicadores"}
dict_classicos = {"numero": "03", "nome": "Clássicos"}
dict_ofensivos = {"numero": "04", "nome": "Ofensivos"}
dict_inovadores = {"numero": "05", "nome": "Inovadores"}
dict_romanticos = {"numero": "06", "nome": "Românticos"}
num_complicadores = "02"
num_classicos = "03"
num_ofensivos = "04"
num_inovadores = "05"
num_romanticos = "06"

kramnik = {"numero_partido": "01", "numero_candidato": "001", "nome": "Vladimir Kramnik"}
karpov = {"numero_partido": "01", "numero_candidato": "002", "nome": "Anatoly Karpov"}
petrosian = {"numero_partido": "01", "numero_candidato": "003", "nome": "Tigran Petrosian"}
capablanca = {"numero_partido": "01", "numero_candidato": "004", "nome": "José Raul Capablanca"}
nimzowitsch = {"numero_partido": "01", "numero_candidato": "005", "nome": "Aaron Nimzowitsch"}
topalov = {col_num_partido: num_complicadores, col_num_candidato: "001", col_nome_candidato: "Veselin Topalov"}
geller = {col_num_partido: num_complicadores, col_num_candidato: "002", col_nome_candidato: "Efim Geller"}
bronstein = {col_num_partido: num_complicadores, col_num_candidato: "003", col_nome_candidato: "David Bronstein"}
alekhine = {col_num_partido: num_complicadores, col_num_candidato: "004", col_nome_candidato: "Alexander Alekhine"}
morphy = {col_num_partido: num_complicadores, col_num_candidato: "005", col_nome_candidato: "Paul Morphy"}
carlsen = {col_num_partido: num_classicos, col_num_candidato: "001", col_nome_candidato: "Magnus Carlsen"}
anand = {col_num_partido: num_classicos, col_num_candidato: "002", col_nome_candidato: "Vishy Anand"}
fischer = {col_num_partido: num_classicos, col_num_candidato: "003", col_nome_candidato: "Bobby Fischer"}
smyslov = {col_num_partido: num_classicos, col_num_candidato: "004", col_nome_candidato: "Vasily Smyslov"}
rubinstein = {col_num_partido: num_classicos, col_num_candidato: "005", col_nome_candidato: "Akiba Rubinstein"}
kasparov = {col_num_partido: num_ofensivos, col_num_candidato: "001", col_nome_candidato: "Garry Kasparov"}
tal = {col_num_partido: num_ofensivos, col_num_candidato: "002", col_nome_candidato: "Mikhail Tal"}
stein = {col_num_partido: num_ofensivos, col_num_candidato: "003", col_nome_candidato: "Leonid Stein"}
steinitz = {col_num_partido: num_inovadores, col_num_candidato: "001", col_nome_candidato: "Wilhelm Steinitz"}
lasker = {col_num_partido: num_inovadores, col_num_candidato: "002", col_nome_candidato: "Emanuel Lasker"}
botvinnik = {col_num_partido: num_inovadores, col_num_candidato: "003", col_nome_candidato: "Mikhail Botvinnik"}
korchnoi = {col_num_partido: num_inovadores, col_num_candidato: "004", col_nome_candidato: "Viktor Korchnoi"}
ivanchuk = {col_num_partido: num_inovadores, col_num_candidato: "005", col_nome_candidato: "Vasily Ivanchuk"}
anderssen = {col_num_partido: num_romanticos, col_num_candidato: "001", col_nome_candidato: "Adolf Anderssen"}
chigorin = {col_num_partido: num_romanticos, col_num_candidato: "002", col_nome_candidato: "Mikhail Chigorin"}
reti = {col_num_partido: num_romanticos, col_num_candidato: "003", col_nome_candidato: "Richard Réti"}
larsen = {col_num_partido: num_romanticos, col_num_candidato: "004", col_nome_candidato: "Bent Larsen"}
morozevich = {col_num_partido: num_romanticos, col_num_candidato: "005", col_nome_candidato: "Alexander Morozevich"}

partidos = [dict_estrategistas, dict_complicadores, dict_classicos, dict_ofensivos, dict_inovadores, dict_romanticos]
candidatos = [kramnik, karpov, petrosian, capablanca, nimzowitsch, topalov, geller, bronstein, alekhine, morphy,
              carlsen, anand, fischer, smyslov, rubinstein, kasparov, tal, stein, steinitz, lasker, botvinnik, korchnoi,
              ivanchuk, anderssen, chigorin, reti, larsen, morozevich]


def teste_apagar_todos_partidos():
    partido_controller = PartidosController.PartidosController()
    assert partido_controller.apagar_todos_partidos() == "Os partidos foram apagados com sucesso."


def teste_registrar_partido():
    partido = dict_estrategistas
    partido_controller = PartidosController.PartidosController()
    partido_controller.apagar_todos_partidos()
    assert partido_controller.registrar_partido(partido) == "O partido foi registrado com sucesso."


def teste_apagar_partido():
    partido = dict_estrategistas
    partidos_controller = PartidosController.PartidosController()
    partidos_controller.apagar_todos_partidos()
    partidos_controller.registrar_partido(partido)
    assert partidos_controller.apagar_partido(partido) == "O registro do partido foi apagado com sucesso."


def teste_registrar_todos_partidos():
    partidos_controller = PartidosController.PartidosController()
    partidos_controller.apagar_todos_partidos()
    for partido in partidos:
        partidos_controller.registrar_partido(partido)
    assert partidos_controller.listar_todos_partidos() == partidos


def teste_registrar_candidato():
    candidatos_controller = CandidatosController.CandidatosController()
    assert candidatos_controller.registrar_candidato(kramnik) == "O candidato foi registrado com sucesso."


def teste_apagar_candidato():
    candidatos_controller = CandidatosController.CandidatosController()
    assert candidatos_controller.apagar_candidato(kramnik) == "O registro foi apagado com sucesso."


def teste_apagar_todos_candidatos():
    candidatos_controller = CandidatosController.CandidatosController()
    assert candidatos_controller.apagar_todos_candidatos() == "Os registros foram apagados com sucesso."


def teste_registrar_todos_candidatos():
    partidos_controller = PartidosController.PartidosController()
    candidatos_controller = CandidatosController.CandidatosController()
    partidos_controller.apagar_todos_partidos()
    candidatos_controller.apagar_todos_candidatos()
    for partido in partidos:
        partidos_controller.registrar_partido(partido)
    for candidato in candidatos:
        candidatos_controller.registrar_candidato(candidato)
    assert partidos_controller.listar_todos_partidos() == partidos and candidatos_controller.listar_todos_candidatos()\
           == candidatos


def teste_registrar_candidatura():
    candidaturas_controller = CandidaturasController.CandidaturasController()
    candidato = kramnik
    numero_partido = candidato[col_num_partido]
    numero_candidato = candidato[col_num_candidato]
    status = candidaturas_controller.registrar_candidatura(numero_partido, numero_candidato)
    assert status == "A candidatura foi registrada com sucesso."


def teste_registrar_todas_candidaturas():
    candidaturas_controller = CandidaturasController.CandidaturasController()
    status = True
    for candidato in candidatos:
        num_partido = candidato[col_num_partido]
        num_candidato = candidato[col_num_candidato]
        status = candidaturas_controller.registrar_candidatura(num_partido, num_candidato)
        if not (status == "A candidatura foi registrada com sucesso." or
                status == "Já existe uma candidatura com esse número."):
            break
    assert status == "A candidatura foi registrada com sucesso." or\
           status == "Já existe uma candidatura com esse número."


def teste_rodar_urna():
    votos_controller = VotosController.VotosController()
    votos_controller.view()
