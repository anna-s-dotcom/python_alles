# Lies state-abbrevs.csv und state-areas.csv als DataFrame ein.
# Nutze je die erste Spalte (state) als Index.
#
# Erstelle ein drittes DataFrame, welches die Staaten als Index und die Spalten, Abkürzung und Gebiet hat. (abbreviation und area (sq. mi))

#             abbreviation     area (sq. mi)
#
# Alabama     AL              52423
import pandas as pd

df1 = pd.read_csv('state-abbrevs.csv').set_index('state')
df2 = pd.read_csv('state-areas.csv', index_col='state')

print(df1.head())
print()
print(df2.head())
print()
dfc = pd.concat([df1, df2], axis=1, sort=False)
print(dfc.head())
print()
print(dfc.isna().any())
print()
print(dfc[dfc['abbreviation'].isna()])
# mit warnung:
# dfc['abbreviation']['Puerto Rico'] = 'PR'

# dfc.loc['Puerto Rico', 'abbreviation'] = 'PR'
# print()
dfc.fillna('PR', inplace = True)
print()
# print(dfc.loc['Puerto Rico']['abbreviation'])
# print()
# print(dfc.loc['Puerto Rico'])
print()
# print(dfc.tail())
print(dfc.isna().any())
