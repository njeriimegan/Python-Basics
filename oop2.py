import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def print_details(self):
        print("Radius:", self.radius)
        print("Area of circle:", self.area)
        print("Circumference of circle with self.radius:", self.circumference)

c1 = Circle(14)
c2 = Circle(35.77)

c1.print_details()
print(c1.area())