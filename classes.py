class Jogador:
    def __init__(self, nome, id, idade, numero_de_telefone, email):
        self.nome = nome
        self.id = id
        self.idade = idade
        self.numero_de_telefone = numero_de_telefone
        self.email = email
        self.historico = []
        

class Time:
    def __init__(self, nome, id, esporte, brasao, historico):
        self.nome = nome
        self.id = id
        self.esporte = esporte
        self.brasao = brasao
        self.jogadores = []
        self.historico = historico
        
    def adicionarJogador(self, jogador):
        self.jogadores.append(jogador)

    def apresentar_jogadores(self):
        nomes = [jogador.nome for jogador in self.jogadores]
        return "Os jogadores do time " + self.nome + " são: " + ", ".join(nomes) 
    
    def removerJogadores(self, jogador):
        self.jogadores.remove(jogador)


class Campeonato:
    def __init__(self, nome, esporte):
        self.nome = nome
        self.esporte = esporte


class Organizador:
    def __init__(self, nome, id, telefone):
        self.nome = nome
        self.id = id
        self.telefone = telefone
        self.campeonatos = []

    def adicionarCampeonato(self, nome_campeonato):
        self.campeonatos.append(nome_campeonato)

    def RemoverCampeonato(self, nome_campeonato):
        self.campeonatos.remove(nome_campeonato)
    
    def ApresentarCampeonatos(self):   
        nomes_campeonatos = [camp.nome for camp in self.campeonatos]
        return "Os campeonatos são: " + ", ".join(nomes_campeonatos)