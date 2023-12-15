# mathematical operators in numpy

import numpy as np


a = np.arange(0,18).reshape((6,3))
b = np.arange(20,38).reshape((6,3))
print(a)
print("\n")
print(b)
print("\n")

print(a+b)
print("\n")
print(np.add(a,b))
print("\n")

print(a-b)
print("\n")
print(np.subtract(a,b))
print("\n")

print(a*b)
print("\n")
print(np.multiply(a,b))
print("\n")

print(a/b)
print("\n")
print(np.divide(a,b))
print("\n")


print(a.shape)
print(b.shape)

print("\n")

# reshaping b(6,3) as (3, 6)
b = b.reshape((3,6))
print(a.shape)
print(b.shape)

# dot product between a and b
print(a@b)
print("\n")

# works same as above ( a@b )
print(a.dot(b))
print("\n")

# maximum value of array b
print(b.max())
print("\n")

# minimum value of array b
print(b.min())
print("\n")

# argument maximum of array b
print(b.argmax())
print("\n")

# sum of array b
print(np.sum(b))
print("\n")

# axis 1 means rows
# output displayed is the sum of each rows
print(np.sum(b, axis = 1))
print("\n")

# axis 0 means columns
# output displayed is the sum of each columns
print(np.sum(b, axis = 0))
print("\n")

# mean of array b
print(np.mean(b))
print("\n")

#square root of array b
print(np.sqrt(b))
print("\n")

# standard deviation of array b
print(np.std(b))
print("\n")

# log of array b
print(np.log(b))
print("\n")