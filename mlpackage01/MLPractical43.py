# Feature Extraction with Recursive Feature Elimination (RFE)
import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import warnings

warnings.filterwarnings("ignore")

# load Data
filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

X = array[:, 0:8]
Y = array[:, 8]

# feature extraction
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)
result = fit.transform(X)

print("Num Features: ", fit.n_features_)
print("Selected Features: ", fit.support_)
print("Feature banking: ", fit.ranking_)
print("\n\n\n", result[:30, :])
