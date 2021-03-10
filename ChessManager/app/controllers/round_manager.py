from app.models import Round


class RoundManager:
    def __init__(self):
        self.list_rounds = []
        pass

    def create_round(self, id_round, matches, begin_time, end_time):
        self.list_rounds.append(Round(id_round, matches, begin_time, end_time))
