# import pandas as pd
#
# df1 = pd.DataFrame(columns = ['worker', 'salary'])
# df1['worker'] = ['Alice', 'Joe', 'Jim']
# df1['salary'] = [5000, 1500, 2500]
#
# df2 = pd.DataFrame(columns = ['dept', 'worker'])
# df2['dept'] = ['PR', 'PR', 'DEV']
# df2['worker'] = ['Joe', 'Alice', 'Jane']
#
# print(df1)
# print()
# print(df2)
#
# dfm = pd.merge(df1, df2, on = 'worker', how = 'right')
# print()
# print(dfm)

# import pandas as pd
#
# df1 = pd.DataFrame(columns = ['worker', 'salary'])
# df1['worker'] = ['Alice', 'Joe', 'Jim']
# df1['salary'] = [5000, 1500, 2500]
#
# df2 = pd.DataFrame(columns = ['dept', 'employee'])
# df2['dept'] = ['PR', 'PR', 'DEV']
# df2['employee'] = ['Joe', 'Alice', 'Jane']
#
# print(df1)
# print()
# print(df2)
#
# dfm = pd.merge(df1, df2, left_on = 'worker', right_on = 'employee').drop('employee', axis=1)
# print()
# print(dfm)

import pandas as pd

df1 = pd.DataFrame(columns = ['worker', 'salary', 'id'])
df1['worker'] = ['Alice', 'Joe', 'Jim']
df1['salary'] = [5000, 1500, 2500]
df1['id'] = [564564, 564654, 548654]

df2 = pd.DataFrame(columns = ['dept', 'employee', 'id'])
df2['dept'] = ['PR', 'PR', 'DEV']
df2['employee'] = ['Joe', 'Alice', 'Jane']
df2['id'] = ['kl34l3', 'klöj545', 'j4546ljk']

print(df1)
print()
print(df2)

dfm = pd.merge(df1, df2,
            left_on = 'worker',
            right_on = 'employee',
            how = 'right',
            suffixes = ('-first', '-second'))
print()
print(dfm)
