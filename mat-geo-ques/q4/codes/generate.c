#include <stdio.h>
#include <stdlib.h>

void generate_line_points(double x1, double y1, double z1, double x2, double y2, double z2, double *points, int num_points) {
    double dx = x2 - x1;
    double dy = y2 - y1;
    double dz = z2 - z1;
    
    for (int i = 0; i < num_points; i++) {
        double t = (double)i / (num_points - 1);
        points[i * 3] = x1 + t * dx;
        points[i * 3 + 1] = y1 + t * dy;
        points[i * 3 + 2] = z1 + t * dz;
    }
}
void free_ptr( double *points){
    free(points);
}
