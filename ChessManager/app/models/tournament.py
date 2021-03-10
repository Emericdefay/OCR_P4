class Tournament:
    """
    DESCRIPTION
    """
    def __init__(
            self,
            id_tournament: str,
            name: str,
            number_players: int,
            date: str,
            rounds: list,
            players: list,
            time_control: int,
            description: str,
            number_rounds=4 or int):
        """
        DESCRIPTION

        :param id_tournament:
        :param name:
        :param number_players:
        :param date:
        :param rounds:
        :param players:
        :param time_control:
        :param description:
        :param number_rounds:

        :rtype id_tournament:
        :rtype name:
        :rtype number_players:
        :rtype date:
        :rtype rounds:
        :rtype players:
        :rtype time_control:
        :rtype description:
        :rtype number_rounds:
        """

        self.id_tournament = id_tournament
        self.name = name
        self.number_players = number_players
        self.date = date
        self.number_rounds = number_rounds
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description
        pass

    def __repr__(self):
        return f"Tournament : {self.name} | ID : {self.id_tournament}\n" \
               f"Date : {self.date}\n" \
               f"Number of players : {self.number_players}\n" \
               f"Number of rounds : {self.number_rounds}\n" \
               f"Time limit per round : {self.time_control}\n" \
               f"\n" \
               f"Rounds already done : {self.rounds}\n" \
               f"Stats players : {self.players}\n" \
               f"\n" \
               f"{self.description}"

    @property
    def config_tournament(self):
        return [self.name,
                self.number_players,
                self.date,
                self.number_rounds,
                self.rounds,
                self.players,
                self.time_control,
                self.description]
