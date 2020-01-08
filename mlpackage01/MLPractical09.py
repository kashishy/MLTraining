import matplotlib.pyplot as plt
import pandas

filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'plas','pres','skin',
          'test','mass','pedi','age','class']

df = pandas.read_csv(filename, names=hnames)

print(df)

#hist() create histogram
df.hist()

#show() shows created graph
plt.show()