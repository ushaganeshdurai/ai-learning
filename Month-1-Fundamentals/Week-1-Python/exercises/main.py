# Simple Loop
for i in range(1,10):
    print(i)

sum=0
for i in range(1,10):
    sum+=i
print(sum)

#List operation

list1 = []
list1.append(1)
list1.remove(1)

names = ["Lakshmi","Ganesh","VS code"]
for i in range(len(names)):
    print("Hello"+names[i])



# Functions, Dictionaries & File I/O (10 exercises)

# Simple function
# Function with conditional
# Function with loop
# List as parameter (average)
# Dictionary creation
# Dictionary loop
# Function returns dictionary
# File write
# File read
# List comprehension

# Simple function
def greet(name):
    return "Hello, " + name + "!"

print(greet("Lakshmi"))

# Function with conditional

def check_even_odd(num):
    if num %2==0:
        return "Even"
    else:
        return "Odd"
    
check_even_odd(10)
check_even_odd(7)
check_even_odd(25)

# Function with loop
def print_table(num):
    for i in range(1,10):
        print(num +"x"+i+"="+num*i)

print_table(5)

# List as parameter (average)
avg = 0 
def find_average(numbers):
    return sum(numbers)/len(numbers)

test = [78, 85, 92, 67, 88]
print(find_average(test))

# Dictionary creation
dict1 = {"Name":"Usha","Age":22,"Department":"CSE","CGPA":8.6}
print(dict1["Department"])


# Dictionary loop
student = {
    "name": "Asha",
    "age": 20,
    "cgpa": 8.5
}

for key, value in student.items():
    print(key, ":", value)

# Function returns dictionary
def create_employee(name,salary,department):
    return {"Name":name,"Salary":salary,"Department":department}

# File write
sentences = ["Python is easy.","Functions make code reusable.","File handling is important."]
with open("notes.txt","w") as f:
    for i in range(len(sentences)):
        f.write(sentences[i])
    
    
# File read
with open("notes.txt") as f:
    print(f.read())

#List comprehension

numbers = [1,2,3,4,5,6,7,8,9,10]
new_list =[]

for i in range(len(numbers)):
    if numbers[i]%2==0:
        new_list.append(numbers[i])

'''
Mini Project Challenge (Combines Everything)

Create a program that:

Stores student marks in a dictionary.
Uses a function to calculate the average.
Writes the result to a file called report.txt.
Reads the file and displays the report.

'''

def create_student(name,marks):
    return {"name":name,"marks":marks}

studentdict = create_student("Usha",[85,90,80])
def find_avg(studentdict):
    return sum(studentdict["marks"])/len(studentdict["marks"])

with open("report.txt","w") as f:
    f.write(str(find_avg(studentdict)))

with open("report.txt") as f:
    print(f.read())
