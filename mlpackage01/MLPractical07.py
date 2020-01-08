import warnings
warnings.filterwarnings(action="ignore")

import pandas
import urllib.request

#manually added column headings
hnames = ['sepal-length','sepal-width',
          'petal-length','petal-width',
          'class']

#here frist four features represent input and class represent output
#data of Iris flower
web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")

#web_path and metadata for the data
dataframe = pandas.read_csv(web_path, names=hnames)

print(dataframe.shape)

print(dataframe)

print(dataframe.columns)

print("\n\n\n")
print(dataframe.describe())

print("\n\n\n")
print(dataframe.dtypes)

print("\n\n\n")
print(dataframe.describe(include="all"))