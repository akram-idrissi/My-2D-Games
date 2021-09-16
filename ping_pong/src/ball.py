import pygame


class Ball:

    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings

        self.v_x = 3
        self.v_y = 3

        self.x = self.settings.hw
        self.y = self.settings.hh

        self.rect = pygame.Rect(self.x, self.y, self.settings.radius, self.settings.width)

    def draw(self):
        pygame.draw.circle(self.screen, self.settings.white, (self.x, self.y),
                           self.settings.radius, self.settings.width)
