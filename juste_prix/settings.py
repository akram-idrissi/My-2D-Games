class Settings:

    def __init__(self):
        self.width = 800
        self.height = 600

        self.fps = 60
        self.score = 0

        self.write = False
        self.help_user = False

        self.white = (255, 255, 255)
        self.color_active = (200, 200, 200)
        self.color_passive = (130, 130, 130)
        self.background = (240, 240, 240)

        self.color = self.color_passive
