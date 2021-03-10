# Local application imports
from app.models import Round


class RoundManager:
    """
    Round Manager for a tournament
    """
    def __init__(self):
        """
        Construct the round manager
        """
        self.list_rounds = []
        pass

    def create_round(self, id_round, matches, begin_time, end_time):
        """
        Add a round to a list of round.

        :param id_round: ID of a round
        :param matches: List of matches making the round
        :param begin_time: Time when the round start
        :param end_time: Time when rhe round should finish

        :rtype id_round: str
        :rtype matches: list
        :rtype begin_time: str
        :rtype end_time: str
        """
        self.list_rounds.append(Round(id_round, matches, begin_time, end_time))
