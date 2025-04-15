from abc import ABC, abstractmethod
from mostrar import Mostrar

class Mostrar_carta(ABC, Mostrar):
    @abstractmethod
    def mostrar_carta(self, carta):
        pass