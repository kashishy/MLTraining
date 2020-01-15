# Pipeline
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
import warnings

warnings.filterwarnings(action='ignore')

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

X = array[:, 0:8]
Y = array[:, 8]

estimators = []
estimators.append(("standardize", StandardScaler()))
estimators.append(("lda", LinearDiscriminantAnalysis())) # we can use LogisticRegression instead of LDA
pipelineModel = Pipeline(estimators)
print(pipelineModel)

kfold = KFold(n_splits=10, random_state=7)
results = cross_val_score(pipelineModel, X, Y, cv=kfold)

print("Accuracy: %.2f %%" % (results.mean()*100))