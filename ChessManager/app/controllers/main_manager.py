from .player_manager import PlayerManager
from .tournament_manager import TournamentManager
from .match_manager import MatchManager
from .round_manager import RoundManager


class MainManager:
    """

    """
    def __init__(self, number_players):
        """

        """
        # Composition
        self.players_management = PlayerManager()
        self.tournament = object
        self.matches_management = MatchManager()
        self.round_management = RoundManager()

        # Attributes
        self.number_players = number_players
        self.check_first_round = True
        self.offset_players = 0
        self.list_compatible = []
        self.number_matches = 0
        self.number_rounds = 0

        # Initialisation
        self.generate_tournament()
        self.generate_players()
        self.generate_pairs()

        pass

    def generate_tournament(self):
        """
        1. Creating tournament
        """
        ;"""|!|"""
        print("\nCreating tournament :")
        self.tournament = TournamentManager()
        ;"""|!|"""
        print(self.tournament.event.config_tournament)

    def generate_players(self):
        """
        2. Add players
        """
        ;"""|!|"""
        print("\nCreating players :")

        for i in range(self.number_players):
            self.players_management.create_player()

        ;"""|!|"""
        for player in self.players_management.players:
            ;"""|!|"""
            print(player.__repr__())

    def generate_pairs(self):
        """
        3. Create matches
        """
        self.players_management.sort_players()

        if self.check_first_round:
            for player in self.players_management.players:
                if player.points > 0:
                    self.check_first_round = False
                    break
        if self.check_first_round:
            number_matches = len(self.players_management.players)//2
            for i in range(number_matches):
                player_a = self.players_management.players[i]
                player_b = self.players_management.players[i + number_matches]
                self.matches_management.set_matches(i, player_a, player_b)

        else:
            self.matches_management.matches = []
            number_matches = len(self.players_management.players)//2

            list_player = self.players_management.players.copy()
            self.list_compatible = []

            pointer = self.offset_players

            for i in range(number_matches):
                player_a = list_player.pop(0)
                for j in range(pointer, len(list_player)):
                    if player_a.player_attributes[0] in list_player[j].match_passed:
                        if len(list_player) <= 2:
                            self.offset_players += 1
                            self.generate_pairs()
                        if self.offset_players > len(self.players_management.players) - 1:
                            raise ArithmeticError("Must redefine algo!")
                        pass
                    else:
                        player_b = list_player.pop(j)
                        break
                pointer = 0
                self.list_compatible.append(player_a)
                self.list_compatible.append(player_b)

        for i in range(len(self.list_compatible)//2):
            player_a = self.list_compatible[i*2]
            player_b = self.list_compatible[i*2+1]
            self.matches_management.set_matches(i, player_a, player_b)

        self.offset_players = 0

        for player in self.players_management.players:
            if player not in self.matches_management.playing:
                player.points = 1
        self.matches_management.playing = []

        ;"""|!|"""
        print("")
        if self.number_rounds > 0:
            """|!|"""
            print(f"Round n°{self.number_rounds} :")
            """|!|"""
            for player in self.players_management.players:
                """|!|"""
                print(player)

    def match_result(self, id_match, test=None):
        for index, match in enumerate(self.matches_management.matches):
            if id_match == match.id_match:
                # points
                player_a = match.player_a
                player_b = match.player_b

                if test is None:
                    choice = str(input(f"Who win? {player_a}:0 or {player_b}:1 or equal:2."))
                else:
                    choice = str(test)

                if choice == "0":
                    self.matches_management.match_winner(player_a)
                    self.matches_management.match_looser(player_b)
                elif choice == "1":
                    self.matches_management.match_winner(player_b)
                    self.matches_management.match_looser(player_a)
                else:
                    self.matches_management.match_equality(player_a, player_b)

                self.matches_management.match_done(player_a, player_b)
                self.matches_management.matches.pop(index)
        self.number_matches += 1

        if self.number_matches > 3:
            self.number_rounds += 1
            self.number_matches = 0
