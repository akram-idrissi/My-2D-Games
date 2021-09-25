import pygame, os

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

MAP = [
	[1, 1, 1, 1, 1, 1, 1],
	[1, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 1],
	[1, 1, 1, 1, 1, 1, 1],
]

x_pos, y_pos = 100, 100
path = r"C:\Users\Ce pc\Desktop\programming\python\PYGAME\escape_project"
red_square = pygame.image.load(os.path.join(path, "redsquare.png")).convert()
blue_square = pygame.image.load(os.path.join(path, "bluesquare.png")).convert()

while True:

	for y in range(5):
		for x in range(7):
			if MAP[y][x] == 1:
				screen.blit(red_square, (x_pos + 30, y_pos))
			else :
				screen.blit(blue_square, (x_pos, y_pos + 30))

	pygame.display.update()


