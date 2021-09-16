import pygame


class Ship:

    def __init__(self, screen, settings):
        self.screen = screen

        self.img_path = r"../images/ship.bmp"
        self.image = pygame.image.load(self.img_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.settings = settings

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed

        self.rect.centerx = self.center
