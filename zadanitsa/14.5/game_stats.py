import json


class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        self.high_score = self.get_saved_high_score()

    def get_saved_high_score(self):
        try:
            with open("high_score.json") as f:
                return json.load(f)
        except FileNotFoundError:
            return 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
