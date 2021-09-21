import pygame

from player import Player


class GameMap:

    def __init__(self):
        self.room_map = []

        self.room_width = 0
        self.room_height = 0

        self.map_width = 5
        self.map_height = 10
        self.map_size = self.map_width * self.map_height

        self.top_left_x = 100
        self.top_left_y = 150

        self.outdoor_rooms = range(1, 26)
        self.current_room = 31

    def get_floor_type(self):
        if self.current_room in self.outdoor_rooms:
            return 2
        else:
            return 0

    def generate_map(self):
        side_edge = 0
        bottom_edge = 0

        game_map = self.rooms()
        room_data = game_map[self.current_room]
        room_name = room_data[0]
        self.room_height = room_data[1]
        self.room_width = room_data[2]

        floor_type = self.get_floor_type()
        if self.current_room in range(1, 21):
            bottom_edge = 2
            side_edge = 2
        if self.current_room in range(21, 26):
            bottom_edge = 1
            side_edge = 2
        if self.current_room > 25:
            bottom_edge = 1
            side_edge = 1

        self.room_map = [[side_edge] * self.room_width]
        for y in range(self.room_height - 2):
            self.room_map.append([side_edge] + [floor_type]*(self.room_width - 2) + [side_edge])

        self.room_map.append([bottom_edge] * self.room_width)

        middle_row = self.room_height // 2
        middle_column = self.room_width // 2

        if room_data[4]:
            self.room_map[middle_row][self.room_width - 1] = floor_type
            self.room_map[middle_row + 1][self.room_width - 1] = floor_type
            self.room_map[middle_row - 1][self.room_width - 1] = floor_type

        if self.current_room % self.map_width != 1:  # If room is not on left of map
            room_to_left = game_map[self.current_room - 1]
            # If room on the left has a right exit, add left exit in this room
            if room_to_left[4]:
                self.room_map[middle_row][0] = floor_type
                self.room_map[middle_row + 1][0] = floor_type
                self.room_map[middle_row - 1][0] = floor_type
        if room_data[3]:  # If exit at top of this room
            self.room_map[0][middle_column] = floor_type
            self.room_map[0][middle_column + 1] = floor_type
            self.room_map[0][middle_column - 1] = floor_type
        if self.current_room <= self.map_size - self.map_width:  # If room is not on bottom row
            room_below = game_map[self.current_room + self.map_width]
            # If room below has a top exit, add exit at bottom of this one
            if room_below[3]:
                self.room_map[self.room_height - 1][middle_column] = floor_type
                self.room_map[self.room_height - 1][middle_column + 1] = floor_type
                self.room_map[self.room_height - 1][middle_column - 1] = floor_type

    @staticmethod
    def rooms():
        player_name = Player("Sean")
        friend1_name = Player("Karen")
        friend2_name = Player("Karen")

        game_rooms = [["Room 0 - where unused objects are kept", 0, 0, False, False]]

        for planet_sectors in range(1, 26):
            game_rooms.append(["The dusty planet surface", 13, 13, True, True])

        game_rooms += [
            # ["Room name", height, width, Top exit?, Right exit?]
            ["The airlock", 13, 5, True, False],  # room 26
            ["The engineering lab", 13, 13, False, False],  # room 27
            ["Poodle Mission Control", 9, 13, False, True],  # room 28
            ["The viewing gallery", 9, 15, False, False],  # room 29
            ["The crew's bathroom", 5, 5, False, False],  # room 30
            ["The airlock entry bay", 7, 11, True, True],  # room 31
            ["Left elbow room", 9, 7, True, False],  # room 32
            ["Right elbow room", 7, 13, True, True],  # room 33
            ["The science lab", 13, 13, False, True],  # room 34
            ["The greenhouse", 13, 13, True, False],  # room 35
            [player_name.__str__() + "'s sleeping quarters", 9, 11, False, False],  # room 36
            ["West corridor", 15, 5, True, True],  # room 37
            ["The briefing room", 7, 13, False, True],  # room 38
            ["The crew's community room", 11, 13, True, False],  # room 39
            ["Main Mission Control", 14, 14, False, False],  # room 40
            ["The sick bay", 12, 7, True, False],  # room 41
            ["West corridor", 9, 7, True, False],  # room 42
            ["Utilities control room", 9, 9, False, True],  # room 43
            ["Systems engineering bay", 9, 11, False, False],  # room 44
            ["Security portal to Mission Control", 7, 7, True, False],  # room 45
            [friend1_name.__str__() + "'s sleeping quarters", 9, 11, True, True],  # room 46
            [friend2_name.__str__() + "'s sleeping quarters", 9, 11, True, True],  # room 47
            ["The pipe works", 13, 11, True, False],  # room 48
            ["The chief scientist's office", 9, 7, True, True],  # room 49
            ["The robot workshop", 9, 11, True, False]  # room 50
        ]
        return game_rooms

    def draw(self, screen):

        self.generate_map()

        floor = pygame.image.load("../images/floor.png")
        pillar = pygame.image.load("../images/pillar.png")
        soil = pygame.image.load("../images/soil.png")
        images = [floor, pillar, soil]

        for y in range(self.room_height):
            for x in range(self.room_width):
                image_to_draw = images[self.room_map[y][x]]
                screen.blit(image_to_draw, (self.top_left_x + (x * 30),
                                            self.top_left_y + (y * 30) - image_to_draw.get_height()))
