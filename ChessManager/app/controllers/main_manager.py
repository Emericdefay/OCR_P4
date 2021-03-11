# Built-in libraries
import datetime
# Controllers
from .player_manager import PlayerManager
from .tournament_manager import TournamentManager
from .match_manager import MatchManager
from .round_manager import RoundManager
# Views
from app.views import Report


class MainManager:
    """

    """
    def __init__(self, number_players, id_tournament):
        """

        """
        # Composition
        self.players_management = PlayerManager()
        self.tournament = object
        self.matches_management = MatchManager()
        self.round_management = RoundManager()

        # Attributes
        self.id_tournament = id_tournament
        self.number_players = number_players
        self.offset_players = 0
        self.list_compatible = []
        self.number_matches = 0
        self.number_rounds = 1

        # Initialisation
        self.generate_tournament()
        self.generate_players()
        self.generate_pairs()

        pass

    def generate_tournament(self):
        """
        1. Creating tournament
            With an id_tournament, create an instance of TournamentManager.
            And report the tournament created on the terminal.
        """
        self.tournament = TournamentManager(self.id_tournament)
        self.report_create_tournament()

    def generate_players(self):
        """
        2. Add players
        """

        for i in range(self.number_players):
            self.players_management.create_player(auto=True)

        self.report_create_players()

        for player in self.players_management.players:
            self.tournament.add_players(player)

    def generate_pairs(self):
        """
        3. Create matches
        """
        self.players_management.sort_players()

        if self.check_first_round():
            number_matches = len(self.players_management.players)//2
            for i in range(number_matches):
                player_a = self.players_management.players[i]
                player_b = self.players_management.players[i + number_matches]
                id_match = f"{self.id_tournament}-{self.number_rounds}-{i+1}"
                self.matches_management.set_matches(id_match, player_a, player_b)

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
                            return self.generate_pairs()
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
            id_match = f"{self.id_tournament}-{self.number_rounds}-{i+1}"
            self.matches_management.set_matches(id_match, player_a, player_b)

        self.offset_players = 0

        for player in self.players_management.players:
            if player not in self.matches_management.playing:
                player.points = 1
        self.matches_management.playing = []

        if self.number_rounds > 1:
            self.report_players()

        time_beginning = self.get_times()[0]
        time_ending = self.get_times()[1]
        self.round_management.create_round(self.number_rounds,
                                           self.matches_management.matches,
                                           time_beginning,
                                           time_ending)

        self.show_round(self.number_rounds)

    def match_result(self, id_match, test=None, auto=False):
        for index, match in enumerate(self.matches_management.matches):
            if id_match == match.id_match:
                player_a = match.player_a
                player_b = match.player_b

                self.tournament.add_rounds(match)

                if test is None:
                    choice = str(input(f"Who win? {player_a}:0 or {player_b}:1 or equal:2."))
                else:
                    choice = str(test)

                if choice == "0":
                    self.matches_management.match_winner(id_match, choice)
                elif choice == "1":
                    self.matches_management.match_winner(id_match, choice)
                else:
                    self.matches_management.match_equality(id_match, choice)

                self.matches_management.match_done(player_a, player_b)

                if not auto:
                    self.show_match_played(id_match)

                self.matches_management.matches.pop(index)

                if not auto:
                    self.show_match_left()

        self.number_matches += 1

        if self.number_matches > (self.number_players//2) - 1:
            self.number_rounds += 1
            self.number_matches = 0

    def check_first_round(self):
        for player in self.players_management.players:
            if player.points > 0:
                return False
        return True

    def get_times(self):
        time_a = datetime.datetime.now()
        time_a_strf = time_a.strftime("%H:%M:%S - %d/%b/%Y")

        time_added = self.tournament.event.time_control
        minutes_added = datetime.timedelta(minutes=time_added)

        time_b = time_a + minutes_added
        time_b_strf = time_b.strftime("%H:%M:%S - %d/%b/%Y")
        return time_a_strf, time_b_strf

    def report_create_tournament(self):
        Report(self.tournament.event).tournament_created()

    def report_create_players(self):
        Report(self.players_management.players).players_created()

    def report_players(self):
        Report(self.players_management.players).show_players_by_score()

    def report_round_number(self):
        Report(self.number_rounds).show_number_round()

    def show_round(self, id_round):
        Report(self.round_management.list_rounds).show_round(id_round)

    def show_matches(self, id_match):
        # REDEFINE
        Report(self.tournament.event.rounds).show_matches(id_match[:3])

    def show_match_played(self, id_match):
        Report(self.tournament.event.rounds).show_matches(id_match)

    def show_match_left(self):
        Report(self.matches_management.matches).show_matches_left()

    def show_players_by_score(self):
        Report(self.players_management.players).show_players_by_score()

    def show_players_by_alpha(self):
        Report(self.players_management.players).show_player_by_alpha()
