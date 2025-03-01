class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


circle = Circle(5)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())

