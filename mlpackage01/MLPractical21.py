# Data transformation using Binarizer Method
import numpy as np
from sklearn.preprocessing import Binarizer

X = np.array([[1., -1., 2.],
              [2., 0.,  0.],
              [0., 1., -1.]])

transformer = Binarizer(threshold=5)

print(transformer.fit_transform(X))