import general as gn
import pygame

from obstacle import Obstacle
from player import Player
from settings import Settings
from background import Background

settings = Settings()
screen = pygame.display.set_mode(settings.resolution)

player = Player(screen, settings)
background = Background(screen, settings)
obstacle = Obstacle(screen, settings, background)

ICON = pygame.image.load("assets/DinoWallpaper.png")
ICON = pygame.transform.scale(ICON, (30, 30))
pygame.display.set_icon(ICON)
pygame.display.set_caption("Chrome Dinosaur")

clock = pygame.time.Clock()

while True:
    gn.events(screen, settings, player)
    background.scroll(settings.speed)
    obstacle.draw()
    gn.check_collision(settings, player, obstacle)
    if not settings.game_over:
        player.jump()
        player.animate()
        player.draw()

    if settings.game_over:
        settings.speed = 0
        player.list_frame = 1
        rect = gn.game_over_screen(screen)
        gn.change_dino(player)

    pygame.display.update()
    clock.tick(settings.fps)
