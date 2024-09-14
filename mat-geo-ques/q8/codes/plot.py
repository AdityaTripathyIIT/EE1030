import ctypes
import numpy as np
import matplotlib.pyplot as plt

gen = ctypes.CDLL('./generate.so')

gen.generate_line_points.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.c_int
]

gen.generate_line_points.restype = None

x1, y1, z1 = -18, 12, -4
x2, y2, z2 = 0, 0, 0
num_points = 1000
vec1 = np.array([x1,y1,z1]).reshape(-1,1)
vec1 = vec1 /((vec1.T @ vec1)**0.5)
points = np.zeros((1,3*num_points), dtype=np.double)


gen.generate_line_points(
    x1, y1, z1, x2, y2, z2,
    points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    num_points
)
points = np.array(points).reshape((num_points,3))    
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='r', marker='o')
ax.text(x1, y1, z1, ' (-18,12,-4)', color='red', fontsize=12)
ax.text(x2, y2, z2, ' (0,0,0)', color='green', fontsize=12)
gen.generate_line_points(
    vec1[0,0], vec1[1,0], vec1[2,0], x2, y2, z2,
    points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    num_points
)

ax.text(vec1[0,0], vec1[1,0], vec1[2,0], f"({vec1[0,0]:.2f},{vec1[1,0]:.2f},{vec1[2,0]:.2f})", color='red', fontsize=12)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('1000 Points on the Line')
gen.free_ptr(points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
plt.savefig('../figs/fig.png')
plt.show()
