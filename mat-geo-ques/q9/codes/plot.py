import ctypes
import numpy as np
import matplotlib.pyplot as plt

gen = ctypes.CDLL('./generate.so')
gen.get_vertex.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
gen.get_vertex.restype = None
gen.generate_triangle.argtypes = [ctypes.c_double, ctypes.c_int, ctypes.POINTER(ctypes.c_double * 3 * 1000 * 2)]
gen.generate_triangle.restype = None

# Input length
length = 5.0

x3 = ctypes.c_double()
y3 = ctypes.c_double()
gen.get_vertex(length, 0.0, ctypes.byref(x3), ctypes.byref(y3))
vertices = [[0.0, 0.0], [length, 0.0], [x3.value, y3.value]]
num_points = 1000
points = (ctypes.c_double * (3 * num_points * 2))()

gen.generate_triangle(length, num_points, ctypes.cast(points, ctypes.POINTER(ctypes.c_double * 3 * 1000 * 2)))

fig = plt.figure()
ax = plt.gca()
points_np = np.frombuffer(points, dtype=np.double).reshape((3, num_points, 2))
plt.plot(points_np[0, :, 0], points_np[0, :, 1])
plt.plot(points_np[1, :, 0], points_np[1, :, 1])
plt.plot(points_np[2, :, 0], points_np[2, :, 1])
plt.annotate('(0,0)', vertices[0], textcoords="offset points", xytext=(-5, -5), ha="center")
plt.annotate(f"({vertices[1][0]}, 0)", vertices[1], textcoords="offset points", xytext=(-5, -5), ha="center")
plt.annotate(f"({vertices[2][0]}, {vertices[2][1]})", vertices[2], textcoords="offset points", xytext=(5, 5), ha="center")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Equilateral triangle with side 5cm')
plt.savefig('../figs/fig.png')
plt.show()

