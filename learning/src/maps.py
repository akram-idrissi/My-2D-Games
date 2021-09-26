"""
* The space station has 50 maps
* The first 25 maps represent the planet surface (Mars)
* The other 25 maps are rooms
* Every room has an exit
* The player will be in room 31 every time the game is run
"""
import pygame
import random
import time

import maps_list as ml
import objects as obj
import scenery as sc

from images import Images
from player import Player


class Maps:
    def __init__(self):
        """ initializing variables """
        self.WIDTH = 800
        self.HEIGHT = 800

        self.font = pygame.font.SysFont("Sans MS", 30)

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

        # Colors
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 155, 255)
        self.YELLOW = (255, 255, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (128, 0, 0)

        self.outdoor_rooms = range(1, 26)
        self.TILE_SIZE = 30
        self.game_over = False

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

        # All the game sceneries
        self.scenery = sc.scenery()

        self.items_player_may_carry = list(range(53, 82))
        # Numbers below are for floor, pressure pad, soil, toxic floor.
        self.items_player_may_stand_on = self.items_player_may_carry + [0, 39, 2, 48]

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

        self.add_scenery()
        self.load_scenery()

    def add_scenery(self):
        """This method adds the perimeter fence for the planet surface """
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

    def load_scenery(self):
        """This method draws the scenery data
        in the space station
        """
        if self.current_room in self.scenery:
            for this_scenery in self.scenery[self.current_room]:
                scenery_number = this_scenery[0]
                scenery_y = this_scenery[1]
                scenery_x = this_scenery[2]
                self.room_map[scenery_y][scenery_x] = scenery_number

                image_here = self.objects[scenery_number][0]
                image_width = image_here.get_width()
                image_width_in_tiles = int(image_width / self.TILE_SIZE)
                for tile_number in range(1, image_width_in_tiles):
                    self.room_map[scenery_y][scenery_x + tile_number] = 255

        center_y = int(self.HEIGHT / 2)  # Center of game window
        center_x = int(self.WIDTH / 2)
        room_pixel_width = self.room_width * self.TILE_SIZE  # Size of room in pixels
        room_pixel_height = self.room_height * self.TILE_SIZE
        self.top_left_x = center_x - 0.5 * room_pixel_width
        self.top_left_y = (center_y - 0.5 * room_pixel_height) + 110

    def player_movement(self, screen):
        """This method handles the player movement"""
        if self.game_over:
            return
        if self.PLAYER_NAME.player_frame > 0:
            self.PLAYER_NAME.player_frame += 1
            time.sleep(0.05)
            if self.PLAYER_NAME.player_frame == 5:
                self.PLAYER_NAME.player_frame = 0
                self.PLAYER_NAME.player_offset_x = 0
                self.PLAYER_NAME.player_offset_y = 0

        # save player's current position
        old_player_x = self.PLAYER_NAME.player_x
        old_player_y = self.PLAYER_NAME.player_y

        # move if key is pressed
        if self.PLAYER_NAME.player_frame == 0:
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                from_player_x = self.PLAYER_NAME.player_x
                from_player_y = self.PLAYER_NAME.player_y
                self.PLAYER_NAME.player_x += 1
                self.PLAYER_NAME.player_direction = "right"
                self.PLAYER_NAME.player_frame = 1

            elif pygame.key.get_pressed()[pygame.K_LEFT]:  # elif stops player making diagonal movements
                from_player_x = self.PLAYER_NAME.player_x
                from_player_y = self.PLAYER_NAME.player_y
                self.PLAYER_NAME.player_x -= 1
                self.PLAYER_NAME.player_direction = "left"
                self.PLAYER_NAME.player_frame = 1

            elif pygame.key.get_pressed()[pygame.K_UP]:
                from_player_x = self.PLAYER_NAME.player_x
                from_player_y = self.PLAYER_NAME.player_y
                self.PLAYER_NAME.player_y -= 1
                self.PLAYER_NAME.player_direction = "up"
                self.PLAYER_NAME.player_frame = 1

            elif pygame.key.get_pressed()[pygame.K_DOWN]:
                from_player_x = self.PLAYER_NAME.player_x
                from_player_y = self.PLAYER_NAME.player_y
                self.PLAYER_NAME.player_y += 1
                self.PLAYER_NAME.player_direction = "down"
                self.PLAYER_NAME.player_frame = 1

        # check for exiting the room
        if self.PLAYER_NAME.player_x == self.room_width:  # through door on RIGHT
            self.current_room += 1
            self.generate_map()
            self.PLAYER_NAME.player_x = 0  # enter at left
            self.PLAYER_NAME.player_y = int(self.room_height / 2)  # enter at door
            self.PLAYER_NAME.player_frame = 0
            self.start_room(screen)
            return

        if self.PLAYER_NAME.player_x == -1:  # through door on LEFT
            self.current_room -= 1
            self.generate_map()
            self.PLAYER_NAME.player_x = self.room_width - 1  # enter at right
            self.PLAYER_NAME.player_y = int(self.room_height / 2)  # enter at door
            self.PLAYER_NAME.player_frame = 0
            self.start_room(screen)
            return

        if self.PLAYER_NAME.player_y == self.room_height:  # through door at BOTTOM
            self.current_room += self.map_width
            self.generate_map()
            self.PLAYER_NAME.player_y = 0  # enter at top
            self.PLAYER_NAME.player_x = int(self.room_width / 2)  # enter at door
            self.PLAYER_NAME.player_frame = 0
            self.start_room(screen)
            return

        if self.PLAYER_NAME.player_y == -1:  # through door at TOP
            self.current_room -= self.map_width
            self.generate_map()
            self.PLAYER_NAME.player_y = self.room_height - 1  # enter at bottom
            self.PLAYER_NAME.player_x = int(self.room_width / 2)  # enter at door
            self.PLAYER_NAME.player_frame = 0
            self.start_room(screen)
            return

        # If the player is standing somewhere they shouldn't, move them back.
        # Keep the 2 comments below - you'll need them later

        if self.room_map[self.PLAYER_NAME.player_y][self.PLAYER_NAME.player_x] not in self.items_player_may_stand_on:
            # or hazard_map[player_y][player_x] != 0:
            self.PLAYER_NAME.player_x = old_player_x
            self.PLAYER_NAME.player_y = old_player_y
            self.PLAYER_NAME.player_frame = 0

        if self.PLAYER_NAME.player_direction == "right" and self.PLAYER_NAME.player_frame > 0:
            self.PLAYER_NAME.player_offset_x = -1 + (0.25 * self.PLAYER_NAME.player_frame)
        if self.PLAYER_NAME.player_direction == "left" and self.PLAYER_NAME.player_frame > 0:
            self.PLAYER_NAME.player_offset_x = 1 - (0.25 * self.PLAYER_NAME.player_frame)
        if self.PLAYER_NAME.player_direction == "up" and self.PLAYER_NAME.player_frame > 0:
            self.PLAYER_NAME.player_offset_y = 1 - (0.25 * self.PLAYER_NAME.player_frame)
        if self.PLAYER_NAME.player_direction == "down" and self.PLAYER_NAME.player_frame > 0:
            self.PLAYER_NAME.player_offset_y = -1 + (0.25 * self.PLAYER_NAME.player_frame)

    def draw_image(self, image, y, x, screen):
        screen.blit(
            image,
            (self.top_left_x + (x * self.TILE_SIZE),
             self.top_left_y + (y * self.TILE_SIZE) - image.get_height())
        )

    def draw_shadow(self, image, y, x, screen):
        screen.blit(
            image,
            (self.top_left_x + (x * self.TILE_SIZE),
             self.top_left_y + (y * self.TILE_SIZE))
        )

    def draw_player(self, screen):
        player_image = self.PLAYER_NAME.PLAYER[self.PLAYER_NAME.player_direction][self.PLAYER_NAME.player_frame]

        self.draw_image(player_image, self.PLAYER_NAME.player_y + self.PLAYER_NAME.player_offset_y,
                        self.PLAYER_NAME.player_x + self.PLAYER_NAME.player_offset_x, screen)

        player_image_shadow = \
            self.PLAYER_NAME.PLAYER_SHADOW[self.PLAYER_NAME.player_direction][self.PLAYER_NAME.player_frame]

        self.draw_shadow(player_image_shadow, self.PLAYER_NAME.player_y + self.PLAYER_NAME.player_offset_y,
                         self.PLAYER_NAME.player_x + self.PLAYER_NAME.player_offset_x, screen)

    def draw(self, screen):
        """This method draw all the game sprites, shadows..."""
        if self.game_over:
            return

        # Clear the game arena area.
        box = pygame.Rect(0, 150, 800, 600)
        pygame.draw.rect(screen, self.RED, box)
        # box = Rect((0, 0), (800, top_left_y + (room_height - 1) * 30))
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
                        image = self.PLAYER_NAME.PILLARS[self.PLAYER_NAME.wall_transparency_frame]

                    self.draw_image(image, y, x, screen)

                    if self.objects[item_here][1] is not None:  # If object has a shadow
                        shadow_image = self.objects[item_here][1]
                        # if shadow might need horizontal tiling
                        if shadow_image in [self.images.half_shadow,
                                            self.images.full_shadow]:
                            shadow_width = int(image.get_width() / self.TILE_SIZE)
                            # Use shadow across width of object.
                            for z in range(0, shadow_width):
                                self.draw_shadow(shadow_image, y, x + z, screen)
                        else:
                            self.draw_shadow(shadow_image, y, x, screen)

                # hazard_here = hazard_map[y][x]
                # if hazard_here != 0:  # If there's a hazard at this position
                #     draw_image(objects[hazard_here][0], y, x)

            if self.PLAYER_NAME.player_y == y:
                self.draw_player(screen)

        # screen.surface.set_clip(None)

    def adjust_wall_transparency(self):
        """This method makes the front wall transparent when the player is behind it"""
        if (self.PLAYER_NAME.player_y == self.room_height - 2
                and self.room_map[self.room_height - 1][self.PLAYER_NAME.player_x] == 1
                and self.PLAYER_NAME.wall_transparency_frame < 4):
            self.PLAYER_NAME.wall_transparency_frame += 1  # Fade wall out.

        if ((self.PLAYER_NAME.player_y < self.room_height - 2
             or self.room_map[self.room_height - 1][self.PLAYER_NAME.player_x] != 1)
                and self.PLAYER_NAME.wall_transparency_frame > 0):
            self.PLAYER_NAME.wall_transparency_frame -= 1  # Fade wall in.

    def start_room(self, screen):
        self.show_text("You are here " + self.room_name, 1, screen)

    def show_text(self, text_to_show, line_number, screen):
        if self.game_over:
            return

        text_lines = [15, 50]
        box = pygame.Rect(0, text_lines[line_number], 800, 35)
        pygame.draw.rect(screen, self.BLACK, box)
        text = self.font.render(text_to_show, False, self.GREEN)
        screen.blit(text, (20, text_lines[line_number]))

    def update_screen(self, screen):
        self.start_room(screen)
        self.player_movement(screen)
        self.adjust_wall_transparency()
        self.draw(screen)
