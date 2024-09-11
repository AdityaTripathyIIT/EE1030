import ctypes
import numpy as np
import matplotlib.pyplot as plt

gen = ctypes.CDLL('./generate.so')

gen.generate_line_points.argtypes = [
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.c_int
]

gen.generate_line_points.restype = None

x1, y1 = -6, 7
x2, y2  = -1, -5 
x3, y3  = (x1 + x2) /2 , (y1 + y2) / 2 
num_points = 1000

points = np.zeros((num_points, 2), dtype=np.double)

gen.generate_line_points(
    x1, y1, x2, y2,
    points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    num_points
)

fig = plt.figure()
ax = plt.gca()
ax.scatter(points[:, 0], points[:, 1], c='r', marker='o')
ax.text(x1, y1, ' (-6, 7)', color='red', fontsize=12)
ax.text(x2, y2, ' (-1, -5)', color='green', fontsize=12)
ax.text(x3, y3, f"({x3}, {y3})", color='blue', fontsize=12)
gen.free_ptr(points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Line joining the given points and showing the midpoint.')
plt.savefig('../figs/fig.png')
plt.show()

