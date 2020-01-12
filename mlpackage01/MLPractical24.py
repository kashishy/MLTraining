import numpy as np
print("--------------------------------")
# array will contain only one bracket, internal bracket can have any number of brackets,
# format of sub brackets must be same ( number of elements inside sub brackets must be same)
ddarr = np.array([[1, 2, 3], [4, 5, 6]])

print("ddarr.ndim = ", ddarr.ndim)
# shape of the array (number rows and number of column)
print("ddarr.shape = ", ddarr.shape)
# ddarr.shape = (2L, 3L)

# total number of elements in the array
print("ddarr.size = ", ddarr.size)
print("len(ddarr) = ", len(ddarr))
# data type of the elements of the arry
print("ddarr.dtype = ", ddarr.dtype)
# print data as matrix
print(ddarr)

print("***********************************")
print("ddarr[0.1] = ", ddarr[0, 1])
print("ddarr[0] = ", ddarr[0])

print("ddarr[:,0] = ", ddarr[:, 0])
print("ddarr[1,:] = ", ddarr[1, :])