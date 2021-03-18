import csv
n = []
sur = []
a = []
s = []  
  
class Employee:

 def __init__(self, name = [], surname = [], age = [], salary = []):
    self.name = name
    self.surname = surname
    self.age = age
    self.salary = salary

 def minSalary(self):
     x = min(self.salary)
     minSalaryName = self.name[x]
     minSalarySurname = self.surname[x]
     minSalaryAge = self.age[x]
     minSalarySalary = self.salary[x]
     print(f"Name - {minSalaryName}, Surname - {minSalarySurname}, Age - {minSalaryAge}, Salary - {minSalarySalary} ")

 def maxAge(self):
     y = max(self.age)
     maxAgeName = self.name[y]
     maxAgeSurname = self.surname[y]
     maxAgeAge = self.age[y]
     maxAgeSalary = self.salary[y]
     print(f"Name - {maxAgeName}, Surname - {maxAgeSurname}, Age - {maxAgeAge}, Salary - {maxAgeSalary} ")
     
    
    
 with open('dataset1.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in csv_reader:
        n.append(i[0])
        sur.append(i[1])
        a.append(i[2])
        s.append(i[3])
 
 


e = Employee(n, sur, a, s)
e.minSalary
e.maxAge