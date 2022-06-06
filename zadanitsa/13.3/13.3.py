import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite


class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)


class Rain(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.image = pygame.image.load('images/rain.png')
        self.rect = self.image.get_rect()
        self.drop_speed = 1

    def update(self):
        self.rect.y += self.drop_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def get_number_rains_x(settings, rain_width):
    available_space_x = settings.screen_width - rain_width * 2
    number_rains_x = int(available_space_x / (rain_width * 2))
    return number_rains_x


def create_rain(settings, screen, rains, number_rain):
    rain = Rain(settings, screen)
    rain.rect.x = rain.rect.width + 2 * rain.rect.width * number_rain
    rains.add(rain)


def create_rain_group(settings, screen, rains):
    rain = Rain(settings, screen)
    number_rains_x = get_number_rains_x(settings, rain.rect.width)

    for rain_number in range(number_rains_x):
        create_rain(settings, screen, rains, rain_number)


def update_rains(settings, rains):

    rains.update()

    for rain in rains.copy():
        if rain.rect.bottom >= settings.screen_height:
            rains.remove(rain)


def run_rain():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Blood of Ukrainians')
    rains = Group()
    create_rain_group(settings, screen, rains)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(settings.bg_color)
        rains.draw(screen)
        update_rains(settings, rains)
        pygame.display.flip()


run_rain()