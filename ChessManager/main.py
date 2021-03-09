from app.controllers import MainManager
import random
import math


PLAYERS = 8
a = MainManager(PLAYERS)
rounds = int(math.log2(PLAYERS))+1
try:
    for i in range(rounds):
        for j in range(PLAYERS//2):
            test = str(random.randint(0, 2))
            a.match_result(j, test)
        a.generate_pairs()
        for player in a.players_management.players:
            print(player)
except:
    raise

a.players_management.sort_players()
print("\nResults finaux :")
for player in a.players_management.players:
    print(player)