import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 100)
x = np.sqrt(1/2) * np.cos(theta)  # From 2x^2 + y^2 = 1
y = np.sin(theta)

point1 = (-1/(3*np.sqrt(2)), 0)
point2 = (0, np.sqrt(2)/3)
point3 = (1/(3*np.sqrt(2)), 2*np.sqrt(2)/3)

line_x = [point1[0], point2[0]]
line_y = [point1[1], point2[1]]

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Ellipse: $2x^2 + y^2 = 1$', color='blue')
plt.plot(line_x, line_y, label='Line joining points', color='orange', linestyle='--')

plt.scatter(*point1, color='red', label='Point 1: (-1/(3√2), 0)')
plt.scatter(*point2, color='green', label='Point 2: (0, √2/3)')
plt.scatter(*point3, color='purple', label='Point 3: (1/(3√2), 2√2/3)')

plt.axis('equal')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.title('Plot of the Ellipse and Points')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.annotate(f"(-1/(3sqrt(2)), 0)", point1)
plt.annotate(f"(0, sqrt2/3)", point2)
plt.annotate(f"(1/(3sqrt2), 2sqrt2/3)", point3)
plt.savefig('../figs/q18.png')
plt.show()

