#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import pandas

filename = 'indians-diabetes.data.csv'

headingnames = ['preg', 'plas','pres','skin',
          'test','mass','pedi','age','class']

dataframe = pandas.read_csv(filename, names=headingnames)

#univariate density plot
#sharex=False to not share common x-axis between subplots
#layout divides the area of the display
#subplots tells either to draw seperate graphs for each feature or not
dataframe.plot(kind='density', subplots=True, layout=(3,3), sharex=True)
plt.show()