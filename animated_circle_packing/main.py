import sys
import math
import pygame
from random import randint

from circle import Circle
from settings import Settings

pygame.init()
st = Settings()
screen = pygame.display.set_mode((st.WIDTH, st.HEIGHT))
pygame.display.set_caption("Animated Circle Packing")

clock = pygame.time.Clock()

circles = []


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


while True:

    screen.fill(st.BLACK)
    events()

    # finding a space
    while True:
        x = randint(0, st.WIDTH)
        y = randint(0, st.HEIGHT)
        found_space = True
        for circle in circles:
            distance = math.hypot(circle.x - x, circle.y - y)
            if distance <= circle.r:
                found_space = False
                break

        if found_space:
            break

        st.attempts += 1
        if st.attempts >= st.max_attempts:
            st.exit = True
            break

    if st.exit:
        break

    circles.append(Circle(x, y, len(circles)))

    # checking for collisions

    for circle in circles:
        if not circle.valid:
            continue
        for n_circle in circles:
            if circle.id == n_circle.id:
                continue
            distance_between_circles = math.hypot(circle.x - n_circle.x, circle.y - n_circle.y)
            sum_radius = circle.r + n_circle.r
            if distance_between_circles - sum_radius <= st.gap:
                circle.valid = False
                n_circle.valid = False
                break

        if circle.valid:
            circle.r += 1

    # screen.blit(background, background.get_rect())
    for circle in circles:
        pygame.draw.circle(screen, st.WHITE, (circle.x, circle.y), circle.r, 1)

    pygame.display.update()
    clock.tick(st.FPS)
