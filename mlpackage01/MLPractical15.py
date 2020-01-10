import pandas as pd
# for deciding number of digits after decimal
from numpy import set_printoptions
# start by capital letter is class of code (here MinMaxScaler)
from sklearn.preprocessing import MinMaxScaler

# to load code in a file we have to use round brackets after name
filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv("indians-diabetes.data.csv", names=hnames)

# data without headings
array = dataframe.values
# Separate array into input and output components
X = array[:, 0:8]      # [row, cols] (slicing) (here all rows and frist 8 columns, 8 is ending condition excluding (all places this except 1))
Y = array[:, 8]        # all rows and 9th column
# MinMaxScaler used for rescaling of data(here all values rescaled between 1 to 5)
scaler = MinMaxScaler(feature_range=(1, 5))

# first Method
rescaledX = scaler.fit_transform(X)

# Second Method
scaler = scaler.fit(X)
rescaledX = scaler.transform(X)

# Summarize transformed data, two places digits after decimal
set_printoptions(precision=2)

# print data of first 30 rows (0 to 29 indexed rows)
print(rescaledX[:30, :])