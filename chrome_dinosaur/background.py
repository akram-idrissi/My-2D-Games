import pygame


class Background:

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load("assets/Other/Track.png")

        # getting the rect and setting its x and y coordinates
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 300

        # holds the previous x position
        self.relative_x = 0

    def scroll(self, speed):
        """Allows the background to scroll to the left infinitely"""
        self.relative_x = self.rect.x % self.rect.width  # 0 <= relative_x <= img width
        self.draw(self.relative_x - self.rect.width, self.rect.y)  # starts drawing an img at the end of the first one

        if self.relative_x < self.settings.width:
            self.draw(self.relative_x, self.rect.y)

        self.rect.x -= speed  # moves the background to the left by the speed

    def draw(self, x, y):
        self.screen.blit(self.image, (x, y))
