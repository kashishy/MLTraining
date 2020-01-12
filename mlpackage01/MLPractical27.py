import numpy as np

# we can create numpy array from range 1 to 5
# for 0 to 5 np.arange(6)
ar = np.arange(1, 6)

print("ar = ", ar)
# output [1,2,3,4,5]

ar[3] = 16

print("After updating ar = ", ar)
# output [1,2,3,16,5]