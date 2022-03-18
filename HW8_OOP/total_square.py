import math


class Shape:  # class Shape(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def square(self):
        return (self.width * self.height) * math.sin(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Triangle(Shape):
    def __init__(self, x, y, a, b, c):
        super().__init__(x, y)
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 1 / 2

    def __str__(self):
        result = super().__str__()
        return result + f'\nTriangle {self.a}, {self.b}, {self.c}'


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass


r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)

c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)

par = Parallelogram(1, 2, 20, 30, 45)
print(par.x)
par1 = Parallelogram(1, 2, 20, 30, 45)
str(par1)

tri = Triangle(50, 50, 12, 15, 10)
tri1 = Triangle(0, 50, 20, 10, 5)

scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(c)
scene.add_figure(c1)
scene.add_figure(par)
scene.add_figure(par1)
scene.add_figure(tri)
scene.add_figure(tri1)

scene.total_square()
