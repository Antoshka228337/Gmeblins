class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует статические настройки игры."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (228, 228, 229)

        self.ship_limit = 3

        self.bullet_width = 80
        self.bullet_height = 80
        # self.bullet_color = (228, 228, 228)
        self.bullets_allowed = 10

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed = 10
        self.bullet_speed = 15.0
        self.alien_speed = 7.0

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
