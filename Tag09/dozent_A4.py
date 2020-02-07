# # Erstelle mit Hilfe der Dateien 'state-abbrevs.csv', 'state-population.csv' und 'state-areas.csv' ein DataFrame welches die folgenden Spalten hat:
#
#
# state,  area (sq. mi),    ages,  year,   population

import pandas as pd

df_ab = pd.read_csv('state-abbrevs.csv')
df_ar = pd.read_csv('state-areas.csv')
df_po = pd.read_csv('state-population.csv')

df_ab_ar = pd.merge(df_ab, df_ar, how = 'outer')

print(df_ab_ar.head())
df_ab_ar = df_ab_ar.fillna('PR')

# print(df_ab_ar.isna().any())

df_unclean = pd.merge(df_ab_ar, df_po,
                    left_on = 'abbreviation',
                    right_on= 'state/region',
                    how = 'outer')

# print(len(df_unclean))

print(df_unclean.isna().any())

print(df_unclean['abbreviation'].nunique())
print(df_unclean['state/region'].nunique())
print(df_unclean[df_unclean.isna()['abbreviation']][['state/region']])
