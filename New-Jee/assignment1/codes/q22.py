import numpy as np
import matplotlib.pyplot as plt

y = np.linspace(-5, 5, 400)

x_positive = np.sqrt((y**2 + y + 10) / 3)
x_negative = -np.sqrt((y**2 + y + 10) / 3)

line1_x = np.linspace(-4, 6, 400)
line1_y = 4 * line1_x - 7

line2_y = -0.25 * line1_x + 1.5

plt.figure(figsize=(10, 6))

plt.plot(x_positive, y, color='blue')
plt.plot(x_negative, y, color='blue')

plt.plot(line1_x, line1_y, color='green')
plt.plot(line1_x, line2_y, color='purple')

plt.scatter(2, 1, color='red')
plt.annotate('(2, 1)', (2, 1), textcoords="offset points", xytext=(0,10), ha='center')
plt.scatter(0, 3/2, color='red')
plt.annotate('(0, 3/2)', (0, 3/2), textcoords="offset points", xytext=(0,10), ha='center')
plt.xlim(-5, 5)
plt.ylim(-6, 6)
plt.axhline()
plt.axvline()
plt.grid()
plt.title('Plot of the Curve and Lines')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.savefig('../figs/q22.png')
plt.show()

