#3)-Evaluate using Leave One Out Cross Validation

from pandas import read_csv
# selecting data items for training and testing
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings(action='ignore')

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = read_csv(filename, names=hnames)
array = dataframe.values

X = array[:, 0:8]
Y = array[:, 8]

# create object of LeaveOneOut
loocv = LeaveOneOut()

# create object of LogisticRegression
model = LogisticRegression()

# all same as KFold only cv value changes
results = cross_val_score(model, X, Y, cv=loocv)

# print all the accuracies(i.e. n accuracies),
# status values(i.e. predicted output matches with required output)
# 0 incorrect output
# 1 correct output
print("results : ", results)

# size of the result will be n, number of times machine works
print("results.size : ", results.size)

# correct number of outputs, number of times machine work correctly
print("Sum of Positive Results: %i " % (results.sum()))

# central accuracy of model
print("Accuracy = %.2f %%" % (results.sum()*100/results.size))