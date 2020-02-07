import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('autos.csv',
                na_values = '?',
                thousands = None,
                decimal = '.')

# print(df.head())
# print(df.columns)

feature_cols = ['horsepower', 'city-mpg']

target_col = 'price'

df = df[['horsepower', 'peak-rpm', 'city-mpg','highway-mpg', 'price']]

# print(df.isna().any())
# print(df.isna().sum())

df = df.dropna()

# print(df.isna().any())
# print(df.isna().sum())

features = df[feature_cols].copy()
target = df[target_col].copy()

# pd.plotting.scatter_matrix(
#                         df,
#                         c = target)
# plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    test_size = 0.2)

lr = LinearRegression()
lr.fit(X_train, y_train)

print(f"Intercept:", lr.intercept_)
print(f'Anstieg:', lr.coef_)
print(f"Unsere Vorhersage: y = {lr.coef_[0]:.2f}*x + {lr.intercept_:.2f}")
print(f'R2 Score', lr.score(X_train, y_train))
print(f'R2 Score', lr.score(X_test, y_test))
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(X_train, y_train)
# ax.plot(X_train, lr.predict(X_train), color = 'r')
# plt.show()

from mpl_toolkits.mplot3d import Axes3D

# 'horsepower', 'city-mpg', 'price'
print(lr.predict(X_train))

# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')
# ax.scatter(features['horsepower'],
#             features['city-mpg'],
#             target)
# ax.plot_surface(features['horsepower'],
#         features['city-mpg'],
#         lr.predict(features),
#         color = 'r')
# plt.show()
