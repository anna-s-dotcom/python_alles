import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('autos.csv', na_values = '?')[['highway-mpg', 'price']]

df = df.dropna()

X_train, X_test, y_train, y_test = train_test_split(
                        df[['highway-mpg']],
                        df['price'],
                        test_size = 0.2)

# print(X_train.head())

degree = 3

quad = PolynomialFeatures(degree = degree)

X_train_quad = quad.fit_transform(X_train)
X_test_quad = quad.fit_transform(X_test)

# print(X_train_quad)

nr = LinearRegression()

nr.fit(X_train_quad, y_train)
X_sort = X_train.sort_values(by = 'highway-mpg')

X_sort_quad = quad.fit_transform(X_sort)
y_pred = nr.predict(X_sort_quad)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X_train['highway-mpg'], y_train, color = 'b')
ax.scatter(X_test['highway-mpg'], y_test, color = 'g')
ax.plot(X_sort['highway-mpg'], y_pred, color = 'red')
ax.set_xlabel('highway-mpg')
ax.set_ylabel('price')
plt.show()
