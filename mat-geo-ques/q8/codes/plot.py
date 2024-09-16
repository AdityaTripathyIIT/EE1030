import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import ctypes

# Define your points
x1, y1, z1 = -18, 12, -4  # Change these values as needed
x2, y2, z2 = 0, 0, 0

def plot_vector_and_angles(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    gen = ctypes.CDLL('./generate.so')

    gen.generate_line_points.argtypes = [
        ctypes.c_double, ctypes.c_double, ctypes.c_double,
        ctypes.c_double, ctypes.c_double, ctypes.c_double,
        ctypes.POINTER(ctypes.c_double), ctypes.c_int
    ]

    gen.generate_line_points.restype = None
    num_points = 1000

    points = np.zeros((num_points, 3), dtype=np.double)
    gen.generate_line_points(
        x1, y1, z1, x2, y2, z2,
        points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        num_points
    )
    ax.plot(points[:, 0], points[:, 1], points[:, 2], c='r')

    # Plot the coordinate axes
    ax.plot([0, x], [0, 0], [0, 0], color='r', linewidth=2, label='X-axis')
    ax.plot([0, 0], [0, y], [0, 0], color='g', linewidth=2, label='Y-axis')
    ax.plot([0, 0], [0, 0], [0, z], color='b', linewidth=2, label='Z-axis')

    # Plot the vector from origin to the point (x, y, z)
    # ax.quiver(0, 0, 0, x, y, z, color='k', label=f'Vector to ({x:.2f}, {y:.2f}, {z:.2f})')

    # Label the point
    ax.text(x, y, z, f'({x:.2f}, {y:.2f}, {z:.2f})', color='k')

    # Setting the limits and labels
    ax.set_xlim([min(0, x) - 1, max(1.5, x) + 1])
    ax.set_ylim([min(0, y) - 1, max(1.5, y) + 1])
    ax.set_zlim([min(0, z) - 1, max(1.5, z) + 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

    # Function to compute angles
    def compute_angles(x, y, z):
        norm = np.sqrt(x**2 + y**2 + z**2)
        angles = {
            'X': np.arccos(x / norm),
            'Y': np.arccos(y / norm),
            'Z': np.arccos(z / norm)
        }
        return angles

    angles = compute_angles(x, y, z)

    # Function to plot arcs
    def plot_arc(start_point, end_point, normal, angle, color, label, angle_value):
        t = np.linspace(0, angle, 100)
        arc_radius = 1.2 * np.max([np.linalg.norm(end_point), 1.5])
        arc_center = np.zeros(3)
        arc = arc_radius * (np.outer(np.cos(t), end_point) + np.outer(np.sin(t), np.cross(normal, end_point))) + arc_center
        ax.plot(arc[:, 0], arc[:, 1], arc[:, 2], color,  linewidth=1, label=label)
        
        # Annotate angle value
        mid_point = arc[len(arc) // 2]
        ax.text(mid_point[0], mid_point[1], mid_point[2], f'{angle_value:.2f}°', color=color, fontsize=9)

    # Plot the arcs showing angles and annotate angle values
    norm_vector = np.array([x, y, z]) / np.linalg.norm([x, y, z])
    
    # Angle with X-axis
    angle_X = np.arccos(np.dot(norm_vector, [1, 0, 0]))
    plot_arc(np.array([0, 0, 0]), np.array([1, 0, 0]), np.cross([1, 0, 0], norm_vector), angle_X, 'r', 
             f'Angle with X-axis: {np.degrees(angle_X):.2f}°', np.degrees(angle_X))

    # Angle with Y-axis
    angle_Y = np.arccos(np.dot(norm_vector, [0, 1, 0]))
    plot_arc(np.array([0, 0, 0]), np.array([0, 1, 0]), np.cross([0, 1, 0], norm_vector), angle_Y, 'g', 
             f'Angle with Y-axis: {np.degrees(angle_Y):.2f}°', np.degrees(angle_Y))

    # Angle with Z-axis
    angle_Z = np.arccos(np.dot(norm_vector, [0, 0, 1]))
    plot_arc(np.array([0, 0, 0]), np.array([0, 0, 1]), np.cross([0, 0, 1], norm_vector), angle_Z, 'b', 
             f'Angle with Z-axis: {np.degrees(angle_Z):.2f}°', np.degrees(angle_Z))

    ax.legend()
    plt.show()

# Example usage
plot_vector_and_angles(x1, y1, z1)

