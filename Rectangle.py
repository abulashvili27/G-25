class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return "Area - " + str(self.width * self.length)

    def perimeter(self):
        return "Perimeter - " + str(2*(self.width + self.length))

    def print_info(self):
        return f"Length - {self.length}, Width - {self.width}, Perimeter - {self.perimeter}, Area - {self.area}"

w = int(input("Width: "))
l = int(input("Length: "))

r = Rectangle(w, l)
print(r.perimeter())
print(r.area())
print(r.print_info())



