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


x1, y1 = 0, 0
x2, y2 = 5, 0
x3, y3 = 2.5 , 5* 3**(0.5) / 2

num_points = 1000
points = np.zeros((num_points, 2), dtype=np.double)

gen.generate_line_points(
    x1, y1, x2, y2,
    points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    num_points
)

fig = plt.figure()
ax = plt.gca()
plt.plot(points[:, 0], points[:, 1])

points = np.zeros((num_points, 2), dtype=np.double)
gen.generate_line_points(
    x1, y1, x3, y3,
    points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    num_points
)
plt.plot(points[:, 0], points[:, 1])
points = np.zeros((num_points, 2), dtype=np.double)
gen.generate_line_points(
    x2, y2, x3, y3,
    points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    num_points
)
plt.plot(points[:, 0], points[:, 1])

plt.annotate( '(0,0)',(x1, y1), textcoords="offset points", xytext = (-5,-5), ha = "center")
plt.annotate('(5,0)',(x2, y2),textcoords = "offset points", xytext = (-5, -5), ha = "center")
plt.annotate( f"({x3}, {y3})", (x3, y3),textcoords="offset points"
             , xytext=(5,0))  # Access value from ctypes object
gen.free_ptr(points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Equilateral triangle with side 5cm')
plt.savefig('../figs/fig.png')
plt.show()


