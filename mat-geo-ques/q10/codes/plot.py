import ctypes
import numpy as np
import matplotlib.pyplot as plt

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

class Circle(ctypes.Structure):
    _fields_ = [("center", Point),
                ("radius", ctypes.c_double),
                ("num_points", ctypes.c_int),
                ("points", ctypes.POINTER(Point))]

gen = ctypes.CDLL('./generate.so')
gen.generate_circle_points.argtypes = [ctypes.POINTER(Circle)]
gen.generate_circle_points.restype = None

num_points = 1000
my_center = Point(0.5, 0.25)
radius = 1 / 12

to_draw = Circle()
to_draw.radius = radius
to_draw.num_points = num_points
to_draw.center = my_center

points_array_type = Point * to_draw.num_points
to_draw.points = points_array_type()

gen.generate_circle_points(ctypes.byref(to_draw))

points_np = np.zeros((num_points,), dtype=[('x', np.float64), ('y', np.float64)])

for j in range(num_points):
    points_np[j] = (to_draw.points[j].x, to_draw.points[j].y)

fig = plt.figure()
ax = plt.gca()
ax.plot(points_np['x'], points_np['y'])
ax.annotate(f"({to_draw.center.x}, {to_draw.center.y})", (to_draw.center.x, to_draw.center.y), textcoords="offset points", xytext=(20, 15), ha="center")
ax.plot([to_draw.center.x, to_draw.points[400].x],[to_draw.center.y, to_draw.points[400].y]);
ax.annotate(f"Radius : {to_draw.radius : 0.3f}", ((to_draw.center.x + to_draw.points[400].x) / 2, (to_draw.center.y + to_draw.points[400].y) / 2))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Circle with given parameters')
plt.savefig('../figs/fig.png')
plt.show()

