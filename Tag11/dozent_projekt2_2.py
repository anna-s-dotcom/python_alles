import pandas as pd

with open('EU2014_BE_EndgErg_Wahlbezirke.csv') as file:
    print(file)
    codec = file.encoding

cols14 = ['WbezirksName', 'CDU', 'SPD', 'GRÜNE']
cols19 = ['Adresse', 'CDU', 'SPD', 'GRÜNE']

df2014 = pd.read_csv('EU2014_BE_EndgErg_Wahlbezirke.csv',
                    encoding = codec,
                    delimiter = ';')[cols14].dropna(thresh = 4)

df2019 = pd.read_csv('EU2019_BE_EndgErg_Wahlbezirke.csv',
                    encoding = codec,
                    delimiter = ';')[cols19].dropna(thresh = 4)


# print(df2014)
# print()
# print(df2019)

dfm = pd.merge(df2014, df2019,
                left_on = 'WbezirksName',
                right_on = 'Adresse',
                suffixes = ('-2014', '-2019'),
                how = 'inner').drop('WbezirksName', axis = 1)

# print()
# print(dfm)
# 1
dfm['diff-CDU'] = dfm['CDU-2019'] - dfm['CDU-2014']
dfm['diff-SPD'] = dfm['SPD-2019'] - dfm['SPD-2014']
dfm['diff-GRÜNE'] = dfm['GRÜNE-2019'] - dfm['GRÜNE-2014']

print(dfm)
# 2
import numpy as np

cdu = np.nansum(dfm['diff-CDU'])
spd = np.nansum(dfm['diff-SPD'])
gruene = np.nansum(dfm['diff-GRÜNE'])

ges = cdu + spd + gruene

print('Gesamtdifferenz 2019 - 2014:', ges)

# 3

ges2014 = np.nansum(dfm['CDU-2014']) + np.nansum(dfm['SPD-2014']) + np.nansum(dfm['GRÜNE-2014'])

ges2019 = np.nansum(dfm['CDU-2019']) + np.nansum(dfm['SPD-2019']) + np.nansum(dfm['GRÜNE-2019'])
