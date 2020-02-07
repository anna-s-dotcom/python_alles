# from sklearn.datasets import load_iris
# import matplotlib.pyplot as plt
#
# data = load_iris()

# print(data.DESCR)
# print(data.target_names)
# print(data.feature_names)
# print(data.target)
# print()
# print(data.data)
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(data.data[:, 1],
#             data.data[:,3],
#             c = data.target)
# ax.set_xlabel(data.feature_names[1])
# ax.set_ylabel(data.feature_names[3])
# plt.show()

# Aufgabe: Führe auf den Iris Datensatz von sklearn einen KNN Algorithmus aus und versuche für 15 Werte eine Vorhersage zu machen.
# Wie genau ist der Algorithmus.

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

data = load_iris()

scaler = MinMaxScaler()
data_n = scaler.fit_transform(data.data)

X_train, X_test, y_train, y_test = train_test_split(data_n,
                                                    data.target,
                                                    test_size = 0.1)
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print(metrics.accuracy_score(y_test, y_pred))
print(metrics.confusion_matrix(y_test, y_pred))

print(help(scaler))
