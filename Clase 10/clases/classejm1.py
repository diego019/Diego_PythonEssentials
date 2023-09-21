# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:40:50 2019

@author: Juan Carlos
"""
##es como crear un molde y el molde viene con todo eso
# una clase es como una plantilla
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d", Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Employee class"      
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp3 = Employee("A",8000)
emp4 = Employee("b",8000)
emp5 = Employee("Diego",100000)
emp6 = Employee("Lucas",800000)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
emp5.displayEmployee()
emp6.displayEmployee()
print ("Total Employee %d" % Employee.empCount)