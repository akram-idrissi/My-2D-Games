import pygame
from pygame.loacls import *

def events(): 
	for event in pygame.event.get():
		if event.type == pygame.QUIT and event.key == K_ESCAPE