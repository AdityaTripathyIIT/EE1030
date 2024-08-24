import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

points = np.loadtxt('points.txt')

x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

v1 = np.array([2.0, 3.0, 4.0])
v2 = np.array([-1.0, -2.0, 1.0])
v3 = np.array([5.0, 8.0, 7.0])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c='blue', marker='o', label='Random Points')
ax.scatter(*v1, c='red', s=100, label='Vertex 1 (2,3,4)')
ax.scatter(*v2, c='green', s=100, label='Vertex 2 (-1,-2,1)')
ax.scatter(*v3, c='orange', s=100, label='Vertex 3 (5,8,7)')

ax.text(v1[0], v1[1], v1[2], ' (2,3,4)', color='red', fontsize=12)
ax.text(v2[0], v2[1], v2[2], ' (-1,-2,1)', color='green', fontsize=12)
ax.text(v3[0], v3[1], v3[2], ' (5,8,7)', color='orange', fontsize=12)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Scatter Plot of Random Points and Tetrahedron Vertices')

ax.legend()
plt.savefig('../figs/fig.png')
plt.show()

