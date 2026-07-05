'''
Exercise 1: Vector Operations

Given vectors:
v1 = [1, 2, 3]
v2 = [4, 5, 6]

1. Calculate dot product
2. Calculate cross product
3. Calculate magnitude of each
4. Calculate angle between them
5. Normalize vectors
'''

import numpy as np 

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

print(np.dot(v1,v2))
print(np.cross(v1,v2))
magv1=np.linalg.norm(v1)
magv2=np.linalg.norm(v2)
costheta = np.dot(v1,v2) / (magv1 * magv2)
angle_radians = np.arccos(costheta)
print(np.degrees(angle_radians))
print(v1/magv1)
print(v2/magv2)

'''
Exercise 2
1. Create 4x4 matrix
2. Access element at [2,3]
3. Get row 1
4. Get column 2
5. Get diagonal elements
6. Check if symmetric
'''

arr_4D = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print("Access element at [2,3]: ",arr_4D[2,3])
print("Get row 1: ",arr_4D[1])
print("Get column 2: ",arr_4D[:,2])
for i in range(4):
    for j in range(4):
        if i==j:
            print(arr_4D[i,j])
# or np.diag(arr_4D)
# check if symmetric A = A.T
is_symmetric = np.array_equal(arr_4D,arr_4D.T)
print(is_symmetric)

'''
Exercise 3

Given matrices A and B (3x3):
1. Multiply A * B
2. Calculate A transpose
3. Calculate determinant of A
4. Calculate inverse of A
5. Verify A * A_inv = Identity
'''
A = np.array([[7,5,8],[3,4,2],[1,2,3]])
B = np.array([[4,5,6],[7,4,2],[5,6,8]])

print(np.matmul(A,B))
print(A.T)
print(np.linalg.det(A))
a_inv = np.linalg.inv(A)
print(a_inv)

Identity = np.identity(3)
left = np.matmul(A,a_inv)
print(np.allclose(left,Identity))


'''
Matrix Decomposition - SVD

Given matrix M (4x3):
1. Perform SVD: U, S, Vt = np.linalg.svd(M)
2. Reconstruct M from U, S, Vt
3. Verify reconstruction
4. Analyze singular values (importance)
5. Rank of matrix
'''

