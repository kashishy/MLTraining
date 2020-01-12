# Sorting of array
import numpy as np

n4 = np.array([10, -1, 0, 90, 300, 3, -6, 2])

print("Before : ", n4)

# External sorting, in this no change in original array, new copy created with sorted values
print(sorted(n4))

print("After : ", n4)

# In-place sorting (Internal Sorting), original array changes
n4.sort()
print("After n4.sort() = ", n4)