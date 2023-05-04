#2
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
name = Circle(radius = 10)
print(f"Радіус кола: {name.radius}")
print(f"Площа кола: {round(name.area(), 2)} см^2")
