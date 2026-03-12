from classes import Jogador
from classes import Time

sahur = Jogador("sahur", 1, 18, 12234555, "gabuim")

garopaba_mulets = Time("garopaba mulets", 1, "basquete", "jpg", "historico legal" )

garopaba_mulets.adicionarJogador(sahur)

print(garopaba_mulets.apresentar_jogadores())