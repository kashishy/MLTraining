import pandas as pd
from numpy import set_printoptions

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

import warnings
warnings.filterwarnings("ignore")

filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'plas', 'pres',
        'skin', 'test', 'mass',
        'pedi', 'age', 'class'
]
dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

X = array[:, 0:8]
Y = array[:, 8]

# feature extraction
test = SelectKBest(score_func=chi2, k=3)
fit = test.fit(X, Y)

# Summarize scores
set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(X)

# Summarize selected features
print("\n\n")
print(features[0:20, :])