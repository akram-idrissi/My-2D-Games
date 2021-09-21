import sys
import math
import pygame
from PIL import Image
from random import choice

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


image = Image.open("../images/427.png")
rgb = image.convert('RGB')

coordinates = []
for x in range(image.size[0]):
    for y in range(image.size[1]):
        r, g, b = image.getpixel((x, y))
        if r == 0 and g == 0 and b == 0:
            coordinates.append((x, y))

while True:

    screen.fill(st.WHITE)
    events()

    # finding a space
    while True:
        spot = choice(coordinates)

        x = spot[0]
        y = spot[1]
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
        pygame.draw.circle(screen, st.BLACK, (circle.x, circle.y), circle.r, 1)

    pygame.display.update()
    clock.tick(st.FPS)
