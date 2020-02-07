import numpy as np

name = np.asarray(['Alice', 'Bob', 'Cathy', 'Doug'])
age = np.asarray([25, 45, 37, 19])
weight = np.asarray([55.0, 85.5, 68.0, 61.5])

data1 = np.zeros(4, dtype=np.dtype('U10,i,f'))
# print(data1)

data2 = np.zeros(4, dtype = {'names': ('name', 'age', 'weight'),
                            'formats': ('U10', 'i', 'f')})
# print(data2)

data3 = np.zeros(4, dtype = np.dtype([
                                    ('name', 'U10'),
                                    ('age', 'i'),
                                    ('weight', 'f')
                                    ]))
# print(data3)

print(data2)
print(data2['name'])
data2['name'] = name
print(data2['name'])
print(data2)
print(data2)
print(data2['age'])
data2['age'] = age
print(data2['age'])
print(data2)
print(data2)
print(data2['weight'])
data2['weight'] = weight
print(data2['weight'])
print(data2)

data2[0] = ('Harry', 99, 536.5)
print(data2)
print(data2['name'])
print(name)


# print(data2['name'][0])
# print(data2[0]['name'])
# print(data2[0][0])
# print(data2.shape)


# print(data1.dtype)
# print(data2.dtype)
# print(data3.dtype)
