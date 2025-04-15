from abc import ABC,abstractmethod
from mostrar_carta import Mostrar_carta

class Carta(ABC, Mostrar_carta):
    @abstractmethod
    def mostrar_carta(self,carta):
        pass