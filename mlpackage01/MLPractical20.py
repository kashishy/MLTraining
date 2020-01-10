# Binarizer data transformation Method
from sklearn.preprocessing import Binarizer
from pandas import read_csv

filename = 'indians-diabetes.data.csv'
names = ['preg', 'ples', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = read_csv(filename, names=names)
array = dataframe.values

X = array[:, 0:8]
Y = array[:, 8]

# threshold value set the boundary value to convert continues values into binary(values above 5 will be converted
# to 1 and values below or equal to 5 converted to 0
binarizer = Binarizer(threshold=6)

binaryX = binarizer.fit_transform(X)

# summarized transformed data
print(binaryX[0:30, :])