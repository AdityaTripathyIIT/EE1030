#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double *generate_circle_points(double center[2], double radius, int num_points) {
    double *points = (double *)malloc(sizeof(double) * 2 * num_points);	
    for (int i = 0; i < num_points; i++) {
        double angle = 2 * M_PI * i / num_points;
        points[2 * i] = center[0] + radius * cos(angle);
        points[2 * i + 1] = center[1] + radius * sin(angle);
    }
    return points;
}

