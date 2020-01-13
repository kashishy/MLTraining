# Save and Load Model Using Joblib
import pandas as pd
from sklearn.model_selection import train_test_split
# LogisticRegression for discrete output data
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
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
seed = 7

# fixing random output ( training and testing data)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_data_size, random_state=seed)

# LogisticRegression is class(object of LogisticRegression)
model = LogisticRegression()

# Training model by train data ( fit the model on 67% data)
model.fit(X_train, Y_train)

# testing model against test data(result will store percentage of correct output)
result = model.score(X_test, Y_test)

# save the model to disk
filename = 'finalized_model.sav'
# b is for encrypted file(binary)
joblib.dump(model, open(filename, 'wb'))

print("Model dumped successfully into a file by Joblib"
      "....\n...\n...\n...")

print("--------------------------\n\n\n")
print("some time later... ")
print("\n\n\n--------------------------")

# load the model from disk
loaded_model = joblib.load(open(filename, 'rb'))
print("Model loaded successfully from file by Joblib")

result = loaded_model.score(X_test, Y_test)
print("Accuracy Result : ", result)