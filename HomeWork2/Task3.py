

class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def info(self):
        return f"Name - {self._name}, Age - {self._age}"

class Dog(Animal):
    def __init__(self, breed, color):
        super().__init__(name, age)
        self._name = name
        self._age = age
        self._breed = breed
        self._color = color
    
    def full_info(self):
        return f"Breed - {self._breed}, Color - {self._color}"
    
name = "Max"
age = "1 Year"   
breed = "Husky"
color = "Gray"
a = Animal(name, age)
d = Dog(breed, color)
print(d.info() + ", " + d.full_info())