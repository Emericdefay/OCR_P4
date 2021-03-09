from app.controllers import MainManager
import random
import math


PLAYERS = 8
a = MainManager(PLAYERS)
try:
    for i in range(int(math.log2(PLAYERS))):
        for j in range(PLAYERS//2):
            test = str(random.randint(0, 2))
            print("result : "+test)
            a.match_result(j, test)
        a.generate_pairs()
except:
    pass

a.players_management.sort_players()
print(int(math.log2(PLAYERS)))
print("result")
for player in a.players_management.players:
    print(player)