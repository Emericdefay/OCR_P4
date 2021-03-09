from app.models import Player
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
        self.offset_player1 = 0

        # Initialisation
        self.generate_tournament()
        self.generate_players()
        self.generate_pairs()

        pass

    def generate_tournament(self):
        """
        1. Creating tournament
        """
        print("Creating tournament :")
        self.tournament = TournamentManager()
        print(self.tournament.event.config_tournament)

    def generate_players(self):
        """
        2. Add players
        """
        print("Creating players :")

        for i in range(self.number_players):
            self.players_management.create_player()

        for player in self.players_management.players:
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
            print(self.matches_management.matches)

        else:
            """AJOUTER MATCH DEJA FAIT : MP = ID_autre_joueur """
            self.matches_management.matches = []
            number_matches = len(self.players_management.players)//2
            list_player = self.players_management.players
            for i in range(number_matches):
                player_a = self.players_management.players[i * 2]
                player_b = self.players_management.players[i * 2 + 1]
                pointer = i
                while player_b.player_attributes[0] in player_a.match_passed:
                    pointer += 1
                    if pointer < number_matches:
                        player_b = self.players_management.players[i*2 + pointer]
                    else:
                        raise ValueError("The match is impossible to define.")
                self.matches_management.set_matches(i, player_a, player_b)

        for player in self.players_management.players:
            if player not in self.matches_management.playing:
                player.points = 1
        self.matches_management.playing = []

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

        print("\nMatchs restants : \n")

        for match in self.matches_management.matches:
            print(match)

        print("\nBilan joueurs : \n")
        for player in self.players_management.players:
            print(player)




