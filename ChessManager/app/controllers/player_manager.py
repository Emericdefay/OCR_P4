# Standard library import
from random import randint
from operator import attrgetter
# Local application imports
from app.models import Player


class PlayerManager:
    """
    Player Manager for the tournament
    """
    def __init__(self):
        """
        Construct the player manager
        """
        self.players = []

    def create_player(self, auto=False):
        """
        Create players procedurally or manually, depending on <auto>.
        :param auto: True: Procedurally, False: Manually
        :rtype auto: boolean
        """
        if not auto:
            id_player = input("ID player : ")
            last_name = input("Last name : ")
            first_name = input("First name : ")
            birthday = input("Birthday : ")
            sex = input("Sex : ")
            elo = int(input("elo : "))
            self.players.append(Player(id_player, last_name, first_name, birthday, sex, elo))
        else:
            id_player = str(randint(0, 10000))
            last_name = "Doe"+str(randint(0, 1000))
            first_name = "John"+str(randint(0, 1000))
            birthday = f"{randint(1, 28)}/{randint(1, 12)}/{randint(0, 15)}"
            sex = "m"
            elo = randint(0, 3000)
            self.players.append(Player(id_player, last_name, first_name, birthday, sex, elo))

    def sort_players(self):
        """
        Sort players firstly by points and secondly by elo.
        """
        self.players = sorted(self.players, key=attrgetter("elo"), reverse=True)
        self.players = sorted(self.players, key=attrgetter("_points"), reverse=True)
