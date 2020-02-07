# Erstelle ein 3x5 Array mit zufälligen Integern zwischen 1 und 100.
#
# 1) Subtrahiere alle Zeilen voneinander.
# 2) Subtrahiere alle Spalten voneinander.
# 3) Gib die Negierten Ergebnisse aus.
import numpy as np


arr = np.random.randint(1, 101, (3, 5))
# arr = np.random.randint(1, 101, 15).reshape(3, 5)
print(arr)

subRows = np.subtract.reduce(arr, keepdims=True)
print(subRows)
print(subRows.shape)
print()
subCols = np.subtract.reduce(arr, axis = 1, keepdims=True)
print(subCols)
print(subCols.shape)

print(np.negative(subRows))
print(np.negative(subCols))
