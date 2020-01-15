# Spot checking is used to check which model is best for the given data
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import warnings
warnings.filterwarnings(action='ignore')

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

X = array[:, 0:8]
Y = array[:, 8]

kfold = KFold(n_splits=10)


# 1: Spot checking for Logistic Regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=kfold)
print("Validation Score for LogisticRegression : ", results.mean())


# 2: Spot Checking for Linear Discriminant Analysis(LDA)
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis()
results = cross_val_score(model, X, Y, cv=kfold)
print("Validation Score for Linear Discriminant Analysis : ", results.mean())


# 3: Spot Checking for k-Nearest Neighbors(kNN)
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()
results = cross_val_score(model, X, Y, cv=kfold)
print("Validation Score for KNN : ", results.mean())


# 4: Spot Checking for Gaussian Naive Bayes
# Naive Bayes calculation the probability of each class and
# the conditional probability of each class given each input value
# These probabilities are estimated for new data and
# multiplied together assuming that they are all
# independent ( a simple or naive assumption)
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
results = cross_val_score(model, X, Y, cv=kfold)
print("Validation Score for GaussianNB : ", results.mean())


# 5: Spot Checking for Classification And Regression Tress
# (CART or just decision tress)
# ________________________________________________________
# CART or just decision trees construct a binary tree
# from the training data
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
results = cross_val_score(model, X, Y, cv=kfold)
print("Validation Score for CART Decision Tree : ", results.mean())


# 6: Spot Checking for Support Vector Machines(SVM)
# ------------------------------------------------
# SVM seek a line that best separates two classes
# Those data instances that are closest to the line that
# best separates the classes are called support vectors
# and influence where the line is placed
from sklearn.svm import SVC
model = SVC()
results = cross_val_score(model, X, Y, cv=kfold)
print("Validation Score for SVM : ", results.mean())