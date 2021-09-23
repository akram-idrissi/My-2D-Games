from images import Images


class Player:

    def __init__(self, name):
        self.images = Images()
        self.name = name

        self.x = 600
        self.y = 350

        self.player_movements = {
            "left": [self.images.spacesuit_left, self.images.spacesuit_left_1,
                     self.images.spacesuit_left_2, self.images.spacesuit_left_3,
                     self.images.spacesuit_left_4
                     ],
            "right": [self.images.spacesuit_right, self.images.spacesuit_right_1,
                      self.images.spacesuit_right_2, self.images.spacesuit_right_3,
                      self.images.spacesuit_right_4
                      ],
            "up": [self.images.spacesuit_back, self.images.spacesuit_back_1,
                   self.images.spacesuit_back_2, self.images.spacesuit_back_3,
                   self.images.spacesuit_back_4
                   ],
            "down": [self.images.spacesuit_front, self.images.spacesuit_front_1,
                     self.images.spacesuit_front_2, self.images.spacesuit_front_3,
                     self.images.spacesuit_front_4
                     ]
        }

        self.player_y, self.player_x = 2, 5
        self.player_direction = "down"
        self.player_frame = 0
        self.player_image = self.player_movements[self.player_direction][self.player_frame]
        self.player_offset_x, self.player_offset_y = 0, 0

    def __str__(self):
        return self.name
