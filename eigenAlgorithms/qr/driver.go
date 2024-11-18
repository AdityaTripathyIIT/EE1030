package main

import(
    "fmt"
)

func main(){

    /*
    matrix := [][]complex128{
        {complex(5, 1), complex(9, 2), complex(3, 9), complex(5, 3), complex(1, 1)},
        {complex(3, 2), complex(3, 5), complex(0, 8), complex(2, 5), complex(2, 4)},
        {complex(6, 3), complex(2, 6), complex(8, 7), complex(9, 6), complex(3, 6)},
        {complex(8, 4), complex(7, 7), complex(1, 6), complex(8, 7), complex(4, 8)},
        {complex(5, 5), complex(2, 8), complex(6, 5), complex(7, 8), complex(5, 8)},
    }
    matrix := [][]complex128{
        {complex(5, 1), complex(9, 6), complex(3, 9), complex(5, 8)},
        {complex(3, 2), complex(3, 7), complex(0, 7), complex(2, 6)},
        {complex(6, 3), complex(2, 8), complex(8, 5), complex(9, 4)},
        {complex(8, 4), complex(7, 9), complex(1, 3), complex(8, 2)},
    }

    matrix := [][]complex128{
        {complex(5, 0), complex(9, 0), complex(3, 0), complex(5, 0)},
        {complex(3, 0), complex(3, 0), complex(0, 0), complex(2, 0)},
        {complex(6, 0), complex(2, 0), complex(8, 0), complex(9, 0)},
        {complex(8, 0), complex(7, 0), complex(1, 0), complex(8, 0)},
    }
    matrix := [][]complex128{
        {complex(5, 1), complex(9, 6), complex(3, 2), complex(5, 1), complex(1, 1)},
        {complex(3, 2), complex(3, 7), complex(0, 4), complex(2, 3), complex(2, 4)},
        {complex(6, 3), complex(2, 8), complex(8, 6), complex(9, 5), complex(3, 7)},
        {complex(8, 4), complex(7, 9), complex(1, 8), complex(8, 7), complex(4, 2)},
        {complex(5, 5), complex(2, 0), complex(6, 0), complex(7, 9), complex(5, 5)},

    }
    matrix := [][]complex128{
        {complex(5, 1), complex(9, 6), complex(3, 2), complex(5, 1), complex(1, 1)},
        {complex(3, 2), complex(3, 7), complex(0, 4), complex(2, 3), complex(2, 4)},
        {complex(6, 3), complex(2, 8), complex(8, 6), complex(9, 5), complex(3, 7)},
        {complex(8, 4), complex(7, 9), complex(1, 8), complex(8, 7), complex(4, 2)},
        {complex(5, 5), complex(2, 0), complex(6, 0), complex(7, 9), complex(5, 5)},
    }
    */
    /*
    matrix := [][]complex128{
        {complex(2, 0), complex(3, 0), complex(5, 0), complex(7, 0), complex(11, 0)},
        {complex(13, 0), complex(17, 0), complex(19, 0), complex(23, 0), complex(29, 0)},
        {complex(31, 0), complex(37, 0), complex(41, 0), complex(43, 0), complex(47, 0)},
        {complex(53, 0), complex(59, 0), complex(61, 0), complex(67, 0), complex(71, 0)},
        {complex(73, 0), complex(79, 0), complex(83, 0), complex(89, 0), complex(97, 0)},
    }
    */ 
    matrix := [][]complex128{
		{(3.47 + 8.21i), (5.91 + 4.37i), (1.42 + 7.68i), (9.03 + 3.57i), (7.22 + 0.89i), (2.47 + 5.35i), (4.91 + 6.01i), (6.78 + 9.12i), (1.02 + 3.47i), (8.15 + 1.33i)},
		{(0.85 + 9.14i), (6.12 + 4.71i), (8.39 + 0.74i), (4.22 + 7.94i), (3.55 + 8.61i), (5.81 + 6.39i), (9.67 + 1.62i), (2.47 + 7.14i), (0.36 + 6.49i), (1.99 + 4.55i)},
        {(7.73 + 2.43i), (9.04 + 6.78i), (1.67 + 9.86i), (8.55 + 0.32i), (0.12 + 3.01i), (6.39 + 1.78i), (4.52 + 9.09i), (2.61 + 4.02i), (5.84 + 7.53i), (8.02 + 2.79i)},
        {(5.61 + 9.77i), (2.89 + 0.97i), (1.24 + 5.65i), (6.31 + 8.47i), (4.71 + 0.81i), (9.22 + 7.69i), (3.43 + 4.32i), (2.56 + 6.94i), (8.94 + 3.62i), (1.33 + 7.56i)},
        {(6.43 + 3.29i), (4.71 + 9.21i), (7.25 + 2.16i), (9.45 + 8.13i), (0.51 + 4.76i), (5.23 + 2.92i), (8.31 + 7.64i), (1.09 + 6.39i), (7.87 + 1.54i), (3.34 + 9.85i)},
        {(3.90 + 6.58i), (9.84 + 3.73i), (2.60 + 1.93i), (1.57 + 7.79i), (4.43 + 8.94i), (7.23 + 5.17i), (6.94 + 4.81i), (3.89 + 9.28i), (5.12 + 2.41i), (2.67 + 0.99i)},
        {(9.30 + 1.12i), (6.57 + 7.88i), (4.98 + 3.22i), (7.10 + 5.41i), (8.64 + 0.86i), (1.75 + 4.72i), (3.59 + 9.94i), (9.51 + 2.29i), (0.18 + 5.34i), (2.48 + 1.21i)},
        {(1.65 + 9.42i), (0.95 + 6.87i), (8.25 + 5.03i), (4.80 + 0.58i), (7.58 + 2.04i), (3.18 + 9.62i), (6.42 + 3.47i), (1.83 + 8.76i), (5.27 + 1.29i), (2.70 + 6.03i)},
        {(9.08 + 2.97i), (7.32 + 5.69i), (3.49 + 7.91i), (8.03 + 0.53i), (5.90 + 9.12i), (6.14 + 4.73i), (2.86 + 3.20i), (4.55 + 8.24i), (1.02 + 6.71i), (9.90 + 2.54i)},
        {(4.60 + 6.83i), (5.26 + 1.28i), (7.33 + 9.51i), (3.12 + 7.24i), (9.59 + 2.38i), (8.74 + 6.79i), (0.94 + 5.35i), (2.45 + 8.92i), (6.58 + 0.39i), (1.18 + 9.20i)},
    }

    hessenbergMatrix := Mhessenberg(matrix)

    eigenValueList, _:= MshiftedIterations(hessenbergMatrix)

    for i := 0; i < len(eigenValueList); i++{
        fmt.Printf("eigenvalue %d: %6.6f + %6.6fi\n", i + 1, real(eigenValueList[i]), imag(eigenValueList[i]))
    }
}
