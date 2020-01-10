# data transformation using Normalization Method
import numpy as np
from sklearn.preprocessing import Normalizer

X = np.array([[4, 1, 2, 2],
              [1, 3, 9, 3],
              [5, 7, 5, 1]])

# normalizing on rows, works on formula Xi/sqrt(Xi**2+Yi**2+Zi**2)
# adding square of all the values of the row after normalization should be one
transformer = Normalizer().fit(X)  # fit does nothing.

print(transformer.transform(X))