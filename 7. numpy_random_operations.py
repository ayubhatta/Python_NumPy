import numpy as np 
import matplotlib.pyplot as plt
plt.style.use('dark_background')

print(np.random.random(1))  # prints an array of a random integer or float value 
print("\n")

print(np.random.random(2))  # prints an array of 2 random integers or float values
print("\n")

print(np.random.random((2,2)))  # prints an array of 2 rows and 2 columns 
print("\n")

print(np.random.randint(1,10))  # prints a random integer between 1 to 10
print("\n")

print(np.random.randint(1,10, (2,2)))  #prints a 2D array of random numbers between 1 to 10 in which there are 3 rows and 2 columns
print("\n")

print(np.random.randint(1,10, (3,4,5)))  # prints a 3D array of random numbers between 1 to 10 in which there are 4 rows and 5 columns
print("\n")

print(np.random.rand(2,2))  # prints a 2D array of 2 rows and 2 columns
print("\n")

print(np.random.randn(2,2))  # "n" after rand prints a 2D array with random negative numbers
print("\n")

a = np.arange(1,10)  # generates an array of numbers from 1 to 10
print(a)  
print("\n")

print(np.random.choice(a))  # prints a random number from array "a".