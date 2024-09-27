import ctypes
import numpy as np
import matplotlib.pyplot as plt

circle_lib = ctypes.CDLL('./generate.so')

circle_lib.generate_circle_points.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double, ctypes.c_int]
circle_lib.generate_circle_points.restype = ctypes.POINTER(ctypes.c_double)  # Specify return type

def generate_circle_points(center, radius, num_points):
    points_ptr = circle_lib.generate_circle_points(center, radius, num_points)  # Call C function
    points = np.ctypeslib.as_array(points_ptr, (num_points, 2))
    return points

center_array_type = ctypes.c_double * 2  # Define a ctypes array type
my_center = center_array_type(0.5, 0.25)  # Initialize the center array
radius = 1/12
num_points = 1000

circle_points = generate_circle_points(my_center, radius, num_points)

plt.figure()
plt.plot(circle_points[:, 0], circle_points[:, 1], marker='o', markersize=1)
plt.plot((my_center[0], circle_points[200, 0]),(my_center[1], circle_points[200, 1]))
plt.annotate(f"({my_center[0]}, {my_center[1]})", (my_center[0], my_center[1]))
plt.annotate(f"({circle_points[200, 0]:.3f}, {circle_points[200, 1 ]:.3f})", (circle_points[200, 0], circle_points[200, 1]))
midpoint_x = (my_center[0] + circle_points[200, 0]) / 2
midpoint_y = (my_center[1] + circle_points[200, 1]) / 2
plt.annotate(f"Radius:{radius : .3f}", (midpoint_x, midpoint_y))
plt.title('Points on a Circle')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axis('equal')
plt.savefig('../figs/fig.png')
plt.grid()
plt.show()


