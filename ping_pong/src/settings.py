import pygame


class Settings:

    def __init__(self):
        # screen settings
        self.width = 852
        self.height = 480

        self.hw = self.width // 2
        self.hh = self.height // 2

        # colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)

        # frame per seconds
        self.fps = 60

        # background image n path
        self.path = r"..\images\background.jpg"
        self.background = pygame.image.load(self.path)
        self.background_rect = self.background.get_rect()

        # bar settings
        self.offset = 10
        self.b_width = 20
        self.b_height = 120
        self.x_left = self.offset
        self.x_right = self.width - self.b_width - self.offset
        self.y = self.hh - (self.b_height // 2)

        # ball settings
        self.radius = 20
        self.ball_width = 20

        self.sub = 1
        self.move = True
