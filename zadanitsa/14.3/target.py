import pygame


class Target:

    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = ss_game.settings
        self.color = self.settings.target_color

        self.rect = pygame.Rect(
            0, 0, self.settings.target_width, self.settings.target_height
        )
        self.center_target()

        self.direction = 1

    def update(self):
        self.y += self.direction * self.settings.target_speed

        if self.rect.top < 0:
            self.rect.top = 0
            self.direction = 1
        elif self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom
            self.direction = -1

        self.rect.y = self.y

    def center_target(self):
        self.rect.midright = self.screen_rect.midright

        self.y = float(self.rect.y)

    def draw_target(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
