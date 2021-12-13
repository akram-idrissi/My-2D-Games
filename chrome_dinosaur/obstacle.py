import pygame
import random


class Obstacle:
    def __init__(self, screen, settings, background):
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()
        self.background = background

        self.obstacles = [pygame.image.load("assets/Cactus/LargeCactus1.png"),
                          pygame.image.load("assets/Cactus/LargeCactus2.png"),
                          pygame.image.load("assets/Cactus/LargeCactus3.png"),
                          pygame.image.load("assets/Cactus/SmallCactus1.png"),
                          pygame.image.load("assets/Cactus/SmallCactus1.png"),
                          pygame.image.load("assets/Cactus/SmallCactus2.png"),
                          pygame.image.load("assets/Cactus/SmallCactus3.png"),
                          ]

        self.image = random.choice(self.obstacles)
        self.rect = self.image.get_rect()
        self.rect.x = 2404

    def change_image(self):
        if self.rect.right < self.screen_rect.left:
            self.image = random.choice(self.obstacles)
            self.rect = self.image.get_rect()
            self.rect.x = 2404

    def draw(self):
        if self.rect.height == 71:
            y = 242
        else:
            y = 218

        self.rect.y = y
        self.screen.blit(self.image, self.rect)
        self.rect.x -= self.settings.speed
        self.change_image()
