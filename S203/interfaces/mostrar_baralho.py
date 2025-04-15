from abc import ABC, abstractmethod
from mostrar import Mostrar

class Mostrar_baralho(Mostrar, ABC):
    @abstractmethod
    def mostrar_baralho(self, cartas):
        pass