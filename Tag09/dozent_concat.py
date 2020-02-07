import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(9).reshape(3, 3), columns = ['B', 'A', 'C'], index = [2, 3, 4])

df2 = pd.DataFrame(np.arange(9, 15).reshape(3, 2), columns = ['C', 'D'])

print(df1)
print()
print(df2)
print()

dfc1 = pd.concat([df1, df2], sort=False, axis = 0)
# print(dfc1)
# dfc2 = pd.concat([df1, df2], sort=True, axis = 0)
# print(dfc2)
print()
dfc3 = pd.concat([df1, df2], sort=False, axis = 1, ignore_index=True)
# print(dfc3)
print()
dfc4 = pd.concat([df1, df2], sort=False, axis = 1, ignore_index=False)
print(dfc4)
print(dfc4.set_index('B'))
