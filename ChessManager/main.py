from app.controllers import MainManager
import random
import math


PLAYERS = 6
a = MainManager(PLAYERS)
rounds = int(math.log2(PLAYERS))+1
try:
    for i in range(rounds):
        for j in range(PLAYERS//2):
            test = str(random.randint(0, 2))
            a.match_result(j, test)
        a.generate_pairs()
except ArithmeticError:
    print("The algorithm is incomplete")
except Exception as e:
    print(f"Error : {e}")


a.players_management.sort_players()
print("\nResults finaux :")
for player in a.players_management.players:
    print(player)
