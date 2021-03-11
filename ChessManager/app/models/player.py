class Player:
    """
    Player subscribe to a chess tournament
    """
    def __init__(self, id_player: str, last_name: str, first_name: str, birthday: str, sex: str, elo: int):
        """
        Creating a player

        :param id_player: ID of the player, UNIQUE
        :param last_name: last name's player
        :param first_name: first name's player
        :param birthday: birthday's player
        :param sex: sex's player
        :param elo: elo's player

        :rtype id_player: str
        :rtype last_name: str
        :rtype first_name: str
        :rtype birthday: str
        :rtype sex: str
        :rtype elo: int
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
        """
        Resuming the player by : ID, elo, points, match_passed
        :return: f-string
        """
        return f'{self.id_player}|{self.last_name} {self.first_name}:' \
               f' elo={self.elo}, points = {self._points}, MP={self._match_passed}'

    @property
    def player_attributes(self):
        """
        Get the attributes of the player
        :return: list of player's attributes
        """
        return [self.id_player,
                self.last_name,
                self.first_name,
                self.birthday,
                self.sex,
                self.elo,
                self._points,
                self._match_passed]

    @property
    def match_passed(self):
        """
        Get the <match_passed> list.
        :return: list of str
        """
        return self._match_passed

    @match_passed.setter
    def match_passed(self, id_player):
        """
        Add the <id_player> of the player faced in the <match_passed> list
        :param id_player: The ID of the player faced
        :rtype id_player: str
        """
        self._match_passed.append(id_player)

    @property
    def points(self):
        """
        Get the points of player
        :return: points in float
        """
        return self._points

    @points.setter
    def points(self, point):
        """
        Set the points of player
        :param point: Points given at player
        :rtype point: float
        """
        try:
            self._points += float(point)
        except ValueError as v:
            print(f"Error : {v}. Points must be 0, 0.5 or 1.")
        except Exception as e:
            print(f"Error : {e}")
