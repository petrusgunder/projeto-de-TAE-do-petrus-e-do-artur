from classes import Jogador
from classes import Time
from classes import Organizador
from classes import Campeonato

sahur = Jogador("sahur", 1, 18, 12234555, "gabuim")
arthut = Jogador("arthur", 2, 29, 38593859385983, "xaulin")
guilherme = Jogador("guilherme",3,43,2412341343,"jao")

garopaba_mulets = Time("garopaba mulets", 1, "basquete", "jpg", "historico legal" )

thiago_paes = Organizador("thiago", 1,"48 1164 5500" )

jifsc = Campeonato("jifsc", "basquete")
jesc = Campeonato("jesc", "handboll")

garopaba_mulets.adicionarJogador(sahur)
garopaba_mulets.adicionarJogador(arthut)
garopaba_mulets.adicionarJogador(guilherme)

thiago_paes.adicionarCampeonato(jifsc)
thiago_paes.adicionarCampeonato(jesc)

print(garopaba_mulets.apresentar_jogadores())

print(" nova linha so para separar as coisas e ver que esta certo o codigo")

garopaba_mulets.removerJogadores(sahur)

print(garopaba_mulets.apresentar_jogadores())

print(thiago_paes.ApresentarCampeonatos())