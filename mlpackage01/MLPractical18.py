# data transformation using Normalization method
from sklearn.preprocessing import Normalizer
from pandas import read_csv
from numpy import set_printoptions

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'ples', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = read_csv(filename, names=hnames)
# data values without headings
array = dataframe.values

# separating input and output features
X = array[:, 0:8]
Y = array[:, 8]

scaler = Normalizer()
normalizedX = scaler.fit_transform(X)

set_printoptions(precision=2)
print(normalizedX[0:30, :])