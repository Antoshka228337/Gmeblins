import sys

import pygame
from putin import Putin
from settings import Settings


class PutinGame:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Легенда двигается ровно")

        self.putin = Putin(self)

    def run_game(self):
        while True:
            self._check_events()
            self.putin.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.putin.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.putin.moving_left = True
        if event.key == pygame.K_UP:
            self.putin.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.putin.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):

        if event.key == pygame.K_RIGHT:
            self.putin.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.putin.moving_left = False
        if event.key == pygame.K_UP:
            self.putin.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.putin.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.putin.blitme()

        pygame.display.flip()


if __name__ == "__main__":
    rg = PutinGame()
    rg.run_game()
