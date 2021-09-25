WIDTH, HEIGHT = 800, 600

room_map = [ [1, 1, 1, 1, 1, 1, 1, 1, 1],#1
			[1, 1, 0, 0, 0, 0, 0, 1, 1], #2
			[1, 0, 0, 0, 0, 0, 0, 0, 1], #3
			[1, 0, 0, 0, 0, 0, 0, 0, 0], #4 
			[1, 0, 0, 1, 1, 0, 0, 0, 0], #5
			[1, 0, 0, 0, 1, 0, 0, 0, 0], #6
			[1, 0, 0, 0, 0, 0, 0, 0, 1], #7
			[1, 0, 0, 0, 0, 0, 0, 0, 1], #8
			[1, 1, 1, 0, 0, 0, 1, 1, 1]  #9
]

rows = 9
columns = 9

top_left_x, top_left_y = 300, 150

DEMO_OBJECTS = [images.floor, images.pillar]

def draw():
	for y in range(rows):
		for x in range(columns):
			image_to_draw = DEMO_OBJECTS[room_map[y][x]]
			screen.blit(image_to_draw, (top_left_x + (x * 30), top_left_y + (y * 30)
			 -  image_to_draw.get_height()))




