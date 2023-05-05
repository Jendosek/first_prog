#2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.result_1 = width * height
        self.result_2 = 2 * (width + height)
name = Rectangle(width = 10, height = 6)
print(f"Довжина = {name.width}")
print(f"Висота  = {name.height}")
print("--------------------------")
print(f"Периметр прямокутника: {name.result_2}")
print(f"Площа прямокутника: {name.result_1}")
