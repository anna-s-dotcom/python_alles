# Nutze pandas merge um aus den beiden Dateien 'state-abbrevs.csv' und 'state-areas.csv' ein verbundenes DataFrame zu erstellen.

import pandas as pd

df1 = pd.read_csv('state-abbrevs.csv')
df2 = pd.read_csv('state-areas.csv')

print(df1)


dfm = pd.merge(df1, df2, how = 'outer')

print(dfm)

print(dfm.isna().any())
print(dfm.isna()['abbreviation'])
print(dfm[ dfm.isna()['abbreviation'] ])
dfm_clean = dfm.fillna('PR')
