from cmath import log
from numpy import random


class Game:
    round = 0
    players = []

    def __init__(self):
        pass

    def newRound(self):
        self.round = self.round + 1

    def addPlayers(self, players):
        rang = len(players)
        randPlayers = []
        for x in range(0, rang):
            rand = random.randint(len(players))
            randPlayers.append(players[rand])
            players.pop(rand)

        self.players = randPlayers
        print("Ordem do Jogadores será: ")
        for x in randPlayers:
            print(x.name)

    def initGame(self):
        self.round = 1
        print("Inicio da rodada 1!!")
