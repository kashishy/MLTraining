import numpy as np
# all rows must have same number elements to make it 2-D array
# otherwise it will make all row as list
d1 = np.array([[1, 2],
               [3, 4],
               [5, 6],
               [7, 8],
               [9, 10],
               [11, 12],
               [13, 14]])

print(d1)
print(d1.shape)

# dimensions(maximum depth of bracket opening)
print(d1.ndim)

# Entire expression before "," is for rows
# print elements of 1st column of odd indexed rows
print("d1[: :2,0] = ", d1[: :2, 0]) # output will be 1,5,9,13

# print elements of 2nd column of even indexed rows
print("d1[1: :2,0] = ", d1[1: :2, 1])

# print entire rows alternatively
print("d1[: :] = ", d1[: :2])