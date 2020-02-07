# Füge die Datensätze aus jena1.csv und jena2.csv sinnvoll zusammen.
# (Optional: Speichere den vollständigen Datensatz als neue csv Datei.)

# # set a maximum of shown columns with print
# pd.set_option("display.max_columns", 999)

import pandas as pd

df1 = pd.read_csv('jena1.csv', index_col = 0)
df2 = pd.read_csv('jena2.csv', index_col = 0)

print((df1.columns == df2.columns).all())

# dfc = pd.concat([df1, df2])
# dfc = dfc.sort_index()
# print(dfc)

dfc = df1.append(df2)
dfc = dfc.sort_index()
print(dfc)
