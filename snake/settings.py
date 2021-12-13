class Settings:
    def __init__(self):
        self.SIZE = 20
        self.WIDTH, self.HEIGHT = 1500, 800
        self.RES = self.WIDTH, self.HEIGHT
        self.HW, self.HH = self.WIDTH // 2, self.HEIGHT // 2

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (150, 0, 0)
        self.LIGHT_YELLOW = (255, 255, 204)
        self.GREEN = (0, 200, 0)

        self.score = 0
        self.fps = 60
