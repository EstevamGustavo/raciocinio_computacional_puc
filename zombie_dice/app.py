from game import Game
from player import Player
from dices import Tube
import sys

playerNumber = int(input("How many players? 2 ~ * "))

if playerNumber < 2:
    print("número mínimo de jogadores não atingido pare de ser solitário e ache um amiguinho!!!")
    sys.exit()

players = []

for x in range(0, playerNumber):
    namePlayer = input(f"Nome do Jogador {x + 1}? ")
    players.append(Player(namePlayer))

game = Game()
game.addPlayers(players)
