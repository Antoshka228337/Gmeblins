import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centery = self.screen_rect.centery

        # self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        # if self.moving_up and self.rect.top > 0:

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor
        self.rect.centery = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)