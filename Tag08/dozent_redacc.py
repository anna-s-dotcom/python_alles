import numpy as np

########## reduce
#
# arr = np.arange(1, 17).reshape(2, 4, 2)
#
# print(arr)
# print(arr.shape)
# print()
#
# print(np.add.reduce(arr, axis = 0))
# print(np.add.reduce(arr, axis = 0).shape)
# print()
#
# print(np.add.reduce(arr, axis = 1))
# print(np.add.reduce(arr, axis = 1).shape)
# print()
#
# print(np.add.reduce(arr, axis = 2))
# print(np.add.reduce(arr, axis = 2).shape)
# print()
#
# print(np.add.reduce(arr, axis = 1, keepdims=True))
# print(np.add.reduce(arr, axis = 1, keepdims=True).shape)

######### accumulate

arr = np.arange(1, 7).reshape(2, 3)

print(arr)
print(arr.shape)
print()

print(np.add.accumulate(arr, axis = 0))
print(np.add.accumulate(arr, axis = 0).shape)
print()

print(np.add.accumulate(arr, axis = 1))
print(np.add.accumulate(arr, axis = 1).shape)
print()
