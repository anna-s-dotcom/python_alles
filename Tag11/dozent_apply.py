import pandas as pd
import numpy as np

df2019 = pd.read_csv('EU2019_BE_EndgErg_Wahlbezirke.csv',
                    encoding = 'cp1252', delimiter = ';')

df2019 = df2019[['Wähler', 'CDU', 'SPD', 'GRÜNE']]
df2019 = df2019.dropna(how = 'all')

print(df2019.dtypes)

# nums = df2019['Wähler'].str.isnumeric()
# print(df2019[~nums])

# print('564564'.isnumeric())
df2019['Wähler'] = df2019['Wähler'].str.replace(' ', '')

nums = df2019['Wähler'].str.isnumeric()
print(df2019[~nums])

# df2019['Wähler'] = df2019['Wähler'].apply(int)
df2019['Wähler'] = df2019.apply({'Wähler' : int})

df2019[['CDU', 'SPD', 'GRÜNE']] = df2019[['CDU', 'SPD', 'GRÜNE']].applymap(int)

print(df2019.dtypes)


#########
# Aufgabe
#########

# Erstelle eine neue Spalte im df2019 Sie soll für jede Zeile die Summe aus 'CDU', 'SPD' und 'GRÜNE' beinhalten.
 # Bonus Gib die Gesamtsummen aller Spalten einzeln aus.

df2019['Summe'] = df2019[['CDU', 'SPD', 'GRÜNE']].apply(np.sum, axis = 1)

df2019.loc[len(df2019)] = df2019.apply(np.sum, axis = 0)

print(df2019)
print(df2019.dtypes)
