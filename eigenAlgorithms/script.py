import numpy as np
from scipy.linalg import hessenberg
from scipy.linalg import qr
from pprint import pprint
# Define the complex matrix A
'''
A = np.array([[5+1j, 9+6j, 3+2j, 5+1j, 1+1j],
              [3+2j, 3+7j, 0+4j, 2+3j, 2+4j],
              [6+3j, 2+8j, 8+6j, 9+5j, 3+7j],
              [8+4j, 7+9j, 1+8j, 8+7j, 4+2j],
              [5+5j, 2+0j, 6+0j, 7+9j, 5+5j]])
A = np.array([[5+1j, 9+6j, 3+9j, 5+8j],
              [3+2j, 3+7j, 0+7j, 2+6j],
              [6+3j, 2+8j, 8+5j, 9+4j],
              [8+4j, 7+9j, 1+3j, 8+2j]])

A = np.array([[5+0j, 9+0j, 3+0j, 5+0j],
              [3+0j, 3+0j, 0+0j, 2+0j],
              [6+0j, 2+0j, 8+0j, 9+0j],
              [8+0j, 7+0j, 1+0j, 8+0j]])
A = np.array([
    [complex(2, 0), complex(3, 0), complex(5, 0), complex(7, 0), complex(11, 0)],
    [complex(13, 0), complex(17, 0), complex(19, 0), complex(23, 0), complex(29, 0)],
    [complex(31, 0), complex(37, 0), complex(41, 0), complex(43, 0), complex(47, 0)],
    [complex(53, 0), complex(59, 0), complex(61, 0), complex(67, 0), complex(71, 0)],
    [complex(73, 0), complex(79, 0), complex(83, 0), complex(89, 0), complex(97, 0)]
])
'''
A = np.array([
    [3.47 + 8.21j, 5.91 + 4.37j, 1.42 + 7.68j, 9.03 + 3.57j, 7.22 + 0.89j, 2.47 + 5.35j, 4.91 + 6.01j, 6.78 + 9.12j, 1.02 + 3.47j, 8.15 + 1.33j],
    [0.85 + 9.14j, 6.12 + 4.71j, 8.39 + 0.74j, 4.22 + 7.94j, 3.55 + 8.61j, 5.81 + 6.39j, 9.67 + 1.62j, 2.47 + 7.14j, 0.36 + 6.49j, 1.99 + 4.55j],
    [7.73 + 2.43j, 9.04 + 6.78j, 1.67 + 9.86j, 8.55 + 0.32j, 0.12 + 3.01j, 6.39 + 1.78j, 4.52 + 9.09j, 2.61 + 4.02j, 5.84 + 7.53j, 8.02 + 2.79j],
    [5.61 + 9.77j, 2.89 + 0.97j, 1.24 + 5.65j, 6.31 + 8.47j, 4.71 + 0.81j, 9.22 + 7.69j, 3.43 + 4.32j, 2.56 + 6.94j, 8.94 + 3.62j, 1.33 + 7.56j],
    [6.43 + 3.29j, 4.71 + 9.21j, 7.25 + 2.16j, 9.45 + 8.13j, 0.51 + 4.76j, 5.23 + 2.92j, 8.31 + 7.64j, 1.09 + 6.39j, 7.87 + 1.54j, 3.34 + 9.85j],
    [3.90 + 6.58j, 9.84 + 3.73j, 2.60 + 1.93j, 1.57 + 7.79j, 4.43 + 8.94j, 7.23 + 5.17j, 6.94 + 4.81j, 3.89 + 9.28j, 5.12 + 2.41j, 2.67 + 0.99j],
    [9.30 + 1.12j, 6.57 + 7.88j, 4.98 + 3.22j, 7.10 + 5.41j, 8.64 + 0.86j, 1.75 + 4.72j, 3.59 + 9.94j, 9.51 + 2.29j, 0.18 + 5.34j, 2.48 + 1.21j],
    [1.65 + 9.42j, 0.95 + 6.87j, 8.25 + 5.03j, 4.80 + 0.58j, 7.58 + 2.04j, 3.18 + 9.62j, 6.42 + 3.47j, 1.83 + 8.76j, 5.27 + 1.29j, 2.70 + 6.03j],
    [9.08 + 2.97j, 7.32 + 5.69j, 3.49 + 7.91j, 8.03 + 0.53j, 5.90 + 9.12j, 6.14 + 4.73j, 2.86 + 3.20j, 4.55 + 8.24j, 1.02 + 6.71j, 9.90 + 2.54j],
    [4.60 + 6.83j, 5.26 + 1.28j, 7.33 + 9.51j, 3.12 + 7.24j, 9.59 + 2.38j, 8.74 + 6.79j, 0.94 + 5.35j, 2.45 + 8.92j, 6.58 + 0.39j, 1.18 + 9.20j]
])
# Compute the Hessenberg form using SciPy's 'hessenberg' function
H = hessenberg(A)
#print("Upper hessenberg:")
#pprint(H)
eig1, _= np.linalg.eig(H)
#print("Eigen values of upper hessenberg matrix")
pprint(eig1)
Q, R = qr(H)
#print("Upper triangular:")
#pprint(R)
#eig2, _ = np.linalg.eig(A)
#print("Eigen values of original matrix")
print("\n")



