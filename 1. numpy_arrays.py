import numpy as np

list = [1,2,3,4,5]
#print(list)

print("\n")

print("1D Array")
a = np.array([1,2,3,4,5])
print(a)
print("The size of the array is ", a.size)
print("The shape of the array is ", a.shape)
print("The type of the array is ", a.dtype)

print("\n")

print("2D Array")
b = np.array([[1,2,3,4,5],
              [6,7,8,9,10]])
print(b)
print("The size of the array is ", b.size)
print("The shape of the array is ", b.shape)
print("The type of the array is ", b.dtype)

print("\n")

print("3D Array")
c = np.array([[[1,2,3,4,5],
               [6,7,8,9,10],
               [11,12,13,14,15]]])
print(c)
print("The size of the array is ", c.size)
print("The shape of the array is ", c.shape)
print("The type of the array is", c.dtype)

print("\n")

print("float")
d = np.array([[1,2,3,4.5,5],
              [6,7,8,9,10],
              [11,12,13.5,14,15]])
print(d)
print(d.dtype)

print("\n")

# array transpose

print("The transposed(inverted) of d is: ")
print(d.transpose())