import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius
    
circle1 = Circle(8)

# print(circle1)
# print(circle1.area())


class Mircle:
    def __init__(self, radius = 3):
        self.radius = radius 
    
    def area(self):
        return math.pi * self.radius * self.radius
    
mircle1 = Mircle(7)

# print(mircle1)

# print(mircle1.area())