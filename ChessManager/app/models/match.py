class Match:
    """
    DESCRIPTION
    """
    def __init__(self, id_match, player_a, player_b):
        """
        DESCRIPTION

        :param id_match:
        :param player_a:
        :param player_b:
        """
        self.id_match = id_match
        self.player_a = player_a
        self.player_b = player_b
        self.status = "Game in progress..."
        pass

    def set_winner(self, control):
        if control == "0":
            self.status = f"{self.player_a.player_attributes[0]} won."
        elif control == "1":
            self.status = f"{self.player_b.player_attributes[0]} won."
        else:
            self.status = " Equality"

    def __repr__(self):
        attr_a = self.player_a.player_attributes[0]
        attr_b = self.player_b.player_attributes[0]
        return f"ID Match={self.id_match} : {attr_a} vs {attr_b} : {self.status}"

    def __del__(self):
        del self
