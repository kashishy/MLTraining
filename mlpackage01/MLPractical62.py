from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings(action="ignore")

# plt.style.use('ggplot')
# plt.rcParams['figure.figsize'] = (8,6)
# Importing the dataset

data = pd.read_csv('KMeansData.csv')
print("input data and shape")
print(data.shape)
print(data.head())


# getting the values and plotting
f1 = data["V1"].values
f2 = data["V2"].values

plt.scatter(f1, f2, c="black", s=10)
plt.show()

X = np.array(list(zip(f1, f2)))

print(X)

# Euclidean Distance Calculation
def eu_dist(a, b, ax=1):
    return np.linalg.norm(a-b, axis=ax)

# Number of clusters
k = 3
# X coordinate of random centroid
C_x = np.random.randint(0, np.max(X), size=k)
print("C_x = ", C_x)
# Y coordinate of random centroid
C_y = np.random.randint(0, np.max(X), size=k)
print("C_y = ", C_y)

C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
print("Initial Centroids (random centroid) : ")
print(C)
print(C.shape)

plt.scatter(f1, f2, s=10, c="k")
plt.scatter(C_x, C_y, marker="*", s=300, c="r")
plt.show()

# To store the value of centroids when it updates
C_old = np.zeros(C.shape)
print("C = \n", C)
print("C_old = \n", C_old)
print("len(X) = ", len(X))

# Cluster Labels (0, 1, 2)
clusters = np.zeros(len(X))

print("clusters = ", clusters)
# Error function - Distamce between two centroids(new and old)
error = eu_dist(C,C_old)
print("Error before loop", error)
# Loop will run till the error becomes zero
while error.all():   # error! = 0
    # Assigning each value to its closest cluster
    for i in range(len(X)):
        distances = eu_dist(X[i], C)
        cluster = np.argmin(distances)  # cluster 2
        clusters[i] = cluster
    # Storing the old centroid values
    C_old = deepcopy(C)
    # Finding the new centroids by taking the average value
    for s in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j] == s]
        C[s] = np.mean(points, axis=0)
    error = eu_dist(C, C_old)
    print("Error in loop", error)

colors = ['b', 'c', 'r']
fig, ax = plt.subplots()
for i in range(k):
    points = np.array([ X[j] for j in range(len(X)) if clusters[j]==i])
    ax.scatter(points[:, 0], points[:, 1], s=25, c=colors[i])
ax.scatter(C[:, 0], C[:, 1], marker="*", s=100, c='y')

print("Final Centroid ", C)
plt.show()