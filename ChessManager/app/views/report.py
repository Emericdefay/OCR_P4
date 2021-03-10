class Report:
    """
    This class take an object and show it, depending on it nature.
    """
    def __init__(self, report):
        """
        Create an instance with a <report> object.

        :param report: The object show.
        :rtype report: object
        """
        self.report = report
        pass

    def tournament_created(self):
        """
        Print all tournament's characteristics
        """
        print("\n\tTournament created : ")
        print(self.report)

    def players_created(self):
        """
        Print all players created
        Debug tool
        """
        print("\n\tPlayers created :")
        for player in self.report:
            print(player)

    def show_players(self):
        """
        Print all players from a tournament
        """
        print("\tTournament's players :")
        for player in self.report:
            print(player)

    def show_number_round(self):
        """
        Print the current round of a tournament
        """
        print(f"\n\tRound n°{self.report} :")

    def show_matches(self):
        """
        Print matches played during the tournament.
        """
        print("\n\t Matches played:")
        for match in self.report:
            print(match)
