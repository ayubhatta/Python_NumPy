# importing numpy library as np
import numpy as np

a = np.arange(1, 51)
a = a.reshape(10,5)
print(a)

# print(a[0])

print(a[:, 2:5].dtype)
