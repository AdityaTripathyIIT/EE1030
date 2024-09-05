#include <stdio.h>
#include <stdlib.h>
double **createMat(int m, int n) {
    int i;
    double **a;

    a = (double **)malloc(m * sizeof(*a));
    for (i = 0; i < m; i++)
        a[i] = (double *)malloc(n * sizeof(*a[i]));

    return a;
}

void freeMat(double **matrix, int rows) {
    for (int i = 0; i < rows; ++i) {
        free(matrix[i]);
    }
    free(matrix);
}

void solveMatrixVectorProduct(double row1[3], double row2[3], double output[2]) {
    double **matrix = createMat(2, 3);
    matrix[0][0] = row1[0];
    matrix[0][1] = row1[1];
    matrix[0][2] = row1[2];
    matrix[1][0] = row2[0];
    matrix[1][1] = row2[1];
    matrix[1][2] = row2[2];

    if (matrix[0][0] == 0) {
        if (matrix[1][0] != 0) {
            double *temp = matrix[0];
            matrix[0] = matrix[1];
            matrix[1] = temp;
        } else {
            printf("No unique solution exists.\n");
            freeMat(matrix, 2);
            return;
        }
    }

    double factor = matrix[1][0] / matrix[0][0];
    for (int j = 0; j < 3; ++j) {
        matrix[1][j] -= factor * matrix[0][j];
    }

    if (matrix[1][1] == 0) {
        if (matrix[1][2] != 0) {
            printf("No solution exists.\n");
            freeMat(matrix, 2);
            return;
        }
        printf("Infinite solutions exist.\n");
        freeMat(matrix, 2);
        return;
    }

    double y = matrix[1][2] / matrix[1][1];
    double x = (matrix[0][2] - matrix[0][1] * y) / matrix[0][0];

    output[0] = x;
    output[1] = y;

    freeMat(matrix, 2);
}
void generate_line_points(double** matrix, double* points, int num_points) {
    double dx = matrix[1][0] - matrix[0][0];
    double dy = matrix[1][1]-matrix[0][1];
    
    for (int i = 0; i < num_points; i++) {
        double t = (double)i / (num_points - 1);
        points[i * 2] = matrix[0][0] + t * dx;
        points[i * 2 + 1] = matrix[0][1] + t * dy;
    }
}
void free_ptr(double *points){
    free(points);

}
int main(){
    return 0;
}
