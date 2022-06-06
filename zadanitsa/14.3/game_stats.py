class GameStats:

    def __init__(self, ss_game):
        self.settings = ss_game.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit

        self.num_misses = 0

        self.num_hits = 0
