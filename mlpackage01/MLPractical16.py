# Data transformation using rescaling(custom values)
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# two values x1 and x2 are passed in data
data = np.array([[-1, 2],
                [-0.5, 6],
                [0, 10],
                [1, 18]])
# data without transformation
print(data)

scaler = MinMaxScaler(feature_range=(1, 5))
# data after transformation
print(scaler.fit_transform(data))
print("Minimum Value : ", scaler.data_min_)
print("Maximum Value : ", scaler.data_max_)