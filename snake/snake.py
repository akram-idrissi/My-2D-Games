import pygame
import pygame.font
import sys

from random import randrange

pygame.init()
RES = 800
HW, HH = RES // 2, RES // 2
SIZE = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (150, 0, 0)
LIGHT_YELLOW = (255, 255, 204)
GREEN = (0, 200, 0)

screen = pygame.display.set_mode((RES, RES))
x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = (randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE))

snake = [(x, y)]
length = 1
score = 0
fps = 20
dx, dy = 0, 0

# score
font_score = pygame.font.SysFont("", 40)
score_text = f"Your score : {score}"
text = font_score.render(score_text, True, LIGHT_YELLOW)
text_rect = text.get_rect()
text_rect.x = 20
text_rect.y = 20

# game over
font_end = pygame.font.SysFont("", 40)
game_over_text = f"""You lose
Your score {score}
Tape c to play again or q to exit
"""
game_over = font_end.render(game_over_text, True, WHITE)
game_over_rect = game_over.get_rect()
game_over_rect.x = HW - 100
game_over_rect.y = HH

clock = pygame.time.Clock()

game = False


def close_window():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


while True:
    screen.fill(BLACK)
    close_window()

    screen.blit(text, text_rect)

    [pygame.draw.rect(screen, GREEN, (i, j, SIZE, SIZE)) for i, j in snake]
    pygame.draw.rect(screen, RED, (*apple, SIZE, SIZE))

    if snake[-1] == apple:
        apple = (randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE))
        length += 1
        fps += 1

    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        screen.blit(game_over, game_over_rect)

    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))

    snake = snake[-length:]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        dx, dy = 1, 0
    elif keys[pygame.K_LEFT]:
        dx, dy = -1, 0
    elif keys[pygame.K_UP]:
        dx, dy = 0, -1
    elif keys[pygame.K_DOWN]:
        dx, dy = 0, 1

    pygame.display.update()
    clock.tick(fps)
