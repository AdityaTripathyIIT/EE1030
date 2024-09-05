import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./solve.so')

lib.createMat.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))
lib.createMat.argtypes = [ctypes.c_int, ctypes.c_int]

lib.freeMat.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_int]

lib.solveMatrixVectorProduct.argtypes = [
    ctypes.POINTER(ctypes.c_double), 
    ctypes.POINTER(ctypes.c_double), 
    ctypes.POINTER(ctypes.c_double)
]

lib.generate_line_points.argtypes = [
    ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), 
    ctypes.POINTER(ctypes.c_double), 
    ctypes.c_int
]

lib.free_ptr.argtypes = [ctypes.POINTER(ctypes.c_double)]


#This function exists as a wrapper on the C fuction just for reusability of 
#this large chunk of code
def generate_line_points(p1, p2, num_points):
    points_matrix = lib.createMat(2, 2)
    points_array = np.array([p1, p2], dtype=np.double)

    for i in range(2):
        for j in range(2):
            points_matrix[i][j] = points_array[i, j]

    generated_points = (ctypes.c_double * (num_points * 2))()

    lib.generate_line_points(points_matrix, generated_points, num_points)

    lib.freeMat(points_matrix, 2)

    return np.array(generated_points).reshape((num_points, 2))

#importing ends here



#solving starts here
point1 = np.array([7.0, 6.0])
point2 = np.array([3.0, 4.0])

row1 = [point2[0] - point1[0], point2[1]-point1[1], -30]
row2 = [0, 1, 0]
row1_array = (ctypes.c_double * 3)(*row1)
row2_array = (ctypes.c_double * 3)(*row2)

temp_C_arr = (ctypes.c_double * 2)()

lib.solveMatrixVectorProduct(row1_array, row2_array, temp_C_arr)
solution = np.array(temp_C_arr)

print(f"Solution of the system:")
print(f"x = {solution[0]}")
print(f"y = {solution[1]}")
#solving ends here


#plotting begins here

line1 = generate_line_points(point1,point2, 1000)
       
plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'ro', label='Original Points')
plt.scatter(line1[:, 0], line1[:, 1], label='Line joining (7,6) and (3,4)')


line2 = generate_line_points(solution, point1, 1000)
plt.scatter(line2[:, 0], line2[:, 1], label='Line joining (7,6) and solution point')


line3 = generate_line_points(solution, point2, 1000)
plt.scatter(line3[:, 0], line3[:, 1], label='Line Joining (3,4) and solution point')

plt.text(point1[0], point1[1], '(7,6)')
plt.text(point2[0], point2[1], '(3,4)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Lines Joining Points and Solution')
plt.grid(True)
plt.show()

