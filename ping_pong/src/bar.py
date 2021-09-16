import math
import pygame


class Bar:

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()

        self.rect1 = pygame.Rect(self.settings.x_left, self.settings.y,
                                 self.settings.b_width, self.settings.b_height)

        self.rect2 = pygame.Rect(self.settings.x_right, self.settings.y,
                                 self.settings.b_width, self.settings.b_height)

        self.up, self.down = False, False
        self.mag1, self.mag2 = False, False

    def distance(self, ball):
        x1 = ball.x - self.rect1.x
        y1 = ball.y - self.rect1.y
        mag1 = math.sqrt(x1 ** 2 + y1 ** 2)

        x2 = ball.x - self.rect2.x
        y2 = ball.y - self.rect2.y
        mag2 = math.sqrt(x2 ** 2 + y2 ** 2)

        if mag1 < mag2:
            self.mag1 = True
            self.mag2 = False
            return mag1
        if mag1 > mag2:
            self.mag2 = True
            self.mag1 = False
            return mag2

    def move(self, ball):
        self.distance(ball)

        if self.mag1:
            if self.down and self.rect1.bottom <= self.screen_rect.bottom:
                self.rect1.y += 5
            elif self.up and self.rect1.y > 0:
                self.rect1.y -= 5
        elif self.mag2:
            if self.down and self.rect2.bottom <= self.screen_rect.bottom:
                self.rect2.y += 5
            elif self.up and self.rect2.y > 0:
                self.rect2.y -= 5

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.red, self.rect1)
        pygame.draw.rect(self.screen, self.settings.white, self.rect2)
