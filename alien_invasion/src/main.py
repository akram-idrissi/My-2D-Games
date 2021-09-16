import pygame
from pygame.sprite import Group

from button import Button
from game_stats import GameStats
import general as gf
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship


def run_alien():
    pygame.init()
    bullets = Group()
    alien = Group()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    ship = Ship(screen, game_settings)
    stats = GameStats(game_settings)
    sb = Scoreboard(game_settings, stats, screen)
    play_button = Button(game_settings, screen, "Play")
    gf.create_fleet(game_settings, screen, ship, alien)
    pygame.display.set_caption("Alien Invasion")

    while True:
        gf.check_events(ship, alien, screen, bullets, game_settings, play_button, stats)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(bullets, alien, game_settings, screen, ship, stats, sb)
            gf.update_alien(game_settings, alien, bullets, ship, stats, screen)
        gf.update_screen(game_settings, ship, screen, bullets, alien, play_button, stats, sb)


run_alien()
