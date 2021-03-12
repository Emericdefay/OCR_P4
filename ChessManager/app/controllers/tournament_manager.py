# Local application imports
from app.models import Tournament


class TournamentManager:
    """
    Create a tournament manager
    """
    def __init__(self, id_tournament):
        """
        Construct a tournament manager
        :param id_tournament: ID of the tournament - UNIQUE
        :rtype id_tournament: str
        """
        self.id_tournament = id_tournament
        self.event = object
        self.create_tournament()
        pass

    def create_tournament(self, manual=False):
        """
        Create a tournament, procedurally or manually.
        :param manual: True for procedurally, False for manually.
        :rtype manual: boolean
        """
        if manual:
            name = input("Tournament's name : ")
            number_players = int(input("Number of players : "))
            date = input("Date : ")
            rounds = []
            players = []
            time_control = int(input("Time Control"))
            description = input("Description : ")
            number_rounds = input("Number of rounds : ")
            self.event = Tournament(self.id_tournament,
                                    name,
                                    number_players,
                                    date,
                                    rounds,
                                    players,
                                    time_control,
                                    description,
                                    number_rounds)
        else:
            name = "Best tournament ever seen"
            number_players = int("8")
            date = "20/10/21"
            rounds = []
            players = []
            time_control = int("20")
            description = "Worst description ever seen "
            number_rounds = "4"
            self.event = Tournament(self.id_tournament,
                                    name,
                                    number_players,
                                    date,
                                    rounds,
                                    players,
                                    time_control,
                                    description,
                                    number_rounds)

    def add_rounds(self, list_matches):
        """
        Add a list of matches instances to the tournament.rounds attribute associate
        :param list_matches: list of matches
        :rtype: list
        """
        self.event.rounds.append(list_matches)

    def add_players(self, list_players):
        """
        Add a list of players instances to the tournament.players attribute associate
        :param list_players: List of players for a tournament
        :rtype list_players: list
        """
        self.event.players.append(list_players)
