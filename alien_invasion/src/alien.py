import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.img_path = r"../images/alien.bmp"
        self.image = pygame.image.load(self.img_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x = self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x += self.x

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
