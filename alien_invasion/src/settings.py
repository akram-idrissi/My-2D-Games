class Settings:

	def __init__(self):
		# Screen settings
		self.screen_width = 1000
		self.screen_height = 600 
		self.bg_color = (230, 230, 230)
		self.ship_speed = 5
		self.fps = 240

		# Bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_speed = 4
		self.bullets_number = 3

		# Alien settings
		self.alien_speed = 1

		# Fleet settings
		self.fleet_speed = 5
		self.fleet_direction = 1

		# ship settings 
		self.ship_limit = 3

		# how quickly the game speeds up 
		self.speedup_scale = 1.1
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed = 3
		self.bullet_speed = 3
		self.bullets_number = 3
		self.alien_speed = 1
		self.fleet_direction = 1
		self.alien_point = 50

	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.bullets_number *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.fleet_direction *= self.speedup_scale
		self.alien_point = int(self.alien_point * self.score_scale)
