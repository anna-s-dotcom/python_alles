import pandas as pd
import numpy as np

df = pd.read_csv('clean.csv')

print(df.head())

# print(df.agg([np.min, np.max], axis = 0))

# print(df['year'].agg([np.min, np.max]))

print(df.agg({'year': [np.min, np.max], 'population': np.mean}))
