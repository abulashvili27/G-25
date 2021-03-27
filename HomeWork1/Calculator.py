class Calculator:
    
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
    
    def result(self):
        if self.symbol == "-":
            print(self.x - self.y)
        elif self.symbol == "+":
            print(self.x + self.y)
        elif self.symbol == "*":
            print(self.x * self.y)
        else:
            print(self.x / self.y)
    

a = int(input("First Number: "))
operation = input("Operation (+, -, *, /): ")
b = int(input("Second Number: "))

c = Calculator(a, b, operation)
c.result()
   