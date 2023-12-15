#np.arange(start, end, step)
#np.reshape((rows, columns))
#np.flatten()
#np.ravel()

# importing numpy library as np
import numpy as np

a = np.arange(1,20)
print(a)

print("\n")

print("Odd numbers")
a = np.arange(1,20,2)
print(a)

print("\n")

print("even numbers")
a = np.arange(2,20,2)
print(a)


print("\n")
print("\n")

print("Reshape function.")
a = a.reshape((3,3))
print(a)

print("\n")

print("arange function.")
b = np.arange(1,100,2)
print(b)

print("\n")

print("Reshape function.")
b = b.reshape((10,5))
print(b)



print("\n")
print("\n")



# flatten function reverses the reshape function and converts to or converts back to the arange function

print("flatten function reverses the reshape function and converts to or converts back to the arange function")

print("flatten_function")
b = b.flatten()
print(b)



# Ravel function converts multiple rows and multiple columns into a single row of multiple columns.

a = np.arange(2,20,2)
print(a)

print("\n")

a = a.reshape((3,3))
print(a)

print("\n")

a = a.ravel()
print(a)


# ravel() 
'''
i. Returns only reference/view of original array.
ii. If you modify the array you would notice that the value of original array also changes.
iii. Ravel is faster than flatten() as it does not occupy any memory.
iv. Ravel is a library-level function.
'''

# flatten()
'''
i. Returns copy of original array.
ii. if you modify any value of this array, value of original array is not affected.
iii. flatten() is comparatively slower than ravel() as it occupies memory.
iv. Flatten is a method of an ndarray object.
''' 

