from app.models import Player
import random
from operator import attrgetter


class PlayerManager:
    """

    """
    def __init__(self):
        """

        """
        self.players = []

    def create_player(self, manual=False):
        if manual:
            id_player = input("ID player : ")
            last_name = input("Last name : ")
            first_name = input("First name : ")
            birthday = input("Birthday : ")
            sex = input("Sex : ")
            elo = int(input("elo : "))
            self.players.append(Player(id_player, last_name, first_name, birthday, sex, elo))
        else:
            id_player = str(random.randint(0, 10000))
            last_name = "Doe"+str(random.randint(0, 1000))
            first_name = "John"+str(random.randint(0, 1000))
            birthday = f"{random.randint(1, 28)}/{random.randint(1, 12)}/{random.randint(0, 15)}"
            sex = "m"
            elo = random.randint(0, 3000)
            self.players.append(Player(id_player, last_name, first_name, birthday, sex, elo))

    def sort_players(self):
        self.players = sorted(self.players, key=attrgetter("elo"), reverse=True)
        self.players = sorted(self.players, key=attrgetter("_points"), reverse=True)
