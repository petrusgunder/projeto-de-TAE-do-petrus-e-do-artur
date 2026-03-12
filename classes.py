class Jogador:
    def __init__(self,nome,id,idade,numero_de_telefone,email,historico):
        self.nome = nome
        self.id = id
        self.idade = idade
        self.numero_de_telefone = numero_de_telefone
        self.email = email
        self.historico = []
        

class Time:
    def __init__(self,nome,id,esporte,brasao,historico):
        self.nome = nome
        self.id = id
        self.esporte = esporte
        self.brasao = brasao
        self.jogadores = []
        self.historico = historico
        

    def adicionarJogador (self,jogador):
        self.jogadores.append(jogador)

    def apresentar_jogadores(self):
        nomes = [jogador.nome for jogador in self.jogadores]
        return "Os jogadores são: " + ", ".join(nomes)