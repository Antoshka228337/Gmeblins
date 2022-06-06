import pygame
import sys
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint


class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 51)


class Star(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.random_number = randint(-10, 10)
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width + self.random_number
        self.rect.y = self.rect.height + self.random_number

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def get_number_star_x(settings, star_width):
    available_space_x = settings.screen_width - 2 * star_width
    number_stars_x = int(available_space_x / (star_width * 2))
    return number_stars_x


def get_number_rows(settings, star_height):
    available_space_y = (settings.screen_height - 2 * star_height)
    number_rows = int(available_space_y / (star_height * 2))
    return number_rows


def create_star(settings, screen, stars, star_number, row_number):
    star = Star(settings, screen)
    star.rect.x = star.rect.x + 2 * star.rect.x * star_number
    star.rect.y = star.rect.y + 2 * star.rect.y * row_number
    stars.add(star)


def create_star_group(settgings, screen, stars):
    star = Star(settgings, screen)
    number_stars_x = get_number_star_x(settgings, star.rect.width)
    number_rows = get_number_rows(settgings, star.rect.height)

    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(settgings, screen, stars, star_number, row_number)


def run_star():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Russia Blows Up America')
    stars = Group()
    create_star_group(settings, screen, stars)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(settings.bg_color)
        stars.draw(screen)
        pygame.display.flip()


run_star()