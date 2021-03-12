# Local application imports
from app.models.match import Match


class MatchManager:
    """
    Match manager
    """
    def __init__(self):
        """
        Construct the match manager
        """
        self.matches = []
        self.players_playing = []
        pass

    def set_matches(self, id_match, player_a, player_b):
        """
        Create a match for player_a and player_b

        :param id_match: ID of the match created
        :param player_a: first player
        :param player_b: second player

        :rtype id_match: str
        :rtype player_a: obj
        :rtype player_b: obj
        """

        self.matches.append(Match(id_match, player_a, player_b))
        self.players_playing.append(player_a)
        self.players_playing.append(player_b)
        pass

    def match_winner(self, id_match, control):
        """
        Define the winner of a match

        :param id_match: ID of the match
        :param control: "0": player_a win or "1": player_b win

        :rtype id_match: str
        :rtype control: str
        """
        for match in self.matches:
            if id_match == match.id_match:
                if control == "0":
                    match.player_a.points = 1
                if control == "1":
                    match.player_b.points = 1
                match.set_winner(control)

    def match_equality(self, id_match, control):
        """
        Set an equality for a match

        :param id_match: ID of the equality match
        :param control: "2" for equality

        :rtype id_match: str
        :rtype control: str
        """
        for match in self.matches:
            if id_match == match.id_match:
                match.player_a.points = 0.5
                match.player_b.points = 0.5
            match.set_winner(control)
        pass

    def match_done(self, player_a, player_b):
        """
        Declare the match finished between player_a and player_b

        :param player_a: first player
        :param player_b: second player

        :rtype player_b: obj
        :rtype player_b: obj
        """
        player_a.match_passed = player_b.id_player
        player_b.match_passed = player_a.id_player
        pass

    def round_done(self):
        """
        Empty the matches
        """
        self.matches = []
        pass

    @property
    def playing(self):
        """
        Get the players playing the round
        :return: return the list of players playing during this round.
        """
        return self.players_playing

    @playing.getter
    def playing(self):
        """
        Get the players playing the round
        :return: return the list of players playing during this round.
        """
        return self.players_playing

    @playing.setter
    def playing(self, var):
        """
        Add <var> players to the list players_playing
        :param var: players playing
        :rtype var: obj
        """
        self.players_playing = var
