import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')  # uses black background while displaying the plot graph


x_cot = np.arange(0, 2*np.pi, 0.1)
y_cot = 1/np.tan(x_cot)

print(plt.figure(figsize = (6,6)))
print(plt.plot(x_cot, y_cot))
print(plt.title('Cot Curve'))
print(plt.show())