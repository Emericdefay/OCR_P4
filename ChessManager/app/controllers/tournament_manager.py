from app.models import Tournament


class TournamentManager:
    """

    """
    def __init__(self, id_tournament):
        """

        """
        self.id_tournament = id_tournament
        self.event = object
        self.create_tournament()
        pass

    def create_tournament(self, manual=False):

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
        """"""
        self.event.rounds.append(list_matches)

    def add_players(self, list_players):
        """"""
        self.event.players.append(list_players)
