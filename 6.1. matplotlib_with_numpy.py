import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')  # uses black background while displaying the plot graph


'''
USING MATPLOTLIB WITH NUMPY
'''

x = np.arange(1,11)
y = np.arange(10, 110, 10)

print(plt.figure(figsize = (6, 6)))
print(plt.plot(x,y, 'r--'))
print(plt.show())

