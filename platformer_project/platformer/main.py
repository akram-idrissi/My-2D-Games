import pygame 

from settings import Settings

def run():

	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
	pygame.display.set_caption("Platformer")

	display = pygame.Surface((settings.H_WIDTH, settings.H_HEGHT))

	while True :

		display.fill(settings.WHITE)

		screen.blit(pygame.transform.scale(display, (settings.WIDTH, settings.HEIGHT)), (0, 0))
		pygame.display.update()

run()

