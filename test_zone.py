import numpy as np

a = np.empty([1,2])

print(a)

a = np.append(a, [[1,2]], axis=0)

print(a)