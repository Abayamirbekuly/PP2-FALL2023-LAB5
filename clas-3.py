class Rectangle(Shape):  
    def __init__(self, length, width):
        super().__init__()  
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))


rectangle = Rectangle(length, width)


print(f"Area of the rectangle: {rectangle.area()}")
