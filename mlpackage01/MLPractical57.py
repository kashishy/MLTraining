# B.3)-Cross Validation Regression R2 Error

import pandas as pd
# for splitting historic data in train and test data
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
# for discrete output
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings(action='ignore')

# Continuous values in output so Linear Regression will work
filename = 'housing.csv'
hnames = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

# selecting input and output features
X = array[:, 0:13]
Y = array[:, 13]

# creating object of class
model = LinearRegression()

# for selecting number groups in historic data
num_folds = 10
# splitting data in training and testing data
kfold = KFold(n_splits=num_folds, random_state=7)

# mean absolute error
scoringMethod = 'r2'

# calculating accuracy of model(testing, training and comparing predicted output with the actual output)
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoringMethod)

# printing mean absolute error, best is it should be zero
# negative sign show not good thing, try to make it zero
# deviation in avg error is std
print("R^2: %.3f" % (results.mean()))