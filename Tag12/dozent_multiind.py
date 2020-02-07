import pandas as pd

df = pd.read_csv('clean.csv')

# print(df)

df = df.set_index(['year', 'ages'])

# print(df.index)

# # gibt alle Daten im Jahr 2012
# print(df.loc[2012][['state', 'population']])

# # Alle totalen populationen im Jahr 2012 (ohne under18)
print(df.loc[(2012, 'total')]['state'] == 'Alabama')

# gibt Indexobjekt für index level == 0 (Jahre)
print(df.index.get_level_values(0))

# # gibt für alle Jahre die totalen populationen
# print(df.loc[(df.index.get_level_values(0), 'total'), :][['state', 'population']])
# print(df.loc[(df.index.get_level_values(0), 'total'), ['state', 'population']])

# # dem vorhandenen Index einen weiteren hinzu
df = df.set_index('state', append = True)
print(df)
