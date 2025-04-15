from baralho import Baralho
from interfaces.mostrar_todas_as_cartas import Mostrar_todas_as_cartas
from services.autenticar import Autenticar
from services.chamar_sistema_de_troca import ChamarSistemaDeTroca

class Jogador(Mostrar_todas_as_cartas):
    def __init__(self, login: str, password: str, baralho: Baralho, sistema_troca: ChamarSistemaDeTroca, autenticacao: Autenticar):
        self.login = login
        self.password = password
        self.baralho = baralho
        self.sistema_troca = sistema_troca
        self.autenticacao = Autenticar(login, password)

    def mostrar_tudo(self):
        pass