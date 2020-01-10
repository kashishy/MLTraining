#to avoid warning messages due to version conflict of dependent libraries
#warning messages print along with output of the application
import warnings
warnings.filterwarnings(action="ignore")

#Correlation Matrix Plot
from matplotlib import pyplot as plt
import pandas as pd
import numpy

#this is important with web based editors, decide size of the display
pd.set_option('display.width',1000)
#for setting number of columns will show in output
pd.set_option('display.max_column', 9)

hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv('indians-diabetes.data.csv', names=hnames)

#calculate correlation of every column with all column
correlations = dataframe.corr()

print(correlations)

#plot correlation matrix
#pop window from this(empty graph)
fig = plt.figure()

#following will add matrix and side bar in entire area
#in subplot numbering start with 1
#code 111
subFig = fig.add_subplot(111)

#to pass data to figure that has to be printed
#vmin and vmax decide range, as correlation varies from -1 to 1
cax = subFig.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)

ticks = numpy.arange(0, 9)  #it will generate values from 0...8
subFig.set_xticks(ticks) #for adding ticks on x-axis
subFig.set_yticks(ticks) #for adding ticks on y-axis
subFig.set_xticklabels(hnames) #for adding names to ticks on x-axis
subFig.set_yticklabels(hnames) #for adding names to ticks on y-axis

plt.show()