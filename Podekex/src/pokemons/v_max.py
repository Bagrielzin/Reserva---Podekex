from interfaces.carta import Carta

class V_max(Carta):
    def __init__(self, hp: int, skill: str, description: str, type: str, name: str, viewed: bool, on_deck: bool, v_power: int):
        self.__hp = hp
        self.__skill = skill
        self.__description = description
        self.__type = type
        self.__name = name
        self.__viewed = viewed
        self.__on_deck = on_deck
        self.__v_power = v_power

    def mostrar_carta(self):
        print(f"HP: {self.__hp}")
        print(f"\nHabilidade: {self.__skill}")
        print(f"\nDescricao: {self.__description}")
        print(f"\nTipo: {self.__type}")
        print(f"\nNome: {self.__name}")
        print(f"\nV_power: {self.__v_power}")
        if self.__viewed:
            print("\nPokémon já foi visto")
        else:
            print("\nPokémon não visto")
        if self.__on_deck:
            print("\nPokémon está presente no deck")
        else:
            print("\nPokémon não está no deck")