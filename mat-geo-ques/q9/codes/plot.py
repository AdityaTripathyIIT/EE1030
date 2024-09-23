import ctypes
import numpy as np
import matplotlib.pyplot as plt
class point (ctypes.Structure) :
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)
                ]
    x = 0
    y = 0
class triangle (ctypes.Structure) :
    _fields_ = [("vertex1", ctypes.Structure),
                ("vertex2", ctypes.Structure),
                ("vertex3", ctypes.Structure),
                ("num_points", ctypes.c_int),
                ("length", ctypes.c_int),
                ("sides", ctypes.POINTER(ctypes.POINTER(ctypes.Structure)))
            ]
    vertex1.x = 0
    vertex1.y = 0
    vertex2.x = length
    vertex.y = 0
    sides = ctypes.Structure * (3 * num_points)()


to_draw = triangle()
gen = ctypes.CDLL('./generate.so')
gen.get_vertex.argtypes = [ctypes.Structure, ctypes.Structure]
gen.get_vertex.restype = ctypes.POINTER(ctypes.Structure)
gen.generate_triangle.argtypes = [ctypes.c_double, ctypes.c_int, ctypes.POINTER(ctypes.Structure * (3 * num_points))()]
gen.generate_triangle.restype = None

# Input length and num_points
num_points = 1000
length = 5.0
to_draw.length = length
# you can also change vertex1 and vertex2 to change th eorientation of the triangle
gen.get_vertex(ctypes.byref(to_draw.vertex1), ctypes.byref(to_draw.vertex2))
gen.generate_triangle(ctypes.byref(to_draw))

fig = plt.figure()
ax = plt.gca()
points_np = np.array(to_draw.sides).reshape((3, num_points)) 
plt.plot(points_np[0, :].x, points_np[0, :, 1].y)
plt.plot(points_np[1, :].x, points_np[1, :].y)
plt.plot(points_np[2, :].x, points_np[2, :].y)
plt.annotate(f"({to_draw.vertex1.x}, {to_draw.vertex1.y})", (to_draw.vertex1.x, to_draw.vertex1.y), textcoords="offset points", xytext=(-5, -5), ha="center")
plt.annotate(f"({to_draw.vertex2.x}, {to_draw.vertex2.y})", (to_draw.vertex2.x, to_draw.vertex2.y), textcoords="offset points", xytext=(-5, -5), ha="center")
plt.annotate(f"({to_draw.vertex3.x}, {to_draw.vertex3.y})", (to_draw.vertex3.x, to_draw.vertex3.y), textcoords="offset points", xytext=(-5, -5), ha="center")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Equilateral triangle with side 5cm')
plt.savefig('../figs/fig.png')
plt.show()

