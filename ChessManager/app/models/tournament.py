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

        :param id_tournament: ID of the tournament
        :param name: Name of the tournament
        :param number_players: Number of players playing tournament
        :param date: date when the tournament happens
        :param rounds: List of matches realized during tournament
        :param players: List of players playing tournament
        :param time_control: Duration of matches
        :param description: Description of tournament
        :param number_rounds: Number of rounds of tournament (predefine at 4)

        :rtype id_tournament: str
        :rtype name: str
        :rtype number_players: int
        :rtype date: str
        :rtype rounds: list
        :rtype players: list
        :rtype time_control: int
        :rtype description: str
        :rtype number_rounds: int
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
        """
        Simplifying the reading of instance's attributes.
        """
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
        """
        Tournament attributes
        """
        return [self.name,
                self.number_players,
                self.date,
                self.number_rounds,
                self.rounds,
                self.players,
                self.time_control,
                self.description]
