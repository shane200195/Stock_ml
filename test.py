import pandas
from sklearn.decomposition import PCA

df = pandas.read_csv('sp500.csv')
df = df.set_index('date')
#seperating the targets

print(df.columns)
#my_pca = PCA(n_components=2)
#my_pca.fit



