import pygame
import sys


def check_collision(settings, player, obstacle):
    """Returns True if the player collide with the obstacle"""
    if pygame.Rect.colliderect(player.rect, obstacle.rect):
        settings.game_over = True


def game_over_screen(screen):
    """Displays the game over screen"""
    game_over_image = pygame.image.load("assets/Other/GameOver.png")
    game_over_rect = game_over_image.get_rect()
    screen.blit(game_over_image, (500 - (game_over_rect.width // 2), 150))

    game_reset_image = pygame.image.load("assets/Other/Reset.png")
    game_reset_image = pygame.transform.scale(game_reset_image, (60, 80))
    game_reset_rect = game_reset_image.get_rect()
    screen.blit(game_reset_image, (500 - (game_reset_rect.width // 2), 200))
    game_reset_rect.x, game_reset_rect.y = (500 - (game_reset_rect.width // 2), 200)
    return game_reset_rect


def change_dino(player):
    """Changes the player image when game_over is set to True"""
    player.list_frame = 1
    player.animate()
    player.draw()


def events(screen, settings, player):
    screen.fill(settings.bgr_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player.air_timer < settings.up // 2:
                    player.list_frame = 0
                    player.player_y_momentum = -settings.up
