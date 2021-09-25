from pprint import pprint

room_map = [ [1, 0, 0, 0, 0],
			[0, 0, 0, 2, 0],
			[0, 0, 0, 0, 0],
			[0, 3, 0, 0, 0],
			[0, 0, 0, 0, 4]
]

room_map[0][0] = 5
room_map[0-1][-1] = 6
pprint(room_map)


