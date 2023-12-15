import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')  # uses black background while displaying the plot graph

x_tan = np.arange(0, 2*np.pi, 0.1)
y_tan = np.tan(x_tan)

print(plt.figure(figsize = (6,6)))
print(plt.plot(x_tan, y_tan))
print(plt.title('Tan Curve'))
print(plt.show())