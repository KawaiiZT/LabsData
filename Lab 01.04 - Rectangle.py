class Rectangle:
    """Docstring"""
    def __init__(self, height, width):
        """Docstring"""
        self.height = height
        self.width = width

    def calculate_area(self):
        """Docstring"""
        area = self.height * self.width
        return area

    def calculate_perimeter(self):
        """Docstring"""
        perimeter = (self.height * 2) + (self.width * 2)
        return perimeter
def main():
    """RRRRR"""
    rectangle = Rectangle(float(input()), float(input()))

    condition = input()
    if condition == "area":
        result = rectangle.calculate_area()
    else:
        result = rectangle.calculate_perimeter()
    print("%.2f" % result)
main()
