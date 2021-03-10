class Round:
    """
    Define Round object
    """
    def __init__(self, id_round: str, matches: list, begin_time: str, end_time: str):
        """
        Constructing the round, need : <id_round>, <matches>, <begin_time> & <end_time>

        :param id_round: ID of the round
        :param matches: The list of the matches happening in this round
        :param begin_time: The time when the round begin
        :param end_time:  The time when the round must end

        :rtype id_round: str
        :rtype matches: list
        :rtype begin_time: str
        :rtype end_time: str
        """
        self.id_round = id_round
        self.matches = matches
        self.begin_time = begin_time
        self.end_time = end_time
        pass
