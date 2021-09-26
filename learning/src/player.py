from images import Images


class Player:
    def __init__(self, name):
        self.images = Images()
        self.name = name

        self.PLAYER = {
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

        self.PLAYER_SHADOW = {
            "left": [self.images.spacesuit_left_shadow, self.images.spacesuit_left_1_shadow,
                     self.images.spacesuit_left_2_shadow, self.images.spacesuit_left_3_shadow,
                     self.images.spacesuit_left_3_shadow
                     ],
            "right": [self.images.spacesuit_right_shadow, self.images.spacesuit_right_1_shadow,
                      self.images.spacesuit_right_2_shadow,
                      self.images.spacesuit_right_3_shadow, self.images.spacesuit_right_3_shadow
                      ],
            "up": [self.images.spacesuit_back_shadow, self.images.spacesuit_back_1_shadow,
                   self.images.spacesuit_back_2_shadow, self.images.spacesuit_back_3_shadow,
                   self.images.spacesuit_back_3_shadow
                   ],
            "down": [self.images.spacesuit_front_shadow, self.images.spacesuit_front_1_shadow,
                     self.images.spacesuit_front_2_shadow, self.images.spacesuit_front_3_shadow,
                     self.images.spacesuit_front_3_shadow
                     ]
        }
        self.player_image_shadow = self.PLAYER_SHADOW["down"][0]
        self.PILLARS = [
            self.images.pillar, self.images.pillar_95, self.images.pillar_80,
            self.images.pillar_60, self.images.pillar_50
        ]
        self.wall_transparency_frame = 0
        
        self.player_direction = "down"
        self.player_frame = 0
        self.player_image = self.PLAYER[self.player_direction][self.player_frame]
        self.player_offset_x, self.player_offset_y = 0, 0
        self.player_x = 5
        self.player_y = 2
