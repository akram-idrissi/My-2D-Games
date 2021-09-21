import pygame

import general as gn
from game_map import GameMap
from player import Player
from settings import Settings

pygame.init()
game_map = GameMap()
player = Player()
st = Settings()
screen = pygame.display.set_mode((st.width, st.height))

while True:

    gn.events()
    screen.fill(st.black)
    game_map.draw(screen)

    pygame.display.update()