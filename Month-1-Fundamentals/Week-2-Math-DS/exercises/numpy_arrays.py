'''
1. Create array of zeros (5,5)
2. Create array of ones (3,3)
3. Create array from 0 to 10 using arange
4. Create 10 equally spaced values between 0-100 using linspace
5. Create random array (4,4)
'''
import numpy as np

arr0 = np.zeros(5)
print(arr0)

arr1 = np.ones(3)
print(arr1)

arr = np.arange(0,11)
print(arr)

linspace = np.linspace(0,100,num=10)
print(linspace)

rand_arr = np.random.randint(0,4)
print(rand_arr)
