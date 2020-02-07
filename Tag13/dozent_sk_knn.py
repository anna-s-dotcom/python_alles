from sklearn import metrics
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 5)
df = pd.read_csv('DataSet.txt', delimiter = '\t')
features = df[['Quadratmeter', 'Wandhoehe', 'IA_Ratio']].copy()
target = df['Kategorie']

X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    test_size = 0.25)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# gibt die genauigkeit in prozent an
print(metrics.accuracy_score(y_test, y_pred))

# crosstab ohne funktionsparameter erstellt eine confusion matrix
# als DataFrame
print(pd.crosstab(y_test, y_pred,
                    rownames = ['True'],
                    colnames = ['Pred']))

# erstellt confusion matrix als numpy ndarray
print(metrics.confusion_matrix(y_test, y_pred))

# 7	170.00	2.80	39.00	Wohnung
import numpy as np
# print(knn.predict(np.array([170, 2.80, 39]).reshape(-1, 3)))
print(knn.predict([[25, 2.80, 25]]))
