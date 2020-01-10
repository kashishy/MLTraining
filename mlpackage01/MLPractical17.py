# data transformation using Standardize method
from sklearn.preprocessing import StandardScaler
from pandas import read_csv
from numpy import set_printoptions
import numpy as np

filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'ples', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = read_csv(filename, names=hnames)

# data values without headings
array = dataframe.values

# separating input and output features, X->input features and Y->output features
X = array[:, 0:8]
Y = array[:, 8]

scaler = StandardScaler()
rescaledX = scaler.fit_transform(X)

set_printoptions(precision=3)
print(rescaledX[:30, :])

print("\n\n Mean of First coloum = ")
# mean can be checked  of any feature from input and it should be closed to 0 in Standardize transformation
print(np.mean(rescaledX[:, 0]))