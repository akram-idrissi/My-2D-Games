"""
* The map has 50 sub-maps
* Each sub-map represents a room
* The first 25 sub-maps are planet surface (space)
* Every room has an exit
* The player will be in room 31 every time he plays the game
"""
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
        self.maps = self.game_map()

        # All the game images (objects)
        self.objects = self.game_objects()

    def game_map(self):
        """ Maps and their properties """
        maps_list = [["Room 0 - where unused objects are kept", 0, 0, False, False]]

        for map_list in range(1, 26):
            maps_list.append(["The dusty planet surface", 13, 13, True, True])

        maps_list += [
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
            [self.PLAYER_NAME.name + "'s sleeping quarters", 9, 11, False, False],  # room 36
            ["West corridor", 15, 5, True, True],  # room 37
            ["The briefing room", 7, 13, False, True],  # room 38
            ["The crew's community room", 11, 13, True, False],  # room 39
            ["Main Mission Control", 14, 14, False, False],  # room 40
            ["The sick bay", 12, 7, True, False],  # room 41
            ["West corridor", 9, 7, True, False],  # room 42
            ["Utilities control room", 9, 9, False, True],  # room 43
            ["Systems engineering bay", 9, 11, False, False],  # room 44
            ["Security portal to Mission Control", 7, 7, True, False],  # room 45
            [self.FRIEND1_NAME.name + "'s sleeping quarters", 9, 11, True, True],  # room 46
            [self.FRIEND2_NAME.name + "'s sleeping quarters", 9, 11, True, True],  # room 47
            ["The pipeworks", 13, 11, True, False],  # room 48
            ["The chief scientist's office", 9, 7, True, True],  # room 49
            ["The robot workshop", 9, 11, True, False]  # room 50
        ]
        return maps_list

    def game_objects(self):
        return {
            0: [self.images.floor, None, "The floor is shiny and clean"],
            1: [self.images.pillar, self.images.full_shadow, "The wall is smooth and cold"],
            2: [self.images.soil, None, "It's like a desert. Or should that be dessert?"],
            3: [self.images.pillar_low, self.images.half_shadow, "The wall is smooth and cold"],
            4: [self.images.bed, self.images.half_shadow, "A tidy and comfortable bed"],
            5: [self.images.table, self.images.half_shadow, "It's made from strong plastic."],
            6: [self.images.chair_left, None, "A chair with a soft cushion"],
            7: [self.images.chair_right, None, "A chair with a soft cushion"],
            8: [self.images.bookcase_tall, self.images.full_shadow,
                "Bookshelves, stacked with reference books"],
            9: [self.images.bookcase_small, self.images.half_shadow,
                "Bookshelves, stacked with reference books"],
            10: [self.images.cabinet, self.images.half_shadow,
                 "A small locker, for storing personal items"],
            11: [self.images.desk_computer, self.images.half_shadow,
                 "A computer. Use it to run life support diagnostics"],
            12: [self.images.plant, self.images.plant_shadow, "A spaceberry plant, grown here"],
            13: [self.images.electrical1, self.images.half_shadow,
                 "Electrical systems used for powering the space station"],
            14: [self.images.electrical2, self.images.half_shadow,
                 "Electrical systems used for powering the space station"],
            15: [self.images.cactus, self.images.cactus_shadow, "Ouch! Careful on the cactus!"],
            16: [self.images.shrub, self.images.shrub_shadow,
                 "A space lettuce. A bit limp, but amazing it's growing here!"],
            17: [self.images.pipes1, self.images.pipes1_shadow, "Water purification pipes"],
            18: [self.images.pipes2, self.images.pipes2_shadow,
                 "Pipes for the life support systems"],
            19: [self.images.pipes3, self.images.pipes3_shadow,
                 "Pipes for the life support systems"],
            20: [self.images.door, self.images.door_shadow, "Safety door. Opens automatically \
        for astronauts in functioning spacesuits."],
            21: [self.images.door, self.images.door_shadow, "The airlock door. \
        For safety reasons, it requires two person operation."],
            22: [self.images.door, self.images.door_shadow, "A locked door. It needs " \
                 + self.PLAYER_NAME.name + "'s access card"],
            23: [self.images.door, self.images.door_shadow, "A locked door. It needs " \
                 + self.FRIEND1_NAME.name + "'s access card"],
            24: [self.images.door, self.images.door_shadow, "A locked door. It needs " \
                 + self.FRIEND2_NAME.name + "'s access card"],
            25: [self.images.door, self.images.door_shadow,
                 "A locked door. It is opened from Main Mission Control"],
            26: [self.images.door, self.images.door_shadow,
                 "A locked door in the engineering bay."],
            27: [self.images.map, self.images.full_shadow,
                 "The screen says the crash site was Sector: " \
                 + str(self.LANDER_SECTOR) + " // X: " + str(self.LANDER_X) + \
                 " // Y: " + str(self.LANDER_Y)],
            28: [self.images.rock_large, self.images.rock_large_shadow,
                 "A rock. Its coarse surface feels like a whetstone", "the rock"],
            29: [self.images.rock_small, self.images.rock_small_shadow,
                 "A small but heavy piece of Martian rock"],
            30: [self.images.crater, None, "A crater in the planet surface"],
            31: [self.images.fence, None,
                 "A fine gauze fence. It helps protect the station from dust storms"],
            32: [self.images.contraption, self.images.contraption_shadow,
                 "One of the scientific experiments. It gently vibrates"],
            33: [self.images.robot_arm, self.images.robot_arm_shadow,
                 "A robot arm, used for heavy lifting"],
            34: [self.images.toilet, self.images.half_shadow, "A sparkling clean toilet"],
            35: [self.images.sink, None, "A sink with running water", "the taps"],
            36: [self.images.globe, self.images.globe_shadow,
                 "A giant globe of the planet. It gently glows from inside"],
            37: [self.images.science_lab_table, None,
                 "A table of experiments, analyzing the planet soil and dust"],
            38: [self.images.vending_machine, self.images.full_shadow,
                 "A vending machine. It requires a credit.", "the vending machine"],
            39: [self.images.floor_pad, None,
                 "A pressure sensor to make sure nobody goes out alone."],
            40: [self.images.rescue_ship, self.images.rescue_ship_shadow, "A rescue ship!"],
            41: [self.images.mission_control_desk, self.images.mission_control_desk_shadow,
                 "Mission Control stations."],
            42: [self.images.button, self.images.button_shadow,
                 "The button for opening the time-locked door in engineering."],
            43: [self.images.whiteboard, self.images.full_shadow,
                 "The whiteboard is used in brainstorms and planning meetings."],
            44: [self.images.window, self.images.full_shadow,
                 "The window provides a view out onto the planet surface."],
            45: [self.images.robot, self.images.robot_shadow, "A cleaning robot, turned off."],
            46: [self.images.robot2, self.images.robot2_shadow,
                 "A planet surface exploration robot, awaiting set-up."],
            47: [self.images.rocket, self.images.rocket_shadow, "A one-person craft in repair"],
            48: [self.images.toxic_floor, None, "Toxic floor - do not walk on!"],
            49: [self.images.drone, None, "A delivery drone"],
            50: [self.images.energy_ball, None, "An energy ball - dangerous!"],
            51: [self.images.energy_ball2, None, "An energy ball - dangerous!"],
            52: [self.images.computer, self.images.computer_shadow,
                 "A computer workstation, for managing space station systems."],
            53: [self.images.clipboard, None,
                 "A clipboard. Someone has doodled on it.", "the clipboard"],
            54: [self.images.bubble_gum, None,
                 "A piece of sticky bubble gum. Spaceberry flavour.", "bubble gum"],
            55: [self.images.yoyo, None, "A toy made of fine, strong string and plastic. \
        Used for antigrav experiments.", self.PLAYER_NAME.name + "'s yoyo"],
            56: [self.images.thread, None,
                 "A piece of fine, strong string", "a piece of string"],
            57: [self.images.needle, None,
                 "A sharp needle from a cactus plant", "a cactus needle"],
            58: [self.images.threaded_needle, None,
                 "A cactus needle, spearing a length of string", "needle and string"],
            59: [self.images.canister, None,
                 "The air canister has a leak.", "a leaky air canister"],
            60: [self.images.canister, None,
                 "It looks like the seal will hold!", "a sealed air canister"],
            61: [self.images.mirror, None,
                 "The mirror throws a circle of light on the walls.", "a mirror"],
            62: [self.images.bin_empty, None,
                 "A rarely used bin, made of light plastic", "a bin"],
            63: [self.images.bin_full, None,
                 "A heavy bin full of water", "a bin full of water"],
            64: [self.images.rags, None,
                 "An oily rag. Pick it up by one corner if you must!", "an oily rag"],
            65: [self.images.hammer, None,
                 "A hammer. Maybe good for cracking things open...", "a hammer"],
            66: [self.images.spoon, None, "A large serving spoon", "a spoon"],
            67: [self.images.food_pouch, None,
                 "A dehydrated food pouch. It needs water.", "a dry food pack"],
            68: [self.images.food, None,
                 "A food pouch. Use it to get 100% energy.", "ready-to-eat food"],
            69: [self.images.book, None, "The book has the words 'Don't Panic' on the \
        cover in large, friendly letters", "a book"],
            70: [self.images.mp3_player, None,
                 "An MP3 player, with all the latest tunes", "an MP3 player"],
            71: [self.images.lander, None, "The Poodle, a small space exploration craft. \
        Its black box has a radio sealed inside.", "the Poodle lander"],
            72: [self.images.radio, None, "A radio communications system, from the \
        Poodle", "a communications radio"],
            73: [self.images.gps_module, None, "A GPS Module", "a GPS module"],
            74: [self.images.positioning_system, None, "Part of a positioning system. \
        Needs a GPS module.", "a positioning interface"],
            75: [self.images.positioning_system, None,
                 "A working positioning system", "a positioning computer"],
            76: [self.images.scissors, None, "Scissors. They're too blunt to cut \
        anything. Can you sharpen them?", "blunt scissors"],
            77: [self.images.scissors, None,
                 "Razor-sharp scissors. Careful!", "sharpened scissors"],
            78: [self.images.credit, None,
                 "A small coin for the station's vending systems",
                 "a station credit"],
            79: [self.images.access_card, None,
                 "This access card belongs to " + self.PLAYER_NAME.name, "an access card"],
            80: [self.images.access_card, None,
                 "This access card belongs to " + self.FRIEND1_NAME.name, "an access card"],
            81: [self.images.access_card, None,
                 "This access card belongs to " + self.FRIEND2_NAME.name, "an access card"]
        }

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
        self.room_width  = room_data[2]
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
