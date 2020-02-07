import numpy as np

a1 = np.arange(10)
a2 = np.arange(10)
a3 = np.arange(10)

print(np.equal(a1, a2+0.0000001))
print(np.isclose(a1, a2+0.000001).any())
