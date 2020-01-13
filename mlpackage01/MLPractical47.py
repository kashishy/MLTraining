# 2)-Evaluate using k-Fold Cross validation

import pandas as pd
# for splitting historic data in train and test data
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
# for discrete output
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings(action='ignore')

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

X = array[:, 0:8]
Y = array[:, 8]

# creating object of class
model = LogisticRegression()

# for selecting number groups in historic data
num_folds = 10
# splitting data in training and testing data
kfold = KFold(n_splits=num_folds)

# for accuracy of the model, model is checked against testing data(i.e. one hided group in historic data)
# it will do n time training and testing by selecting test group one by one
# it is dedicated function to do many type of accuracy
# here only model type changes for continiuos and discrete data
# kfold will divide X,Y in kfold times and hide one part
# train model by remaining parts of the data, and then find predicted value against tested X
# and then compare the predicted value with test output value
results = cross_val_score(model, X, Y, cv=kfold)

# results will have kfold numbers(accuracies)
print("Results = ", results)

# average accuracy
print("Accuracy = %.3f %%" % (results.mean()*100.0))

# deviation of accuracies
print("Std.Deviation = %.3f" % (results.std()*100.0))