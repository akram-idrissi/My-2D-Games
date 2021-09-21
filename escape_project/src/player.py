

class Player:

    def __init__(self, name):
        self.name = name

        self.x = 600
        self.y = 350

    def __str__(self):
        return self.name
