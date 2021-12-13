import pygame
import random
import sys
import time
from settings import Settings

pygame.init()
settings = Settings()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT),0, 32)
display = pygame.Surface((300, 300))
f = open("map.txt", "r")
m = [[int(n) for n in line] for line in f.read().split("\n")]
f.close()

grass_image = pygame.image.load("../images/grass2.png").convert()
grass_image.set_colorkey((0, 0, 0))

while True:
    display.fill(settings.BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    for y, row in enumerate(m):
        for x, column in enumerate(row):
            if column:
                pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(grass_image, (150 + x * 10 - y * 10, 150 + x * 5 + y * 5))
                # display.blit(grass_image, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5))
                # if random.randint(0, 1):
                #     display.blit(grass_image, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5 - 14))

    screen.blit(pygame.transform.scale(display, (settings.WIDTH, settings.HEIGHT)), (0, 0))

    pygame.display.update()
    time.sleep(1)
