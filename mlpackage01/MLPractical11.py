from matplotlib import pyplot as plt
import pandas

filename = "indians-diabetes.data.csv"

headingnames = ['preg', 'plas', 'pres', 'skin', 'test',
                'mass', 'pedi', 'age', 'class']

dataframe = pandas.read_csv(filename, names=headingnames)

#box in each graph represent middle 50% data i.e. 25% to 75%
#line in each box represent 50 percentile
#circles in graph represent to much deviated data
dataframe.head()
dataframe.plot(kind='box', subplots=True, layout=(3, 3), sharex=False, sharey=False)
plt.show()