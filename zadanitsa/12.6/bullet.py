import pygame
from pygame.sprite import Sprite
from putin_shoot import PutinShoot


class Bullet(Sprite):

    def __init__(self, ss_game: PutinShoot):
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midright = ss_game.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        if self.rect is not None:
            self.rect.x = int(self.x)

    def draw_bullet(self):
        if self.rect is not None:
            pygame.draw.rect(self.screen, self.color, self.rect)
