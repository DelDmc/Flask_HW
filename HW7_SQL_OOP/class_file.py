class Point:
    def __init__(self, x_p, y_p):
        self.x_p = x_p
        self.y_p = y_p


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point_instance):
        if (point_instance.x_p - self.x) ** 2 + \
           (point_instance.y_p - self.y) ** 2 <= self.radius ** 2:
            return True
        else:
            return False


