#4)- Reapeated Random Test-Train Splits
# Evaluation using Shuffle Split Cross Validation
import pandas as pd
# for splitting train and test data
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings(action='ignore')

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

X = array[:, 0:8]
Y = array[:, 8]

# data for train and test
# 67% train and 33% test data
test_data_size = 0.33

# number of times splitting and testing will done, to increase the accuracy(average accuracy)
no_of_repetitions = 4

# creating object of ShuffleSplit
shufflesplit = ShuffleSplit(n_splits=no_of_repetitions, test_size=test_data_size)

# creating object of LogisticRegression
model = LogisticRegression()

# accuracy of the model, testing and training model shufflesplit times
results = cross_val_score(model, X, Y, cv=shufflesplit)

# printing accuracy for each iteration
print(results)

# average accuracy of the model
print("Accuracy: %.3f " % (results.mean()*100.0))

print("Std.Deviation= %.3f" % (results.std()*100.0))