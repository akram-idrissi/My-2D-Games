import pygame


class GameMap:

    def __init__(self):
        self.room_map = [[1, 1, 1, 1, 1],
                         [1, 0, 0, 0, 1],
                         [1, 0, 1, 0, 1],
                         [1, 0, 0, 0, 1],
                         [1, 0, 0, 0, 1],
                         [1, 0, 0, 0, 1],
                         [1, 1, 1, 1, 1]
                         ]

        self.room_width = 5
        self.room_height = 7

        self.top_left_x = 100
        self.top_left_y = 150

    def draw(self, screen):

        floor = pygame.image.load("../images/floor.png")
        pillar = pygame.image.load("../images/pillar.png")
        images = [floor, pillar]

        for y in range(self.room_height):
            for x in range(self.room_width):
                image_to_draw = images[self.room_map[y][x]]
                screen.blit(image_to_draw, (self.top_left_x + (x * 30),
                                            self.top_left_y + (y * 30) - image_to_draw.get_height()))
