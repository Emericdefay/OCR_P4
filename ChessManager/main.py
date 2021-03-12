from app.controllers import MainManager
from random import randint
import math


# Tests
PLAYERS = 16
TOURNAMENTS = 8


def test_chess_manager(number_players, number_tournaments):
    """Tests for chess_manager."""
    rounds = int(math.log2(number_players)) + 1
    tournaments = []
    for i in range(number_players):
        tournaments.append(MainManager(number_players, i+1))
    # a = MainManager(number_players, number_tournaments)
    for k in range(number_tournaments):
        try:
            for i in range(rounds):
                id_match = ""
                if i > 0:
                    tournaments[k].generate_pairs()
                for j in range(number_players // 2):
                    test = str(randint(0, 2))
                    id_match = f"{k+1}-{i+1}-{j+1}"
                    tournaments[k].match_result(id_match, test, auto=False)
                tournaments[k].show_matches(id_match)
        except ArithmeticError:
            print("The algorithm is incomplete")
        except Exception as e:
            print(f"Error : {e}")

        tournaments[k].show_players_by_alpha()

        tournaments[k].players_management.sort_players()
        print("\nFinal results :")
        for player in tournaments[k].players_management.players:
            print(player)


if __name__ == '__main__':
    test_chess_manager(PLAYERS, TOURNAMENTS)
