import pandas

filename = "indians-diabetes.data.csv"
hnames = ['preg','plas','pres',
          'skin','test','mass',
          'pedi','age','class']

dataframe = pandas.read_csv(filename, names=hnames)

#for selecting number of rows to print
print(dataframe.head(10))
print("-*-"*20)

#dimension of dataframe
print("dataframe.shape : ", dataframe.shape)
print("-#-"*20)

#data type for each attribute
print(dataframe.dtypes)
print("-#-"*20)

#descriptive statistics, for increasing display area, precision set number of spaces between two set
pandas.set_option('display.width',1000)
pandas.set_option('precision',2)

print("description = \n", dataframe.describe())

print("-*-"*20)

#class distribution(classification only)
print()
#group by values of the feature
class_counts = dataframe.groupby('class').size()

print(class_counts)
print("-#-"*20)