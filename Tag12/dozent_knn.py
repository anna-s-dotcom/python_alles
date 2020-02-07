import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

############# Daten betrachten
df = pd.read_csv('DataSet.txt', delimiter = '\t')

# print(df.head())
# print(df['Kategorie'].unique())

# für matplotlib zum Zuordnen der Farben für die Kategorien
col_dic = {'Buero':'y', 'Wohnung': 'r', 'Haus': 'b'}
df['Color'] = df['Kategorie'].map(col_dic)
# print(df.head())

features = df[['Quadratmeter', 'Wandhoehe', 'IA_Ratio']].copy()
target = df['Kategorie'].copy()

def plotdata(df, k1, k2):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(df[k1],
                df[k2],
                marker = 'o',
                s = 7,
                color = df['Color'])
    ax.set_xlabel(k1)
    ax.set_ylabel(k2)
    ax.set_xlim(left = 0)
    ax.set_ylim(bottom = 0)
    plt.show()

    ########### Normalisierung
    # from sklearn import preprocessing

    scaler = preprocessing.MinMaxScaler()
    features = scaler.fit_transform(features)

    features = pd.Dataframe(features,
                    columns = ['Quadratmeter', 'Wandhoehe', 'IA_Ratio'])


# plotdata(df, 'Quadratmeter', 'Wandhoehe')
# plotdata(df, 'Quadratmeter', 'IA_Ratio')
# plotdata(df, 'IA_Ratio', 'Wandhoehe')

# from mpl_toolkits.mplot3d import Axes3D

# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')
# ax.scatter(df['Quadratmeter'],
#             df['Wandhoehe'],
#             df['IA_Ratio'],
#             color = df['Color'])
# ax.set_xlabel('Quadratmeter')
# ax.set_ylabel('Wandhoehe')
# ax.set_zlabel('IA_Ratio')
# ax.set_xlim(left = 0)
# ax.set_ylim(bottom = 0)
# ax.set_zlim(bottom = 0)
# plt.show()
########## Berechnung der Distanzen, Ausgabe der vorhergesagten werte
# from sklearn.model_selection import train_test_split


# aufspalten des Datensatzes in trainings und test Daten
X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    test_size = 0.25)
# print(X_train)
# print()
# print(y_train)
print(features.agg([np.min, np.max]))


k = 5
y_pred = []

# for schleife über X_test, val = jedes element aus X_test
#for i,val in X_test.iloc[:1,]

for i, val in X_test.iterrows():

    # differenz von val zu jedem datenpunkt in X_train
    X_temp = X_train - val

    # quadrieren der differenzen
    X_temp = X_temp.applymap(lambda x: x*x)

    # bilde summe der quadrate (auf dataframe)
    X_temp = X_temp.apply(np.sum, axis = 1)

    # wurzel aus der summe der quadrate (auf series)
    X_temp = X_temp.apply(np.sqrt)

    # nach dem geringsten abstand sortieren
    neigh = X_temp.sort_values()[:k]
    # die zugehörigen Kategorien geholt
    y_temp = y_train.loc[neigh.index]
    # ermitteln der maximalen übereinstimmung mit den nachbarn
    result = {}
    for kategorie in y_temp:
        result[kategorie] = result.get(kategorie, 0) + 1
    pred_max = max(result, key=result.get)
    # vorhergesagtes y an y_pred hängen
    y_pred.append(pred_max)
#in vergleichbare form bringen
y_pred = np.array(y_pred)
y_testarr = y_test.values

print(y_pred, y_testarr[:1], y_pred == y_testarr[:1])

print('Anzahl Testdaten:', len(y_pred))
print('Anzahl Fehler:', np.sum(~(y_pred == y_testarr)))


from mpl_toolkits.mtplot3d import Axes3D
print(lr.predict(X_train))
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(features['horsepower'],
            features['city-mpg'],
            target)
ax.plot(X_train, , color = 'r')

ax.plot_surface(features['horsepower'],
        features['city-mpg'],
        lr.predict(features),
        color = 'r')
plt.show()
