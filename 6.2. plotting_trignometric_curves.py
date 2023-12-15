import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')  # uses black background while displaying the plot graph


# plotting trignometric curves

x_sin = np.arange(0,2*np.pi, 0.1)
y_sin = np.sin(x_sin)

print(y_sin)

print(plt.figure(figsize = (6,6)))
print(plt.plot(x_sin,y_sin))
print(plt.title('Sin Curve'))
print(plt.show())
