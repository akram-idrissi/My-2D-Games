import pygame
import pygame.font
import sys

from random import randrange

pygame.init()
WIDTH, HEIGHT = 1200, 600
RES = WIDTH, HEIGHT
HW, HH = WIDTH // 2, HEIGHT // 2
SIZE = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (150, 0, 0)
LIGHT_YELLOW = (255, 255, 204)
GREEN = (0, 200, 0)

screen = pygame.display.set_mode(RES)
x, y = randrange(SIZE, WIDTH - SIZE, SIZE), randrange(SIZE, HEIGHT - SIZE, SIZE)
apple = (randrange(SIZE, WIDTH - SIZE, SIZE), randrange(SIZE, HEIGHT - SIZE, SIZE))

snake = [(x, y)]
length = 1
score = 0
fps = 10
dx, dy = 0, 0

# score
font_score = pygame.font.SysFont("", 40)
font_end = pygame.font.SysFont("", 40)
font_fps = pygame.font.SysFont("", 1)

clock = pygame.time.Clock()


def close_window():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def restart():
    global x, y, length, apple, score, fps
    x, y = randrange(SIZE, WIDTH - SIZE, SIZE), randrange(SIZE, HEIGHT - SIZE, SIZE)
    apple = (randrange(SIZE, WIDTH - SIZE, SIZE), randrange(SIZE, HEIGHT - SIZE, SIZE))
    score = 0
    length = 1
    fps = 10


while True:
    screen.fill(BLACK)
    close_window()

    text_fps = font_score.render(f"fps : {fps}", True, LIGHT_YELLOW)
    screen.blit(text_fps, (0, 0))
    text = font_score.render(f"Your score : {score}", True, LIGHT_YELLOW)
    screen.blit(text, (0, 40))

    [pygame.draw.rect(screen, GREEN, (i, j, SIZE - 2, SIZE - 2)) for i, j in snake]
    pygame.draw.rect(screen, RED, (*apple, SIZE, SIZE))

    if snake[-1] == apple:
        apple = (randrange(SIZE, WIDTH - SIZE, SIZE), randrange(SIZE, HEIGHT - SIZE, SIZE))
        length += 1
        score += 1
        fps += 1

    if len(snake) != len(set(snake)):
        while True:
            game_over = font_end.render("Game Over, click r to play again  or escape to quit", True,
                                        pygame.Color("orange"))
            screen.blit(game_over, (250, HH))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                restart()
                break
            close_window()
            pygame.display.update()

    if x < 0:
        x = WIDTH
    if x > WIDTH:
        x = 0

    if y < 0:
        y = HEIGHT
    if y > HEIGHT:
        y = 0

    # snake.append((x, y))

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
