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

arrange = np.arange(0,11)
print(arrange)

linspace = np.linspace(0,100,num=10)
print(linspace)

rand_arr = np.random.randint(0,4)
print(rand_arr)


'''
Given: arr = np.array([10, 20, 30, 40, 50])
1. Access first, last, middle element
2. Get elements from index 1-3
3. Get every 2nd element
4. Reverse the array
'''
arr = np.array([10, 20, 30, 40, 50])
print(f"First element: {arr[0]}, Last element: {arr[-1]},Middle element: {arr[arr.size/2]}")

print(f"Reversed array: {arr[::-1]}")
print(f"elements from index 1-3{arr[1:4]}")
print(f"Every 2nd element:{arr[::2]}")

'''
Given two arrays: a = [1,2,3,4,5], b = [2,4,6,8,10]
1. Add them
2. Subtract them
3. Multiply them
4. Divide them
5. Element-wise power (a^2)
6. Sum, mean, std of array
'''
a = np.array([1,2,3,4,5])
b = np.array([2,4,6,8,10])
print(f"Addition: {np.add(a,b)}")
print(f"Subtraction: {np.subtract(a,b)}")
print(f"Multiplication: {np.multiply(a,b)}")
print(f"Division: {np.divide(a,b)}")
print(f"element wise power: {np.power(a,2)}")
print(f"Sum: {np.sum(a)}, Mean: {np.mean(a)}, STD: {np.std(a)}")

'''
1. Create 3x3 matrix
2. Access element at [1,2]
3. Get row 1
4. Get column 2
5. Reshape to (9,1)
6. Transpose it
'''
3D_arr = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(3D_arr[1,2])
print(3D_arr[:,2])
print(3D_arr.reshape(9,1))
print(3D_arr.T)

'''
Matrix operations

Given matrices:
A = [[1,2], [3,4]]
B = [[5,6], [7,8]]

1. Matrix multiplication (A @ B)
2. Element-wise multiplication
3. Inverse of A
4. Determinant of A
'''

A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])

print(f"Matrix multiplication: {np.dot(A,B)}")
print(f"Element wise multiplication: {np.multiply(A,B)}")
print(f"Inverse of A: {np.linalg.inv(A)}")
print(f"Determinant of A: {np.linalg.det(A)}")


