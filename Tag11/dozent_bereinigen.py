import pandas as pd

df_ab = pd.read_csv('state-abbrevs.csv')
df_ar = pd.read_csv('state-areas.csv')
df_po = pd.read_csv('state-population.csv')

df_ab_ar = pd.merge(df_ab, df_ar, how = 'outer')

# print(df_ab_ar.head())
# Puerto Rico hatte keinen Eintrag in state-abbrevs
df_ab_ar = df_ab_ar.fillna('PR')

# print(df_ab_ar.isna().any())

df_unclean = pd.merge(df_ab_ar, df_po,
                    left_on = 'abbreviation',
                    right_on= 'state/region',
                    how = 'outer')

# print(len(df_unclean))

# print(df_unclean.isna().any())

# # Bereinigen Spalte 'state'
# print(df_unclean[df_unclean['state'].isna()]['state/region'])
na_states = df_unclean['state'].isna()
df_unclean.loc[na_states, 'state'] = 'United States of America'


# # Bereinigen Spalte 'abbreviation'
# print(df_unclean[df_unclean['abbreviation'].isna()]['state/region'])
df_unclean.loc[na_states, 'abbreviation'] = 'USA'

# print(df_unclean.isna().any())

# # Bereinigen Spalte 'area (sq. mi)'

# print(df_unclean[df_unclean['area (sq. mi)'].isna()][['abbreviation', 'year', 'area (sq. mi)']])

area_usa = df_ar['area (sq. mi)'].sum()
df_unclean.loc[na_states, 'area (sq. mi)'] = area_usa


print(df_unclean.isna().any())

# print(df_unclean[df_unclean['population'].isna()][['abbreviation', 'year']])

# print(df_unclean[df_unclean['abbreviation'] == 'PR'][['year','ages', 'population']])

tot = (df_unclean['abbreviation'] == 'PR') & (df_unclean['ages'] == 'total')

u18 = (df_unclean['abbreviation'] == 'PR') & (df_unclean['ages'] == 'under18')

df_unclean.loc[tot, 'population'] = df_unclean.loc[tot, 'population'].fillna(method = 'bfill')

df_unclean.loc[u18, 'population'] = df_unclean.loc[u18, 'population'].fillna(method = 'bfill')

# print(df_unclean[df_unclean['abbreviation'] == 'PR'])

print(df_unclean.isna().any())

print(df_unclean.dtypes)

df_unclean['population'] = df_unclean['population'].astype(int)

print(df_unclean.dtypes)
