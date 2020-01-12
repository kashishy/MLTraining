# Operations on two arrays
import numpy as np

n1 = np.array([4, 5, 6])
n2 = np.array([1, 2, 3])

print("\n")
print("n1 = ", n1)
print("n2 = ", n2)

# operation broadcasting is allowed between two arrays of same dimensions and of numpy type
# shape remains same after broadcasting
print("n1+n2 = ", n1+n2) # output [5 7 9]
print("n1-n2 = ", n1-n2) # output [3 3 3

n3 = np.array([4, 5, 6, 7])

# not allowed because of different dimensions
# shape must be same, size will be same if shape same
print(n1+n3)
# ValueError : operands could not be broadcast together with shapes (3,) (4,)