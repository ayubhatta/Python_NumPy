import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')  # uses black background while displaying the plot graph

x_cos = np.arange(0, 2*np.pi, 0.1)
y_cos = np.cos(x_cos)

print(plt.figure(figsize = (6,6)))
print(plt.plot(x_cos, y_cos))
print(plt.title('Cos Curve'))
print(plt.show())