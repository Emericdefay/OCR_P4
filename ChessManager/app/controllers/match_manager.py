from app.models.match import Match
from app.models.player import Player


class MatchManager:
    """
    DESCRIPTION
    """
    def __init__(self):
        """
        DESCRIPTION
        """
        self.matches = []
        self.players_playing = []
        pass

    def set_matches(self, id_match, player_a, player_b):
        """
        DESCRIPTION

        :param id_match:
        :param player_a:
        :param player_b:
        """

        self.matches.append(Match(id_match, player_a, player_b))
        self.players_playing.append(player_a)
        self.players_playing.append(player_b)
        pass

    def match_winner(self, player):
        """"""
        player.points = 1
        pass

    def match_looser(self, player):
        """"""
        player.points = 0
        pass

    def match_equality(self, player_a, player_b):
        """"""
        player_a.points = 0.5
        player_b.points = 0.5
        pass

    def match_done(self, player_a, player_b):
        """"""
        player_a.match_passed = player_b.id_player
        player_b.match_passed = player_a.id_player
        pass

    def round_done(self):
        """"""
        self.matches = []
        pass

    @property
    def playing(self):
        """"""
        return self.players_playing

    @playing.getter
    def playing(self):
        """"""
        return self.players_playing

    @playing.setter
    def playing(self, var):
        self.players_playing = var
