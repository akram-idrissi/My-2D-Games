import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def get_c(self):
        return self.x, self.y

    def add(self, n_vector):
        self.x += n_vector.x
        self.y += n_vector.y

    def substract(self, n_vector):
        self.x -= n_vector.x
        self.y -= n_vector.y

    def mul(self, scaler):
        self.x *= scaler
        self.y *= scaler

    def div(self, scaler):
        self.x /= scaler
        self.y /= scaler

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        mag = self.magnitude()
        if mag != 0 and mag != 1:
            self.div(mag)

    def limit(self, value):
        if self.magnitude() > value:
            self.normalize()
            self.mul(value)

    def set_mag(self, value):
        self.normalize()
        self.mul(value)

    @staticmethod
    def static_div(vector1, scaler):
        vector3 = Vector(0, 0)
        vector3.x = vector1.x / scaler
        vector3.y = vector1.y / scaler
        return vector3
