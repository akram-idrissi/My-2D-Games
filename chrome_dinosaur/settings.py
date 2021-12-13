class Settings:

    def __init__(self):
        # screen resolution
        self.width = 1000
        self.height = 600
        self.resolution = self.width, self.height

        # dynamic variables
        self.up = 12
        self.fps = 60
        self.score = 0
        self.speed = 20
        self.game_over = False

        # colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.bgr_color = (247, 247, 247)

    def initialize_settings(self):
        self.up = 12
        self.speed = 20
        self.game_over = False
