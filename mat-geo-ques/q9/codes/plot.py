import ctypes
import numpy as np
import matplotlib.pyplot as plt

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

class Triangle(ctypes.Structure):
    _fields_ = [("length", ctypes.c_double),
                ("vertex1", Point),
                ("vertex2", Point),
                ("vertex3", Point),
                ("num_points", ctypes.c_int),
                ("sides", ctypes.POINTER(ctypes.POINTER(Point)))]

gen = ctypes.CDLL('./generate.so')
gen.get_vertex.argtypes = [Point, Point]
gen.get_vertex.restype = ctypes.POINTER(Point)
gen.generate_triangle.argtypes = [ctypes.POINTER(Triangle)]
gen.generate_triangle.restype = None

num_points = 1000
length = 5.0

to_draw = Triangle()
to_draw.length = length
to_draw.num_points = num_points
to_draw.vertex1 = Point(0.0, 0.0)
to_draw.vertex2 = Point(length, 0.0)
vertex_ptr = gen.get_vertex(to_draw.vertex1, to_draw.vertex2)
to_draw.vertex3 = vertex_ptr.contents

sides_array_type = ctypes.POINTER(Point) * 3
to_draw.sides = sides_array_type()

gen.generate_triangle(ctypes.byref(to_draw))

points_np = np.zeros((3, num_points), dtype=[('x', np.float64), ('y', np.float64)])
for i in range(3):
    for j in range(num_points):
        points_np[i][j] = (to_draw.sides[i][j].x, to_draw.sides[i][j].y)

fig = plt.figure()
ax = plt.gca()
for i in range(3):
    ax.plot(points_np[i]['x'], points_np[i]['y'])
ax.annotate(f"({to_draw.vertex1.x}, {to_draw.vertex1.y})", (to_draw.vertex1.x, to_draw.vertex1.y), textcoords="offset points", xytext=(20, 15), ha="center")
ax.annotate(f"({to_draw.vertex2.x}, {to_draw.vertex2.y})", (to_draw.vertex2.x, to_draw.vertex2.y), textcoords="offset points", xytext=(-15, 15), ha="center")
ax.annotate(f"({to_draw.vertex3.x}, {to_draw.vertex3.y})", (to_draw.vertex3.x, to_draw.vertex3.y), textcoords="offset points", xytext=(-5, 5), ha="center")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Equilateral triangle with side length 5cm')
plt.savefig('../figs/fig.png')
plt.show()

