from operator import attrgetter


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
        print("\nTournament created : ")
        print(self.report)

    def players_created(self):
        """
        Print all players created
        Debug tool
        """
        print("\nPlayers created :")
        for player in self.report:
            print(f"\t{player}")

    def show_players_by_score(self):
        """
        Print all players from a tournament
        """
        print("\nCurrent Player ranking :")
        for player in self.report:
            print(f"\t{player}")

    def show_player_by_alpha(self):
        """
        Print all players by alphabetic order
        """
        self.report = sorted(self.report, key=attrgetter("first_name"), reverse=False)
        self.report = sorted(self.report, key=attrgetter("last_name"), reverse=False)
        print("\nList of players (A-Z):")
        for player in self.report:
            print(f"\t{player}")

    def show_number_round(self):
        """
        Print the current round of a tournament.
        """
        print(f"\n\tRound n°{self.report} :")

    def show_matches(self, id_match):
        """
        Print matches played during the tournament.

        :param id_match: ID of the match, can be incomplete.
        :rtype id_match: str
        """
        print("\nPlayed :")
        for match in self.report:
            if id_match in match.id_match[:len(id_match)]:
                print(f"\t{match}")

    def show_matches_left(self):
        """
        Print matches still in progress
        """
        print('\nLeft :')
        for match in self.report:
            print(f"\t{match}")

    def show_round(self, id_round):
        """
        Print a specific round, happened or in progress

        :param id_round: ID of the round
        :rtype id_round: str
        """
        for one_round in self.report:
            if id_round == one_round.id_round:
                print(f"\n{one_round}")
