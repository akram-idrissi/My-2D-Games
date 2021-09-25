"""
* The mother map has 50 sub-maps
* Each sub-map represents a room
* The first 25 sub-maps are planet surface (space)
* Every room has an exit
* The player will be in room 31 every time he plays the game
"""

import maps_list as ml
import objects as obj
import random

from images import Images
from player import Player


class Maps:
    def __init__(self):
        """ initializing variables """
        self.images = Images()

        self.top_left_x = 100
        self.top_left_y = 150

        self.map_width = 5
        self.map_height = 10
        self.map_size = self.map_width * self.map_height

        # It'll contain the room shape
        self.room_map = []

        # Players
        self.PLAYER_NAME = Player("Sean")
        self.FRIEND1_NAME = Player("Karen")
        self.FRIEND2_NAME = Player("Leo")

        self.outdoor_rooms = range(1, 26)

        # Where the player is
        self.current_room = 31

        # Room properties
        self.room_name = ""
        self.room_width = 0
        self.room_height = 0
        self.room_top_exit = None
        self.room_right_exit = None
        self.floor_type = self.get_floor_type()

        self.LANDER_SECTOR = random.randint(1, 24)
        self.LANDER_X = random.randint(2, 11)
        self.LANDER_Y = random.randint(2, 11)

        # All the game maps
        self.maps = ml.game_map(self.PLAYER_NAME, self.FRIEND1_NAME, self.FRIEND2_NAME)

        # All the game images (objects)
        self.objects = obj.objects(self.PLAYER_NAME, self.FRIEND1_NAME, self.FRIEND2_NAME,
                                   self.LANDER_SECTOR, self.LANDER_X, self.LANDER_Y)

    def get_floor_type(self):
        if self.current_room in self.outdoor_rooms:
            return 2
        else:
            return 0

    def generate_map(self):
        """ This method creates the map for the current room
        using room_data, scenery data and prop data
        """
        room_data = self.maps[self.current_room]
        self.room_name = room_data[0]
        self.room_height = room_data[1]
        self.room_width = room_data[2]
        self.room_top_exit = room_data[3]
        self.room_right_exit = room_data[4]

        if self.current_room in range(1, 21):
            bottom_edge = 2
            side_edge = 2
        elif self.current_room in range(21, 26):
            bottom_edge = 1
            side_edge = 2
        else:
            bottom_edge = 1
            side_edge = 1

        # Create top line of self.room_map
        self.room_map = [[side_edge] * self.room_width]

        # Add middle lines of self.room_map (wall, floor to fill width, wall)
        for y in range(self.room_height - 2):
            self.room_map.append([side_edge] + [self.floor_type] * (self.room_width - 2) + [side_edge])

        # Add bottom line of room map
        self.room_map.append([bottom_edge] * self.room_width)

        # Add door ways
        middle_row = self.room_height // 2
        middle_column = self.room_width // 2

        if room_data[4]:  # if exit at the right of this room
            self.room_map[middle_row][self.room_width - 1] = self.floor_type
            self.room_map[middle_row + 1][self.room_width - 1] = self.floor_type
            self.room_map[middle_row - 1][self.room_width - 1] = self.floor_type

        if self.current_room % self.map_width != 1:  # if room is not on left of map
            room_to_left = self.maps[self.current_room - 1]
            # If room on the left has a right exit, add left exit in this room
            if room_to_left[4]:
                self.room_map[middle_row][0] = self.floor_type
                self.room_map[middle_row + 1][0] = self.floor_type
                self.room_map[middle_row - 1][0] = self.floor_type

        if room_data[3]:  # If exit at top of this room
            self.room_map[0][middle_column] = self.floor_type
            self.room_map[0][middle_column + 1] = self.floor_type
            self.room_map[0][middle_column - 1] = self.floor_type

        if self.current_room <= self.map_size - self.map_width:  # If room is not on bottom row
            room_below = self.maps[self.current_room + self.map_width]
            # If room below has a top exit, add exit at bottom of this one
            if room_below[3]:
                self.room_map[self.room_height - 1][middle_column] = self.floor_type
                self.room_map[self.room_height - 1][middle_column + 1] = self.floor_type
                self.room_map[self.room_height - 1][middle_column - 1] = self.floor_type

    def draw(self, screen):
        self.generate_map()
        demo = [self.images.floor, self.images.pillar, self.images.soil]
        for y in range(self.room_height):
            for x in range(self.room_width):
                image_to_draw = demo[self.room_map[y][x]]
                screen.blit(image_to_draw,
                            (self.top_left_x + (x * 30),
                             self.top_left_y + (y * 30) - image_to_draw.get_height()))
