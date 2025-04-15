from interfaces.carta import Carta
from interfaces.mostrar_baralho import Mostrar_baralho

class Baralho(Mostrar_baralho):

    def __init__(self):
        self.cartas = []

    def adicionar_carta(self, carta: Carta):
        self.cartas.append(carta)

    def mostrar_baralho(self, cartas):
        pass