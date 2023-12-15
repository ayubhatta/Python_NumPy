#np.empty((rows, columns), dtype)
#np.zeros((rows, columns), dtype)
#np.ones((rows, columns), dtype)

# importing numpy library as np
import numpy as np

print(np.empty((4, 4), dtype = float))

print("\n")

x = np.ones(6)
print(x)

print("\n")

y = np.ones((3,5))
print(y)

print("\n")

z = np.ones((3,5), dtype = int)
print(z)

print("\n")

x = np.zeros(4)
print(x)

print("\n")

y = np.zeros((4,8))
print(y)

print("\n")

z = np.zeros((4,8), dtype = int)
print(z)

print("\n")

z = np.ones((4,8), dtype = str)
print(z)

print("\n")

z = np.zeros((4,8), dtype = str)
print(z)

print("\n")

z = np.zeros((4,8), dtype = int)
print(z)

print("\n")

z = np.ones((4,8), dtype = bool)
print(z)

print("\n")

z = np.zeros((4,8), dtype = bool)
print(z)
