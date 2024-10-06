#include <stdio.h>
#include <math.h>
#include <stdlib.h>
struct point {
    double x;
    double y;
};
struct Circle {
    struct point center;
    double radius;
    int num_points;
    struct point *points;
};

void generate_circle_points(struct Circle *my_circle) {
    my_circle->points = malloc(sizeof(struct point) * my_circle->num_points);
    for (int i = 0; i < my_circle->num_points; i++) {
        double angle = 2 * M_PI * i / my_circle->num_points;
        my_circle->points[i].x = my_circle->center.x + my_circle->radius * cos(angle);
        my_circle->points[i].y = my_circle->center.y + my_circle->radius * sin(angle);
    }
}

void free_circle_points(struct Circle *my_circle) {
    if (my_circle->points != NULL) {
        free(my_circle->points);
        my_circle->points = NULL;
    }
}

