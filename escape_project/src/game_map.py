import time

import pygame
import random

from games.escape_project.src.settings import Settings
from images import Images
from player import Player


class GameMap:

    def __init__(self):

        self.images = Images()
        self.player = Player("")
        self.player_name = Player("Sean")
        self.friend1_name = Player("Karen")
        self.friend2_name = Player("Karen")

        self.room_map = []

        self.room_width = 0
        self.room_height = 0

        self.tile_size = 30

        self.map_width = 5
        self.map_height = 10
        self.map_size = self.map_width * self.map_height

        self.top_left_x = 100
        self.top_left_y = 150

        self.outdoor_rooms = range(1, 26)
        self.current_room = 31

        self.landed_sector = random.randint(1, 24)
        self.landed_x = random.randint(2, 11)
        self.landed_y = random.randint(2, 11)

        self.game_rooms = self.rooms()
        self.objects = self.game_images()
        self.scenery = self.scenery()
        self.props = self.props()

        self.in_my_pockets = [55]
        self.selected_item = 0  # the first item
        self.item_carrying = self.in_my_pockets[self.selected_item]

        self.items_player_may_carry = list(range(53, 82))
        # Numbers below are for floor, pressure pad, soil, toxic floor.
        self.items_player_may_stand_on = self.items_player_may_carry + [0, 39, 2, 48]

    def get_floor_type(self):
        if self.current_room in self.outdoor_rooms:
            return 2
        else:
            return 0

    def generate_map(self, st):
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
            self.room_map.append([side_edge] + [floor_type] * (self.room_width - 2) + [side_edge])

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

        self.add_scenery()

        if self.current_room in self.scenery:
            for this_scenery in self.scenery[self.current_room]:
                scenery_number = this_scenery[0]
                scenery_y = this_scenery[1]
                scenery_x = this_scenery[2]
                self.room_map[scenery_y][scenery_x] = scenery_number
                image_here = self.objects[scenery_number][0]
                image_width = image_here.get_width()
                image_width_in_tiles = int(image_width / self.tile_size)
                for tile_number in range(1, image_width_in_tiles):
                    self.room_map[scenery_y][scenery_x + tile_number] = 255

        center_y = int(st.height / 2)  # Center of game window
        center_x = int(st.width / 2)
        room_pixel_width = self.room_width * self.tile_size  # Size of room in pixels
        room_pixel_height = self.room_height * self.tile_size
        top_left_x = center_x - 0.5 * room_pixel_width
        top_left_y = (center_y - 0.5 * room_pixel_height) + 110

        for prop_number, prop_info in self.props.items():
            prop_room = prop_info[0]
            prop_y = prop_info[1]
            prop_x = prop_info[2]
            if (prop_room == self.current_room and
                    self.room_map[prop_y][prop_x] in [0, 39, 2]):
                self.room_map[prop_y][prop_x] = prop_number
                image_here = self.objects[prop_number][0]
                image_width = image_here.get_width()
                image_width_in_tiles = int(image_width / self.tile_size)
                for tile_number in range(1, image_width_in_tiles):
                    self.room_map[prop_y][prop_x + tile_number] = 255

    def rooms(self):

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
            [self.player_name.__str__() + "'s sleeping quarters", 9, 11, False, False],  # room 36
            ["West corridor", 15, 5, True, True],  # room 37
            ["The briefing room", 7, 13, False, True],  # room 38
            ["The crew's community room", 11, 13, True, False],  # room 39
            ["Main Mission Control", 14, 14, False, False],  # room 40
            ["The sick bay", 12, 7, True, False],  # room 41
            ["West corridor", 9, 7, True, False],  # room 42
            ["Utilities control room", 9, 9, False, True],  # room 43
            ["Systems engineering bay", 9, 11, False, False],  # room 44
            ["Security portal to Mission Control", 7, 7, True, False],  # room 45
            [self.friend1_name.__str__() + "'s sleeping quarters", 9, 11, True, True],  # room 46
            [self.friend2_name.__str__() + "'s sleeping quarters", 9, 11, True, True],  # room 47
            ["The pipe works", 13, 11, True, False],  # room 48
            ["The chief scientist's office", 9, 7, True, True],  # room 49
            ["The robot workshop", 9, 11, True, False]  # room 50
        ]

        return game_rooms

    def game_images(self):
        objects = {
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
            22: [self.images.door, self.images.door_shadow, "A locked door. It needs " + self.player_name.__str__()
                 + "'s access card"],
            23: [self.images.door, self.images.door_shadow, "A locked door. It needs " + self.friend1_name.__str__()
                 + "'s access card"],
            24: [self.images.door, self.images.door_shadow, "A locked door. It needs " + self.friend2_name.__str__()
                 + "'s access card"],
            25: [self.images.door, self.images.door_shadow,
                 "A locked door. It is opened from Main Mission Control"],
            26: [self.images.door, self.images.door_shadow,
                 "A locked door in the engineering bay."],
            27: [self.images.map, self.images.full_shadow, "The screen says the crash site was Sector: "
                 + str(self.landed_sector) + " // X: " + str(self.landed_x) + " // Y: " + str(self.landed_y)],
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
                        Used for antigrav experiments.", self.player_name.__str__() + "'s yoyo"],
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
                 "This access card belongs to " + self.player_name.__str__(), "an access card"],
            80: [self.images.access_card, None,
                 "This access card belongs to " + self.friend1_name.__str__(), "an access card"],
            81: [self.images.access_card, None,
                 "This access card belongs to " + self.friend2_name.__str__(), "an access card"]
        }

        return objects

    @staticmethod
    def scenery():
        scenery = {
            26: [[39, 8, 2]],
            27: [[33, 5, 5], [33, 1, 1], [33, 1, 8], [47, 5, 2],
                 [47, 3, 10], [47, 9, 8], [42, 1, 6]],
            28: [[27, 0, 3], [41, 4, 3], [41, 4, 7]],
            29: [[7, 2, 6], [6, 2, 8], [12, 1, 13], [44, 0, 1],
                 [36, 4, 10], [10, 1, 1], [19, 4, 2], [17, 4, 4]],
            30: [[34, 1, 1], [35, 1, 3]],
            31: [[11, 1, 1], [19, 1, 8], [46, 1, 3]],
            32: [[48, 2, 2], [48, 2, 3], [48, 2, 4], [48, 3, 2], [48, 3, 3],
                 [48, 3, 4], [48, 4, 2], [48, 4, 3], [48, 4, 4]],
            33: [[13, 1, 1], [13, 1, 3], [13, 1, 8], [13, 1, 10], [48, 2, 1],
                 [48, 2, 7], [48, 3, 6], [48, 3, 3]],
            34: [[37, 2, 2], [32, 6, 7], [37, 10, 4], [28, 5, 3]],
            35: [[16, 2, 9], [16, 2, 2], [16, 3, 3], [16, 3, 8], [16, 8, 9], [16, 8, 2], [16, 1, 8],
                 [16, 1, 3], [12, 8, 6], [12, 9, 4], [12, 9, 8],
                 [15, 4, 6], [12, 7, 1], [12, 7, 11]],
            36: [[4, 3, 1], [9, 1, 7], [8, 1, 8], [8, 1, 9],
                 [5, 5, 4], [6, 5, 7], [10, 1, 1], [12, 1, 2]],
            37: [[48, 3, 1], [48, 3, 2], [48, 7, 1], [48, 5, 2], [48, 5, 3],
                 [48, 7, 2], [48, 9, 2], [48, 9, 3], [48, 11, 1], [48, 11, 2]],
            38: [[43, 0, 2], [6, 2, 2], [6, 3, 5], [6, 4, 7], [6, 2, 9], [45, 1, 10]],
            39: [[38, 1, 1], [7, 3, 4], [7, 6, 4], [5, 3, 6], [5, 6, 6],
                 [6, 3, 9], [6, 6, 9], [45, 1, 11], [12, 1, 8], [12, 1, 4]],
            40: [[41, 5, 3], [41, 5, 7], [41, 9, 3], [41, 9, 7],
                 [13, 1, 1], [13, 1, 3], [42, 1, 12]],
            41: [[4, 3, 1], [10, 3, 5], [4, 5, 1], [10, 5, 5], [4, 7, 1],
                 [10, 7, 5], [12, 1, 1], [12, 1, 5]],
            44: [[46, 4, 3], [46, 4, 5], [18, 1, 1], [19, 1, 3],
                 [19, 1, 5], [52, 4, 7], [14, 1, 8]],
            45: [[48, 2, 1], [48, 2, 2], [48, 3, 3], [48, 3, 4], [48, 1, 4], [48, 1, 1]],
            46: [[10, 1, 1], [4, 1, 2], [8, 1, 7], [9, 1, 8], [8, 1, 9], [5, 4, 3], [7, 3, 2]],
            47: [[9, 1, 1], [9, 1, 2], [10, 1, 3], [12, 1, 7], [5, 4, 4], [6, 4, 7], [4, 1, 8]],
            48: [[17, 4, 1], [17, 4, 2], [17, 4, 3], [17, 4, 4], [17, 4, 5], [17, 4, 6], [17, 4, 7],
                 [17, 8, 1], [17, 8, 2], [17, 8, 3], [17, 8, 4],
                 [17, 8, 5], [17, 8, 6], [17, 8, 7], [14, 1, 1]],
            49: [[14, 2, 2], [14, 2, 4], [7, 5, 1], [5, 5, 3], [48, 3, 3], [48, 3, 4]],
            50: [[45, 4, 8], [11, 1, 1], [13, 1, 8], [33, 2, 1], [46, 4, 6]]
        }

        return scenery

    def add_scenery(self):
        for room in range(1, 26):  # Add random scenery in planet locations.
            if room != 13:  # Skip room 13.
                scenery_item = random.choice([16, 28, 29, 30])
                self.scenery[room] = [[scenery_item, random.randint(2, 10),
                                       random.randint(2, 10)]]
        # Use loops to add fences to the planet surface rooms.
        for room_coordinate in range(0, 13):
            for room_number in [1, 2, 3, 4, 5]:  # Add top fence
                self.scenery[room_number] += [[31, 0, room_coordinate]]
            for room_number in [1, 6, 11, 16, 21]:  # Add left fence
                self.scenery[room_number] += [[31, room_coordinate, 0]]
            for room_number in [5, 10, 15, 20, 25]:  # Add right fence
                self.scenery[room_number] += [[31, room_coordinate, 12]]

        del self.scenery[21][-1]  # Delete last fence panel in Room 21
        del self.scenery[25][-1]  # Delete last fence panel in Room 25

    def player_movements(self, st):
        st = Settings()

        if st.game_over:
            return

        if self.player.player_frame > 0:
            self.player.player_frame += 1
            time.sleep(0.05)
            if self.player.player_frame == 5:
                self.player.player_frame = 0
                self.player.player_offset_x = 0
                self.player.player_offset_y = 0

        # save player's current position
        old_player_x = self.player.player_x
        old_player_y = self.player.player_y

        # move if key is pressed
        if self.player.player_frame == 0:
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                from_player_x = self.player.player_x
                from_player_y = self.player.player_y
                self.player.player_x += 1
                self.player.player_direction = "right"
                self.player.player_frame = 1
            elif pygame.key.get_pressed()[pygame.K_LEFT]:  # elif stops player making diagonal movements
                from_player_x = self.player.player_x
                from_player_y = self.player.player_y
                self.player.player_x -= 1
                self.player.player_direction = "left"
                self.player.player_frame = 1
            elif pygame.key.get_pressed()[pygame.K_UP]:
                from_player_x = self.player.player_x
                from_player_y = self.player.player_y
                self.player.player_y -= 1
                self.player.player_direction = "up"
                self.player.player_frame = 1
            elif pygame.key.get_pressed()[pygame.K_DOWN]:
                from_player_x = self.player.player_x
                from_player_y = self.player.player_y
                self.player.player_y += 1
                self.player.player_direction = "down"
                self.player.player_frame = 1
            elif pygame.key.get_pressed()[pygame.K_g]:
                self.pick_up_object()

        if self.player.player_x == self.room_width:  # through door on RIGHT
            # clock.unschedule(hazard_move)
            self.current_room += 1
            self.generate_map(st)
            self.player.player_x = 0  # enter at left
            self.player.player_y = int(self.room_height / 2)  # enter at door
            self.player.player_frame = 0
            # start_room()
            return

        if self.player.player_x == -1:  # through door on LEFT
            # clock.unschedule(hazard_move)
            self.current_room -= 1
            self.generate_map(st)
            self.player.player_x = self.room_width - 1  # enter at right
            self.player.player_y = int(self.room_height / 2)  # enter at door
            self.player.player_frame = 0
            # start_room()
            return

        if self.player.player_y == self.room_height:  # through door at BOTTOM
            # clock.unschedule(hazard_move)
            self.current_room += self.map_width
            self.generate_map(st)
            self.player.player_y = 0  # enter at top
            self.player.player_x = int(self.room_width / 2)  # enter at door
            self.player.player_frame = 0
            # start_room()
            return

        if self.player.player_y == -1:  # through door at TOP
            # clock.unschedule(hazard_move)
            self.current_room -= self.map_width
            self.generate_map(st)
            self.player.player_y = self.room_height - 1  # enter at bottom
            self.player.player_x = int(self.room_width / 2)  # enter at door
            self.player.player_frame = 0
            # start_room()
            return

        # If the player is standing somewhere they shouldn't, move them back.
        if self.room_map[self.player.player_y][self.player.player_x] not in self.items_player_may_stand_on:  # \
            # or hazard_map[player_y][player_x] != 0:
            self.player.player_x = old_player_x
            self.player.player_y = old_player_y
            self.player.player_frame = 0

        if self.player.player_direction == "right" and self.player.player_frame > 0:
            self.player.player_offset_x = -1 + (0.25 * self.player.player_frame)
        if self.player.player_direction == "left" and self.player.player_frame > 0:
            self.player.player_offset_x = 1 - (0.25 * self.player.player_frame)
        if self.player.player_direction == "up" and self.player.player_frame > 0:
            self.player.player_offset_y = 1 - (0.25 * self.player.player_frame)
        if self.player.player_direction == "down" and self.player.player_frame > 0:
            self.player.player_offset_y = -1 + (0.25 * self.player.player_frame)

    # def start_room(self):
    #     self.show_text("You are here: " + room_name, 0)

    def draw_image(self, image, y, x, screen):
        screen.blit(image,
                    (self.top_left_x + (x * self.tile_size),
                     self.top_left_y + (y * self.tile_size) - image.get_height())
                    )

    def draw_shadow(self, image, y, x, screen):
        screen.blit(image,
                    (self.top_left_x + (x * self.tile_size),
                     self.top_left_y + (y * self.tile_size))
                    )

    def draw_player(self, screen):
        player_image = self.player.player_movements[self.player.player_direction][self.player.player_frame]

        self.draw_image(player_image, self.player.player_y + self.player.player_offset_y,
                        self.player.player_x + self.player.player_offset_x, screen)
        player_image_shadow = self.player.player_shadow[self.player.player_direction][self.player.player_frame]
        self.draw_shadow(player_image_shadow, self.player.player_y + self.player.player_offset_y,
                         self.player.player_x + self.player.player_offset_x, screen)

    def draw(self, screen, st):
        if st.game_over:
            return

        # Clear the game arena area.
        # box = pygame.Rect((0, 150), (800, 600))
        # pygame.draw.circle(box, st.red)
        # box = pygame.Rect((0, 0), (800, self.top_left_y + (self.room_height - 1) * 30))
        # screen.surface.set_clip(box)
        floor_type = self.get_floor_type()

        for y in range(self.room_height):  # Lay down floor tiles, then items on floor.
            for x in range(self.room_width):
                self.draw_image(self.objects[floor_type][0], y, x, screen)
                # Next line enables shadows to fall on top of objects on floor
                if self.room_map[y][x] in self.items_player_may_stand_on:
                    self.draw_image(self.objects[self.room_map[y][x]][0], y, x, screen)

        # Pressure pad in room 26 is added here, so props can go on top of it.
        if self.current_room == 26:
            self.draw_image(self.objects[39][0], 8, 2, screen)
            image_on_pad = self.room_map[8][2]
            if image_on_pad > 0:
                self.draw_image(self.objects[image_on_pad][0], 8, 2, screen)

        for y in range(self.room_height):
            for x in range(self.room_width):
                item_here = self.room_map[y][x]
                # Player cannot walk on 255: it marks spaces used by wide objects.
                if item_here not in self.items_player_may_stand_on + [255]:
                    image = self.objects[item_here][0]

                    if (self.current_room in self.outdoor_rooms
                        and y == self.room_height - 1
                        and self.room_map[y][x] == 1) or \
                            (self.current_room not in self.outdoor_rooms
                             and y == self.room_height - 1
                             and self.room_map[y][x] == 1
                             and 0 < x < self.room_width - 1):
                        # Add transparent wall image in the front row.
                        image = self.player.pillars[self.player.wall_transparency_frame]

                    self.draw_image(image, y, x, screen)

                    if self.objects[item_here][1] is not None:  # If object has a shadow
                        shadow_image = self.objects[item_here][1]
                        # if shadow might need horizontal tiling
                        if shadow_image in [self.images.half_shadow,
                                            self.images.full_shadow]:
                            shadow_width = int(image.get_width() / self.tile_size)
                            # Use shadow across width of object.
                            for z in range(0, shadow_width):
                                self.draw_shadow(shadow_image, y, x + z, screen)
                        else:
                            self.draw_shadow(shadow_image, y, x, screen)

            if self.player.player_y == y:
                self.draw_player(screen)

    def adjust_wall_transparency(self):
        if (self.player.player_y == self.room_height - 2
                and self.room_map[self.room_height - 1][self.player.player_x] == 1
                and self.player.wall_transparency_frame < 4):
            self.player.wall_transparency_frame += 1  # Fade wall out.
        if ((self.player.player_y < self.room_height - 2
             or self.room_map[self.room_height - 1][self.player.player_x] != 1)
                and self.player.wall_transparency_frame > 0):
            self.player.wall_transparency_frame -= 1  # Fade wall in.

    # def show_text(self, text_to_show, line_number, screen, st):
    #     if st.game_over:
    #         return
    #
    #     text_lines = [15, 50]
    #     box = pygame.Rect((0, text_lines[line_number]), (800, 35))
    #     screen.draw.filled_rect(box, st.black)
    #     screen.draw.text(text_to_show,
    #                      (20, text_lines[line_number]), color=st.green)

    def props(self):
        props = {
            20: [31, 0, 4], 21: [26, 0, 1], 22: [41, 0, 2], 23: [39, 0, 5],
            24: [45, 0, 2],
            25: [32, 0, 2], 26: [27, 12, 5],  # two sides of same door
            40: [0, 8, 6], 53: [45, 1, 5], 54: [0, 0, 0], 55: [0, 0, 0],
            56: [0, 0, 0], 57: [35, 4, 6], 58: [0, 0, 0], 59: [31, 1, 7],
            60: [0, 0, 0], 61: [36, 1, 1], 62: [36, 1, 6], 63: [0, 0, 0],
            64: [27, 8, 3], 65: [50, 1, 7], 66: [39, 5, 6], 67: [46, 1, 1],
            68: [0, 0, 0], 69: [30, 3, 3], 70: [47, 1, 3],
            71: [0, self.landed_y, self.landed_x], 72: [0, 0, 0], 73: [27, 4, 6],
            74: [28, 1, 11], 75: [0, 0, 0], 76: [41, 3, 5], 77: [0, 0, 0],
            78: [35, 9, 11], 79: [26, 3, 2], 80: [41, 7, 5], 81: [29, 1, 1]
        }

        return props

    def find_object_start_x(self):
        checker_x = self.player.player_x

        while self.room_map[self.player.player_y][checker_x] == 255:
            checker_x -= 1
        return checker_x

    def get_item_under_player(self):
        item_x = self.find_object_start_x()

        item_player_is_on = self.room_map[self.player.player_y][item_x]
        return item_player_is_on

    def pick_up_object(self):

        item_player_is_on = self.get_item_under_player()
        if item_player_is_on in self.items_player_may_carry:
            self.room_map[self.player.player_y][self.player.player_x] = self.get_floor_type()
        self.add_object(item_player_is_on)
        time.sleep(0.5)

    def add_object(self, item):  # Adds item to inventory.
        self.in_my_pockets.append(item)
        item_carrying = item
        selected_item = len(self.in_my_pockets) - 1
        self.display_inventory()
        self.props[item][0] = 0  # Carried objects go into room 0 (off the map).

    def display_inventory(self):
        print(self.in_my_pockets)
