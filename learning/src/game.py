import pygame
import sys

from maps import Maps


class MainGame:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600

        self.maps = Maps()

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.fps = 60

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.clock.tick(self.fps)
        pygame.display.set_caption(str(self.clock.get_fps()))

    def run(self):
        self.maps.generate_map()
        while True:
            self.screen.fill(self.black)
            [sys.exit() for event in pygame.event.get() if event.type == pygame.QUIT or
             pygame.key.get_pressed()[pygame.K_ESCAPE]]
            self.maps.update_screen(self.screen)
            pygame.display.update()


if __name__ == "__main__":
    game = MainGame()
    game.run()
