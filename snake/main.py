import pygame
import pygame.font
import sys

from apple import Apple
from random import randrange
from settings import Settings
from snake import Snake


class Main:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.RES)

        self.apple = Apple(self.screen, self.settings)
        self.snake = Snake(self.screen, self.settings)

        self.clock = pygame.time.Clock()

    @staticmethod
    def close_window():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def restart(self):
        self.snake.x = randrange(self.settings.SIZE, self.settings.WIDTH - self.settings.SIZE, self.settings.SIZE)
        self.snake.y = randrange(self.settings.SIZE, self.settings.HEIGHT - self.settings.SIZE, self.settings.SIZE)

        self.apple.crd = (randrange(self.settings.SIZE, self.settings.WIDTH - self.settings.SIZE, self.settings.SIZE),
                          randrange(self.settings.SIZE, self.settings.HEIGHT - self.settings.SIZE, self.settings.SIZE))

        self.settings.score = 0
        self.snake.length = 1
        self.settings.fps = 60

    def blit_font(self, text, color, coordinates):
        message = pygame.font.SysFont("", 40)
        message_rect = message.render(text, True, color)
        self.screen.blit(message_rect, coordinates)

    def run(self):
        while True:
            self.screen.fill(self.settings.BLACK)
            self.blit_font(f"fps : {self.settings.fps}", self.settings.LIGHT_YELLOW, (0, 0))
            self.blit_font(f"Your score : {self.settings.score}", self.settings.LIGHT_YELLOW, (0, 40))

            self.close_window()

            if self.snake.collisions():
                while True:
                    self.blit_font("Game Over, click r to play again  or escape to quit", pygame.Color("orange"),
                                   (250, self.settings.HH))

                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_r]:
                        self.restart()
                        break
                    self.close_window()
                    pygame.display.update()

            self.snake.draw()
            self.apple.draw()
            pygame.display.update()
            self.clock.tick(self.settings.fps)

            self.snake.eat(self.apple)
            self.snake.move()
            self.snake.increase()


if __name__ == "__main__":
    app = Main()
    app.run()
