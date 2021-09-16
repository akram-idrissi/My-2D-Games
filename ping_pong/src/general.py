import pygame
import sys


def events(bar):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_UP:
                bar.up = True
            elif event.key == pygame.K_DOWN:
                bar.down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_UP:
                bar.up = False
            elif event.key == pygame.K_DOWN:
                bar.down = False


def move(ball):
    ball.x += ball.v_x
    ball.y += ball.v_y


def ball_collisions(ball, bar, screen_rect):
    if ball.x <= bar.rect1.right + 20:
        ball.v_x = 3
    elif ball.x >= bar.rect2.left - 20:
        ball.v_x = -3

    if ball.y >= screen_rect.bottom:
        ball.v_y = -3
    if ball.y <= screen_rect.top:
        ball.v_y = 3
