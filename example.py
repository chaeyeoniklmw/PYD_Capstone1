import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df=pd.read_csv('wine.data', header=None)
data= df.values  #change into numpy array
x=data[:,1:] #remove first column


estimator= KMeans(n_clusters=3).fit(X)
y= estimator.predict(X)

df_g= pd.DataFrame(X)
df_g['label']= pd.Series(y)

sns.set(style='ticks', color_codes=True)
sns.pairplot(df_g, hue='label', markers=['o','s','D'])

plt.show()
