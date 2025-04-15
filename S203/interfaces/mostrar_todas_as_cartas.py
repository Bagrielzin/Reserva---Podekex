from abc import ABC,abstractmethod
from mostrar import Mostrar

class Mostrar_todas_as_cartas(Mostrar, ABC):
    @abstractmethod
    def mostrar_tudo(self):
        pass