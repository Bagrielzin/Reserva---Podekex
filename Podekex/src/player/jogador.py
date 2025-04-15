from baralho import Baralho
from interfaces.mostrar_todas_as_cartas import Mostrar_todas_as_cartas
from services.autenticar import Autenticar
from services.chamar_sistema_de_troca import ChamarSistemaDeTroca

class Jogador(Mostrar_todas_as_cartas):
    def __init__(self, login: str, password: str, sistema_troca: ChamarSistemaDeTroca):
        self.__login = login
        self.__password = password
        self.__baralho = Baralho()
        self.__sistema_troca = sistema_troca
        self.__autenticacao = Autenticar(self.__login, self.__password)

    def mostrar_tudo(self):
        pass