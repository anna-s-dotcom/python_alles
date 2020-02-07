import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np

# def logistic(x):
#     return 1/(1+ np.exp(-x))
#
# x = np.arange(-7, 7, 0.05)
#
# plt.plot(x, logistic(x))
# plt.title('Logistische Funktion')
# plt.show()

data = load_iris()

features = data.data
target = data.target

scaler = MinMaxScaler()
features = scaler.fit_transform(features)

X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    test_size = 0.1 )

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(data.data[:,2], data.data[:, 3], c = data.target)
# ax.set_xlabel('petal length')
# ax.set_ylabel('petal width')
# plt.show()

logr = LogisticRegression(max_iter = 150)
logr.fit(X_train, y_train)

print('Genauigkeit:', accuracy_score(y_test, logr.predict(X_test)))

print('Probs für erste Test:', logr.predict_proba(X_test[:1]))
