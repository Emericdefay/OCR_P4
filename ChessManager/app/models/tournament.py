class Tournament:
    """
    DESCRIPTION
    """
    def __init__(
            self,
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

        :param name:
        :param number_players:
        :param date:
        :param rounds:
        :param players:
        :param time_control:
        :param description:
        :param number_rounds:

        :rtype name:
        :rtype number_players:
        :rtype date:
        :rtype rounds:
        :rtype players:
        :rtype time_control:
        :rtype description:
        :rtype number_rounds:
        """

        self.name = name
        self.number_players = number_players
        self.date = date
        self.number_rounds = number_rounds
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description
        pass

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
