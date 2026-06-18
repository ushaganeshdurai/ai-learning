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

'''
 Student Class with Grade Logic
Task:
Create a Student class that calculates grades.
Requirements:

Attributes: name, marks
Method:

get_grade()

90+ → A
80–89 → B
70–79 → C
<70 → D




Method to display student details + grade
'''

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_grade(self):
        if self.marks in range(90,101):
            return "A"
        elif self.marks in range(80,90):
            return "B"
        elif self.marks in range(70,80):
            return "C"
        else:
            return "D"
    def display(self):
        return f"{self.name}'s marks is :{self.marks} and grade is {self.get_grade()}"
 

student1 = Student("Usha",101)
print(student1.display())

      

student_list =[{"name":"Andres","marks":89},{"name":"julius","marks":90},{"name":"subha","marks":80},{"name":"karpathy","marks":67},{"name":"asha","marks":99}]
for i in range(len(student_list)):
    list1=Student(student_list[i]["name"],student_list[i]["marks"])
    print(list1.display())
    if list1.get_grade()=="A":
        print(student_list[i]["name"])

with open("student_data.csv","w") as f:
    for student in student_list:
        f.write(f"{student['name']} {student['marks']}\n")
'''
Shopping Cart Class
Task:
Design a ShoppingCart system.
Requirements:

Methods:

add_item(name, price, quantity)
remove_item(name)
calculate_total()


Store items internally (list or dictionary)
Print full cart summary (items + total price)
'''
class ShoppingCart:
    def __init__(self):
        self.cart=[]
       
    def add_item(self,name,price,quantity):
        self.cart.append({"name":name,"price":price,"quantity":quantity})
    
    def remove_item(self,name):
        for item in self.cart:
            if item["name"]==name:
                self.cart.remove(item)
                break

    def calculate_total(self):
        total=0
        for items in self.cart:
            total+=items["price"]*items["quantity"]
        return total
        
    def display_cart(self):
        for item in self.cart:
            print(f"{item['name']} - {item['quantity']} * {item['price']}")
    
sc = ShoppingCart()
sc.add_item("Vegetables",78,3)
sc.remove_item("Vegetables")
sc.add_item("Fruits",78,3)
sc.add_item("Stationery",67,5)
sc.display_cart()
print(f"Total is {sc.calculate_total()}")



'''
Inheritance (Animal, Dog, Cat)
Task:
Demonstrate inheritance.
Requirements:
Base class: Animal
Method: speak()
Derived classes:
Dog → overrides speak() (“Bark”)
Cat → overrides speak() (“Meow”)

Create objects and call methods
'''

class Animal:
    def speak(self):
        return "Animal speaks.."

class Dog(Animal):
    def speak(self):
        return "Barks"

class Cat(Animal):
    def speak(self):
        return "Meow"

cat1 = Cat()
dog1=Dog()
print(cat1.speak())
print(dog1.speak())

'''
Static Methods
Task:
Create a utility class.
Example idea:
MathUtils
Requirements:

Static methods:

is_even(number)
is_prime(number)

Call methods without creating an object
'''
class MathUtils:
    def __init__(self,number):
        self.number=number
    @staticmethod
    def is_even(number):
        if number%2==0:
            return True
        return False
    @staticmethod
    def is_prime(number):
        if number<=1:
            return False
        for i in range(2,number):
            if number%i==0:
                return False
        return True
print(MathUtils.is_even(67))
print(MathUtils.is_prime(9))
'''
 Class Methods & Variables
Task:
Track number of objects created.
Requirements:

Class: Employee
Class variable: employee_count
Increment count every time a new object is created
Class method:

get_employee_count()
Print total employees
'''

class Employee:
    employee_count=0
    emp_list=[]
    def __init__(self,name):
        self.name=name
        Employee.employee_count+=1
        Employee.emp_list.append(name)
     
    @classmethod
    def get_employee_count(cls):
        print(f"Total employees: {cls.employee_count}")

    def list_out(self):
        for e in self.emp_list:
            print(e,end="\n")

emp = Employee("summa")
emp1 = Employee("summaa")

Employee.get_employee_count()
emp1.list_out()

'''
File + Class Integration
Task:
Combine classes with file handling.
Requirements:

Use Student class
Save student data to a file (text/CSV)
Read data back and recreate objects
Display all students
'''

