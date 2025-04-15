from interfaces.carta import Carta

class Basico(Carta):
    def __init__(self, hp: int, skill: str, description: str, type: str, name: str, viewed: bool, on_deck: bool):
        self.__hp = hp
        self.__skill = skill
        self.__description = description
        self.__type = type
        self.__name = name
        self.__viewed = viewed
        self.__on_deck = on_deck

    def mostrar_carta(self):
        print(f"HP: {self.hp}")
        print(f"\nHabilidade: {self.skill}")
        print(f"\nDescricao: {self.description}")
        print(f"\nTipo: {self.type}")
        print(f"\nNome: {self.name}")
        if self.viewed:
            print("\nPokémon já foi visto")
        else:
            print("\nPokémon não visto")
        if self.on_deck:
            print("\nPokémon está presente no deck")
        else:
            print("\nPokémon não está no deck")