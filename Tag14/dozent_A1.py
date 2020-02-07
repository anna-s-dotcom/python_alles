from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import metrics

# mögliche methoden: .data , .target .feature_names .DESCR
# nicht .target_names   -> warum?

data = fetch_california_housing()

# print(data.DESCR)
# print(data.feature_names)

# ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

# Skalieren der Daten zwischen 0-1: Normalisierung
scaler = MinMaxScaler()
features_np = scaler.fit_transform(data.data)

# Erstellen eines DataFrames aus den Features und dem Target
df = pd.DataFrame(features_np, columns = data.feature_names)
df['target']  = data.target

cols = ['MedInc', 'AveRooms']

# features = df[['MedInc', 'AveRooms']]
# Betrachte nur die Features in der Liste cols
features = df[cols]
target = df['target']

# Scatter Matrix:
# pd.plotting.scatter_matrix(df[['MedInc', 'AveRooms', 'target']], c = data.target)
# plt.show()

# Daten in Trainings- und Testdaten spalten
X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    test_size = 0.25)

######### Lineare Regression
# from sklearn import metrics
lr = LinearRegression()
lr.fit(X_train, y_train)

print('Trainingsdaten R²:', lr.score(X_train, y_train))
print('metrics r2_score:', metrics.r2_score(y_train,
                                            lr.predict(X_train)))
print('Testdaten R²:', lr.score(X_test, y_test))
print('metrics r2_score:', metrics.r2_score(y_test,
                                            lr.predict(X_test)))


######### Polinomiale Regression

poli = PolynomialFeatures(degree = 5)
X_train_poli = poli.fit_transform(X_train)
X_test_poli = poli.fit_transform(X_test)

pr = LinearRegression()
pr.fit(X_train_poli, y_train)

print()
print('Polinomiale Regression')
print('Traingscore R²:', pr.score(X_train_poli, y_train))
print('Testscore R²:', pr.score(X_test_poli, y_test))
