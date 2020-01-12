import numpy as np

n4 = np.array([777, 555, 222, 111, 999, 666])

print("n4 = ", n4)
# argsort() gives index position of elements in sorted from original array
print("n4.argsort():", n4.argsort())
# output [3 2 1 5 0 4]

# index array
indxArr = n4.argsort()
print("Min = ", n4[indxArr[0]])

print("Max = ", n4[indxArr[len(indxArr)-1]])