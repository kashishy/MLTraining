import numpy as np

# matrix of (3,4) filled with 0
zr = np.zeros([3, 4])
print("Zero filed array zr = \n", zr)

# matrix of (4,4) filed with 1's
ar = np.ones([4, 4])
print("1's filed array ones = \n", ar)

# for matrix filed with 4, multiply ones matrix by 4
print(ar*4)

# data type of elements of matrix
print(ar.dtype)

# array filed with 0's of size 5
zr2 = np.zeros(5)
print("Zero filed array zr2 = \n", zr2)