import pygame

from ball import Ball
from bar import Bar
import general as gn
from settings import Settings


pygame.init()

st = Settings()
screen = pygame.display.set_mode((st.width, st.height))
screen_rect = screen.get_rect()
bar = Bar(screen, st)
ball = Ball(screen, st)

clock = pygame.time.Clock()
pygame.display.set_caption("Ping-Pong")

while True:

    gn.events(bar)
    screen.fill(st.white)
    screen.blit(st.background, st.background_rect)

    bar.move(ball)
    bar.draw()

    gn.move(ball)
    gn.ball_collisions(ball, bar, screen_rect)
    ball.draw()

    pygame.display.update()
    clock.tick(st.fps)
