import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для упраления снарядами, выпущенные кораблем."""
    def __init__(self, ai_game):
        """Создает объект снарядов в текущей позиции корабля."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # self.color = self.settings.bullet_color
        self.image = pygame.image.load('images/knife.png')
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает снаряд вверх по экрану."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод снаряда на экран."""
        self.screen.blit(self.image, self.rect)
