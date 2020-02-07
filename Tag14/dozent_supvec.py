import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.svm import SVC

data = load_iris()

# print(data.feature_names)
# > ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

df = pd.DataFrame(data.data[:, 2:], columns = data.feature_names[2:])
df['iris'] = data.target

# print(df.head())

features = df[['petal length (cm)', 'petal width (cm)']]
target = df['iris']

svm = SVC(kernel='linear')
svm.fit(features, target)

xx, yy = np.meshgrid(np.arange(features['petal length (cm)'].min()-1,
                    features['petal length (cm)'].max()+1, 0.05),

                    np.arange(features['petal width (cm)'].min()-1,
                                        features['petal width (cm)'].max()+1, 0.05)
                    )

Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.contourf(xx, yy, Z, cmap = plt.cm.summer)
ax.scatter(features['petal length (cm)'],
            features['petal width (cm)'],
            c = target,
            cmap = plt.cm.summer,
            edgecolors = 'k')
plt.show()
