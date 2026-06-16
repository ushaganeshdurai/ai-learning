'''
Day 3: OOP & Classes (10 exercises)

Simple class
Calculator class with methods
Student class with grade logic
List of objects
Shopping cart class
Inheritance (Animal, Dog, Cat)
Static methods
Class methods & variables
Exception handling
File + Class integration
'''
class Person:
    def __init__(self,name,age):
       self.name = name 
       self.age = age
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")
person1 = Person("Alice",20)
person1.introduce()

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b=b
    def add(self):
        print(self.a +self.b)

    def subtract(self):
        print(self.a - self.b)

    def multiply(self):
        print(self.a * self.b)

    def divide(self):
        print(self.a/self.b)

calc = Calculator(10,8)
calc.add()
calc.subtract()
calc.divide()
calc.multiply()