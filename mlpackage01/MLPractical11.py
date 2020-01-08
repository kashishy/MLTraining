from matplotlib import pyplot as plt
import pandas

filename = "indians-diabetes.data.csv"

headingnames = ['preg','plas','pres','skin','test',
                'mass','pedi','age','class']

dataframe = pandas.read_csv(filename, names=headingnames)

dataframe.plot(kind='box', subplots=True, layout=(3,3), sharex=False)

plt.show()