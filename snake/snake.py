import pygame

from random import randrange


class Snake:
    def __init__(self, screen, st):
        self.length = 1
        self.settings = st
        self.screen = screen

        self.x = randrange(self.settings.SIZE, self.settings.WIDTH - self.settings.SIZE, self.settings.SIZE)
        self.y = randrange(self.settings.SIZE, self.settings.HEIGHT - self.settings.SIZE, self.settings.SIZE)

        self.crd = [(self.x, self.y)]
        self.dx, self.dy = 0, 0

    def increase(self):
        self.x += self.dx * self.settings.SIZE
        self.y += self.dy * self.settings.SIZE

        self.crd.append((self.x, self.y))
        self.crd = self.crd[-self.length:]

    def eat(self, apple):
        if self.crd[-1] == apple.crd:
            apple.crd = (randrange(self.settings.SIZE, self.settings.WIDTH - self.settings.SIZE, self.settings.SIZE),
                         randrange(self.settings.SIZE, self.settings.HEIGHT - self.settings.SIZE, self.settings.SIZE))
            self.length += 1
            self.settings.score += 1
            self.settings.fps += 1

    def collisions(self):
        if self.x < 0 or self.x > self.settings.WIDTH or self.y < 0 or self.y > self.settings.HEIGHT or \
                len(self.crd) != len(set(self.crd)):
            return True

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.dx, self.dy = 1, 0
        elif keys[pygame.K_LEFT]:
            self.dx, self.dy = -1, 0
        elif keys[pygame.K_UP]:
            self.dx, self.dy = 0, -1
        elif keys[pygame.K_DOWN]:
            self.dx, self.dy = 0, 1

    def draw(self):
        [pygame.draw.rect(self.screen, self.settings.GREEN,
                          (i, j, self.settings.SIZE - 2, self.settings.SIZE - 2)) for i, j in self.crd]
