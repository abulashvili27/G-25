class CallMixin:


class Person:
    def __init__(self, fname, lname, phone):
        self.fname = fname
        self.lname = lname
        self.phone = phone

    def info(self):
        return f"First name - {self.fname}, Last name - {self.lname}, Phone number - {self.phone}"
    

#ვერ მივხვდი დარეკვის ფუნქცია როგორ გამეკეთებინა