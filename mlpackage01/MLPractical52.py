# 3)- Cross Validation Classification Area under AUC curve ( Algorithm Performance Evaluation)
import pandas as pd
from sklearn.model_selection import KFold
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

# for selecting number of groups in historic data, create object of KFold
kfold = KFold(n_splits=10)

# create object of LogisticRegression
model = LogisticRegression()

# deciding type of method used for accuracy calculation( here Area under ROC curve)
scoringMethod = 'roc_auc'

# scoring method decides type of accuracy calculation method, default method is classification accuracy
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoringMethod)

print("AUC: %.3f (%.3f)" % (results.mean()*100, results.std()*100))