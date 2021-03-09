class Player:
    """
    DESCRIPTION
    """
    def __init__(self, id_player: str, last_name: str, first_name: str, birthday: str, sex: str, elo: int):
        """
        DESCRIPTION

        :param id_player:
        :param last_name:
        :param first_name:
        :param birthday:
        :param sex:
        :param elo:

        :rtype id_player:
        :rtype last_name:
        :rtype first_name:
        :rtype birthday:
        :rtype sex:
        :rtype elo:
        """
        # Static attributes
        self.id_player = id_player
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.sex = sex
        self.elo = elo
        self._points = 0.0

        # Variable attributes
        self._match_passed = []

    def __repr__(self):
        # return f'Player(id_player={self.id_player}, first_name={self.first_name}, elo={self.elo}, points = {self._points}, MP={self._match_passed})'
        return f'{self.id_player} : elo={self.elo}, points = {self._points}, MP={self._match_passed}'

    @property
    def player_attributes(self):
        return [self.id_player, self.last_name, self.first_name, self.birthday, self.sex, self.elo, self._points, self._match_passed]

    @property
    def match_passed(self):
        """"""
        return self._match_passed

    @match_passed.setter
    def match_passed(self, id_player):
        """"""
        self._match_passed.append(id_player)

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, point):
        try:
            self._points += float(point)
        except:
            raise ValueError("Points have to be 1 or 0.5.")
