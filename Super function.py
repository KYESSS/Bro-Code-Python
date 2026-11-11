
# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled else 'not filled'}.")


class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2,")
        super().describe()

class Square(Shape):
    def __init__(self, colour, is_filled, width):
        super().__init__(colour, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2,")
        super().describe()

class Triangle(Shape):
    def __init__(self, colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a trianagle with an area of {self.width * self.height / 2}cm^2,")
        super().describe()

circle = Circle("red", True, 5)
square = Square("blue", True, 10)
triangle = Triangle("green", False, 25, 50)

print(f"The circle is {circle.colour}, the circled is filled {circle.is_filled} and the radius of the circle is {circle.radius}cm.")
circle.describe()
print(f"The square is {square.colour}, the square is filled {square.is_filled} and the width and height of the square is {square.width}cm.")
square.describe()
print(f"The triangle is {triangle.colour}, the triangle is filled {triangle.is_filled}, the width {triangle.width}cm and the height is {triangle.height}cm.")
triangle.describe()