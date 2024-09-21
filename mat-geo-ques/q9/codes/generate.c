#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void get_vertex(double x1, double y1, double *x2, double *y2) {
    *x2 = x1 / 2;
    *y2 = sqrt(3) * x1 / 2;
}

void generate_line_points(double x1, double y1, double x2, double y2, int num_points, double points[][2]) {
    double dx = x2 - x1;
    double dy = y2 - y1;

    for (int i = 0; i < num_points; i++) {
        double t = (double)i / (num_points - 1);
        points[i][0] = x1 + t * dx;
        points[i][1] = y1 + t * dy;
    }
}

void generate_triangle(double len, int num_points, double points[3][num_points][2]) {
    generate_line_points(0, 0, len, 0, num_points, points[0]);
    
    double x2, y2;
    get_vertex(len, 0, &x2, &y2);
    
    generate_line_points(len, 0, x2, y2, num_points, points[1]);
    generate_line_points(0, 0, x2, y2, num_points, points[2]);
}

