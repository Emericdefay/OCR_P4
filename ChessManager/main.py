from app.controllers import MainManager
import random
import math


# Tests
PLAYERS = 8
a = MainManager(PLAYERS, 1)
rounds = int(math.log2(PLAYERS))+1
try:
    for i in range(rounds):
        if i > 0:
            a.generate_pairs()
        for j in range(PLAYERS//2):
            test = str(random.randint(0, 2))
            id_match = f"{1}-{i+1}-{j+1}"
            a.match_result(id_match, test, auto=False)
        a.show_matches(id_match)

except ArithmeticError:
    print("The algorithm is incomplete")
except Exception as e:
    print(f"Error : {e}")

a.show_players_by_alpha()

a.players_management.sort_players()
print("\nFinal results :")
for player in a.players_management.players:
    print(player)
