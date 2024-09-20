#include <stdio.h>
#include <stdlib.h>

void generate_line_points(double x1, double y1, double x2, double y2, double *points, int num_points) {
    double dx = x2 - x1;
    double dy = y2 - y1;
    
    for (int i = 0; i < num_points; i++) {
        double t = (double)i / (num_points - 1);
        points[i * 2] = x1 + t * dx;
        points[i * 2 + 1] = y1 + t * dy;
    }
}
void free_ptr(double *points){
    free(points);

}

