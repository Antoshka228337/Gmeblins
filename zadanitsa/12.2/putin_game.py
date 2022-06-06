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
        pygame.display.set_caption("Легенда")

        self.putin = Putin(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.putin.blitme()

            pygame.display.flip()


if __name__ == "__main__":
    bbg = PutinGame()
    bbg.run_game()
