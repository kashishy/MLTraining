import numpy as np

arr = np.array([11, 22, 33, 0., 44, 55])

# this is for only numpy type array
print("arr.sum() = ", arr.sum())
# this can be used in any type of numerical array(old or numpy type)
print(np.sum(arr))

print("arr.std() = ", arr.std())
# for numpy type array
print("arr.mean() = ", arr.mean())
# for old type of array
print(np.mean(arr))

print("arr.max() = ", arr.max())
print("arr.min() = ", arr.min())

print("arr.size = ", arr.size)
print("arr.shape = ", arr.shape)