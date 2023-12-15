import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')  # uses black background while displaying the plot graph

# 1st Graph

x = np.arange(1,11)
y = np.arange(10, 110, 10)

print(plt.figure(figsize = (6, 6)))
print(plt.plot(x,y, 'r--'))
print(plt.title('Random Curve'))
print(plt.show())

# SIN CURVE

x_sin = np.arange(0,2*np.pi, 0.1)
y_sin = np.sin(x_sin)

print(y_sin)

print(plt.figure(figsize = (6,6)))
print(plt.plot(x_sin,y_sin, 'b--'))
print(plt.title('Sin Curve'))
print(plt.show())

# COS CURVE

x_cos = np.arange(0, 2*np.pi, 0.1)
y_cos = np.cos(x_cos)

print(plt.figure(figsize = (6,6)))
print(plt.plot(x_cos, y_cos, 'g--'))
print(plt.title('Cos Curve'))
print(plt.show())

# TAN CURVE

x_tan = np.arange(0, 2*np.pi, 0.1)
y_tan = np.tan(x_tan)

print(plt.figure(figsize = (6,6)))
print(plt.plot(x_tan, y_tan, 'y--'))
print(plt.title('Tan Curve'))
print(plt.show())

# COT CURVE

x_cot = np.arange(0, 2*np.pi, 0.1)
y_cot = 1/np.tan(x_cot)

print(plt.figure(figsize = (6,6)))
print(plt.plot(x_cot, y_cot, 'w--'))
print(plt.title('Cot Curve'))
print(plt.show())


# NOW COMBINING ALL DIFFERENT PLOTS INTO A SINGLE PLOT

print(plt.figure(figsize = (6,6)))

print(plt.subplot(2,2,1))
print(plt.plot(x_sin, y_sin, 'r--'))
print(plt.title('Sin Curve'))

print(plt.subplot(2,2,2))
print(plt.plot(x_cos, y_cos, 'b--'))
print(plt.title("Cos Curve"))

print(plt.subplot(2,2,3))
print(plt.plot(x_tan, y_tan, 'g--'))
print(plt.title('Tan Curve'))

print(plt.subplot(2,2,4))
print(plt.plot(x_cot, y_cot, 'w--'))
print(plt.title('Cot Curve'))

print(plt.show())