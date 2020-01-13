# 4)- Cross Validation Classification Confusion Metrix ( Algorithm Performance Evaluation)
import pandas as pd
from sklearn.model_selection import train_test_split
# LogisticRegression for discrete output data
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import warnings

warnings.filterwarnings(action='ignore')

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

X = array[:, 0:8]
Y = array[:, 8]

# selecting size of test from historic data(here 33%)
test_data_size = 0.33
# for fixing output of randomise function, in selecting test and train data
# used for not contradiction of accuracy of the model
seed = 7

# for splitting historic data in train and test
# (this is done by train_test_split function by randomly selecting data)
# 67% train data(X_train, Y_train)
# 33% test data(X_test, Y_test)
# accuracy not be same all time because of randomly selecting train and test data from historic data
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_data_size)

# fixing random output ( training and testing data)(manually dividing data)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_data_size, random_state=seed)

# LogisticRegression is class(object of LogisticRegression)
model = LogisticRegression()

# Training model by train data
model.fit(X_train, Y_train)
predicted = model.predict(X_test)

# report of 33% data
matix = confusion_matrix(Y_test, predicted)
print(matix)
