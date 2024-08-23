#include <stdio.h>

int main() {
    FILE *file = fopen("points.txt", "w");
    if (file == NULL) {
        perror("Unable to open file");
        return 1;
    }

    int num_points = 1000;
    double x_start = 3.0, y_start = 1.0;
    double x_end = 6.0, y_end = 4.0;
    
    for (int i = 0; i < num_points; i++) {
        double t = (double)i / (num_points - 1);
        double x = x_start + t * (x_end - x_start);
        double y = y_start + t * (y_end - y_start);
        fprintf(file, "%lf %lf\n", x, y);
    }

    fclose(file);
    return 0;
}

