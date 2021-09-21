class Settings:

	def __init__(self):

		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)

		self.FPS = 40
		self.WIDTH, self.HEIGHT = 600, 400

		self.exit = False
		self.attempts = 0 
		self.max_attempts = 100000
		self.gap = 3

		self.allowed_circle = 10
		self.count = 0

	