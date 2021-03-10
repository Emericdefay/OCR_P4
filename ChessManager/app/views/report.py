

class Report:
    """

    """
    def __init__(self, report):
        """

        """
        self.report = report
        pass

    def tournament_created(self):
        print("\n\tTournament created : ")
        print(self.report)

    def players_created(self):
        print("\n\tPlayers created :")
        for player in self.report:
            print(player)

    def show_players(self):
        print("\tTournament's players :")
        for player in self.report:
            print(player)

    def show_number_round(self):
        print(f"\n\tRound n°{self.report} :")

    def show_matches(self):
        print("\n\t Matches just happened:")
        for match in self.report:
            print(match)
