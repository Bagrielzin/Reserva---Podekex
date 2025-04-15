from player.baralho import Baralho
from player.jogador import Jogador
from pokemons.basico import Basico
from pokemons.prism_star import Prism_Star
from pokemons.v_max import V_max

from services.chamar_sistema_de_troca import ChamarSistemaDeTroca

troca = ChamarSistemaDeTroca()

j1 = Jogador("admin", "abc123", troca)

pikachu = Basico(
    hp= 50,
    skill= "Thunder Shock!",
    description= "Yellow rat",
    type= "Electric",
    name= "Pikachu",
    viewed= True,
    on_deck= True
)

charizard = Prism_Star(
    hp= 150,
    skill= "Flamethrower!",
    description= "Powerfull orange dragon",
    type= "Fire/Flying",
    name= "Charizard",
    viewed= True,
    on_deck= True,
)

magikarp = V_max(
    hp= 10,
    skill= "Splash!",
    description= "Useless fish",
    type= "Water",
    name= "Magikarp",
    viewed= True,
    on_deck= False,
    v_power= 2
)

if j1._Jogador__autenticacao.realizar_autenticacao():
    j1.mostrar_tudo()
    j1._Jogador__baralho.adicionar_carta(pikachu)
    j1._Jogador__baralho.adicionar_carta(charizard)

    j1._Jogador__baralho.mostrar_baralho()
