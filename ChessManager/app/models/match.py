class Match:
    """
    Match of 2 players, telling if the chess game is in progress or has already took place.
    """
    def __init__(self, id_match, player_a, player_b):
        """
        Create a match between two players

        :param id_match: ID of the match - UNIQUE
        :param player_a: A player instance
        :param player_b: A player instance

        :rtype id_match: str
        :rtype player_a: object
        :rtype player_b: object
        """
        self.id_match = id_match
        self.player_a = player_a
        self.player_b = player_b
        self.status = "Game in progress..."
        pass

    def set_winner(self, control):
        """
        Set the winner of the match

        :param control: "0", "1" or "2" for player_1 win, player_2 win or equality
        :rtype: str
        """
        if control == "0":
            self.status = f"{self.player_a.player_attributes[0]} won."
        elif control == "1":
            self.status = f"{self.player_b.player_attributes[0]} won."
        else:
            self.status = " Equality"

    def __repr__(self):
        """
        Represent Match instance like : <ID_Match> : <ID_player_A> vs <ID_player_B> : <status of the match>
        :return: f-string
        """
        attr_a = self.player_a.player_attributes[0]
        attr_b = self.player_b.player_attributes[0]
        return f"ID Match={self.id_match} : {attr_a} vs {attr_b} : {self.status}"

    @property
    def match(self):
        """
        Return informations of the 2 players of the match
        :return: tuple of 2 lists which has player and his points.
        """
        return tuple([self.player_a, self.player_a.points], [self.player_b, self.player_b.points])
