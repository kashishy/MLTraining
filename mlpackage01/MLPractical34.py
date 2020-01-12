import numpy as np

print("---Sum by row and by columns:---")

x = np.array([[1, 2], [3, 4]])
print("x = \n", x)

print(x.sum())

# column by column addition
print(x.sum(axis=0))
# output array([4, 6])

# sum elements of 1st column and sum of elements of 2nd column
print(x[:, 0].sum(), x[:, 1].sum())

# sum of elements of each row
print(x.sum(axis=1))
print(x[0, :].sum(), x[1, :].sum())