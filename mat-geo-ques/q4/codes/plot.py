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

x1, y1, z1 = 2, 3, 4
x2, y2, z2 = -1, -2, 1
x3, y3, z3 = 5, 8 ,7
num_points = 1000

points = np.zeros((num_points, 3), dtype=np.double)
gen.generate_line_points(
    x1, y1, z1, x2, y2, z2,
    points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    num_points
)
    
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='r', marker='o')
ax.text(x1, y1, z1, ' (2,3,4)', color='red', fontsize=12)
ax.text(x2, y2, z2, ' (-1,-2,1)', color='green', fontsize=12)
ax.text(x3, y3, z3, ' (5,8,7)', color='orange', fontsize=12)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('1000 Points on the Line')
gen.free_ptr(points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
plt.savefig('../figs/fig.png')
plt.show()

