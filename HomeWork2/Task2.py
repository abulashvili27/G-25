a = [123, 44, 654, 77,27]

class Main(list):
   
    def __init__(self, list_1):
     self.list_1 = list_1


    def min(self):
        return min(self.list_1)
    
    def max(self):
        return max(self.list_1)

m = Main(a)
print(f"Min value - {m.min()}, Max value - {m.max()}")


    
    