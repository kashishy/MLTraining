from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
# Importing the dataset
filename = 'KMeansData.csv'
data = pd.read_csv(filename)
print("Kmeans of sklearn")
# Number of clusters
kmeans = KMeans(n_clusters=3)


# getting the values and plotting
f1 = data["V1"].values
f2 = data["V2"].values

X = np.array(list(zip(f1, f2)))
# fitting the input data
kmeans = kmeans.fit(X) # calculation of centroids
# Getting the cluster labels
labels = kmeans.predict(X)
print("labels : ", labels)
print(list(zip(X, labels)))

# Centroid values
centroids = kmeans.cluster_centers_
print("Best place for new shop\n", centroids)