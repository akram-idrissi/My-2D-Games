import pygame

from random import randrange


class Apple:
    def __init__(self, screen, settings):
        self.settings = settings
        self.screen = screen
        self.crd = (randrange(self.settings.SIZE, self.settings.WIDTH - self.settings.SIZE, self.settings.SIZE),
                    randrange(self.settings.SIZE, self.settings.HEIGHT - self.settings.SIZE, self.settings.SIZE))

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.RED,
                         (self.crd[0], self.crd[1], self.settings.SIZE, self.settings.SIZE))
