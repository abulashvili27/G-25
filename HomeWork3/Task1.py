class MyList:
    def __init__(self, list1=[]):
        self.data = list1

    def __str__(self):
        return f"{self.data}"

    def __add__(self, other):
        result = [self.data, other]
        return result

    def __mul__(self, other):
        result = self.data * other
        return result


if __name__ == '__main__':
    l1 = MyList([1, 2, 3])
    l2 = MyList([6, 7])
    print(l1 * 2)
    print(l1 + l2)
