'''
Day 4: Advanced Python & Project (10 exercises)

Lambda functions (square, add, filter, map)
Decorators (timer)
Generators
JSON operations
Regular expressions
List of dicts (filtering, sorting)
Modules & imports
API requests (GitHub API)
Data processing
Final Project: Todo CLI App (full project with all concepts)
'''

#lambda functions

plain = [1,2,3,4,5]
squared=list(map(lambda a: a*a,plain))
print(squared)

even_list = list(map(lambda a: a%2==0,plain))
print(even_list)

def countdown(n):
    for i in range(n,-1,-1):
        yield i
print(list(countdown(5)))

def fib(limit):
    n1=0
    n2=1
    while n1<= limit:
        yield n1
        n1=n2
        n2=n1+n2

print(list(fib(100)))
