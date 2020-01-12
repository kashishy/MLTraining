import pandas as pd
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings("ignore")

# load Data
filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

X = array[:, 0:8]
Y = array[:, 8]

# feature extraction
pca = PCA(n_components=3)
fit = pca.fit(X)
resultX = pca.transform(X)

print("Result: ", resultX)
print("Experienced Variance: ", fit.explained_variance_ratio_)