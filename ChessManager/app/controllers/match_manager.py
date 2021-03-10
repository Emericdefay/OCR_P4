# Local application imports
from app.models.match import Match


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

    def match_winner(self, id_match, control):
        """

        :param id_match:
        :param control:
        :return:
        """
        for match in self.matches:
            if id_match == match.id_match:
                if control == "0":
                    match.player_a.points = 1
                if control == "1":
                    match.player_b.points = 1
                match.set_winner(control)
        pass

    def match_equality(self, id_match, control):
        """

        :param id_match:
        :param control:
        :return:
        """
        for match in self.matches:
            if id_match == match.id_match:
                match.player_a.points = 0.5
                match.player_b.points = 0.5
            match.set_winner(control)
        pass

    def match_done(self, player_a, player_b):
        """

        :param player_a:
        :param player_b:
        :return:
        """
        player_a.match_passed = player_b.id_player
        player_b.match_passed = player_a.id_player
        pass

    def round_done(self):
        """

        :return:
        """
        self.matches = []
        pass

    @property
    def playing(self):
        """

        :return:
        """
        return self.players_playing

    @playing.getter
    def playing(self):
        """

        :return:
        """
        return self.players_playing

    @playing.setter
    def playing(self, var):
        """

        :param var:
        :return:
        """
        self.players_playing = var
