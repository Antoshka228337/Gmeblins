class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1.0
        self.ship_limit = 3

        self.bullet_speed = 10.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.target_height = 120
        self.target_width = 15
        self.target_color = (180, 60,10)

        self.target_speed = 0.5

        self.miss_limit = 3