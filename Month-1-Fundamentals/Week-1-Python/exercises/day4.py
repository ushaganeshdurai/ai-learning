'''
Day 4: Data Structures & Problem Solving (10 exercises)
1. Lists
Find the largest number in a list
Find the second largest number
Remove duplicates from a list
'''

list1 = [5,7,8,4,6]
maximum=list1[0]
for item in list1:
    if item>maximum:
        maximum=item
print(maximum)

'''
2. Tuples
Create a tuple and access elements
Convert tuple to list and back
'''
tup = (1,2,3,4,5)
list3=[]
for item in tup:
    print(item)
    list3.append(item)
tuple(list3)

#tuple unpacking
employee = ("John",25,"Developer",75000)
name,age,role,salary = employee
print("Name: ",name)
print("Role: ",role)
print("Salary: ",salary)

'''
3. Dictionaries
Count frequency of characters in a string
Store student marks in a dictionary and find the topper
'''


'''
4. Sets
Find common elements between two lists using sets
Find unique elements
'''

'''
5. String Practice
Reverse a string
Check if a string is a palindrome
Count vowels and consonants
'''

'''
6. Mini Challenges
FizzBuzz
Prime number checker
Number guessing game
'''

'''
7. Problem Solving

Solve 5–10 easy problems from:

LeetCode
HackerRank Python

Recommended easy problems:

Two Sum
Valid Palindrome
Contains Duplicate
FizzBuzz
Running Sum of 1D Array
Why Day 4?

You've learned:

Variables
Loops
Functions
OOP

The next skill employers test is manipulating data using:

Lists
Dictionaries
Strings
Sets

These are used constantly in coding interviews, automation scripts, backend development, data analysis, and AI/ML preprocessing.
After Day 4, Day 5 should be:
File Handling + Modules + Exception Handling + CSV/JSON basics, which prepares you for real-world Python projects.
'''


