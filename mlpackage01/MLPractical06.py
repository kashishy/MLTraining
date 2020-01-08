#Load CSV using pandas

import pandas

filename = 'indians-diabetes.data.csv'

#adding feature names manually to all features
hnames = ['preg','plas','pres',
          'skin','test','mass',
          'pedi','age','class']

dataframe = pandas.read_csv(filename, names=hnames)
#dataframe = pandas.read_csv(filename)#this fro checking heading to be frist rwo if not manually added

print("pandas Data : ", dataframe.shape)

print(dataframe)

print("\n\n")

#type of the dataframe
print(type(dataframe))

a = 5
print(type(a))

a = 12.5
print(type(a))

a = 'iitk'
print(type(a))

#
a = [1,2,3,4]
print(type(a))

#datatypes of features inside the dataframe, dtypes give this(specific for pandas dataframe)
print(dataframe.dtypes)