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
        pass

    def __repr__(self):
        attr_a = self.player_a.player_attributes[0]
        attr_b = self.player_b.player_attributes[0]
        return f"ID Match={self.id_match} : {attr_a} vs {attr_b}"

    def __del__(self):
        del self
