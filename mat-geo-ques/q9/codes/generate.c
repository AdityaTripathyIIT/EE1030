#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct point {
    double x;
    double y;
};

struct triangle {
    double length;
    struct point vertex1;
    struct point vertex2;
    struct point vertex3;
    int num_points;
    struct point **sides;
};
struct point *get_vertex(struct point point1, struct point point2) {
    struct point *vertex = malloc(sizeof(struct point));
    double vec_x = point2.x - point1.x;
    double vec_y = point2.y - point1.y;
    
    vertex->x = point1.x + (vec_x / 2) - (sqrt(3) * vec_y / 2);
    vertex->y = point1.y + (sqrt(3) * vec_x / 2) + (vec_y / 2);
    
    return vertex;
}
struct point *generate_line_points(struct point point1, struct point point2, int num_points) {
    double dx = point2.x - point1.x;
    double dy = point2.y - point1.y;
    struct point *sides = (struct point*) malloc(num_points * sizeof(struct point));
    for (int i = 0; i < num_points; i++) {
        double t = (double)i / (num_points - 1);
        sides[i].x = point1.x + t * dx;
        sides[i].y = point1.y + t * dy;
    }
    return sides;
}

void generate_triangle(struct triangle *to_draw) {
    to_draw->sides = (struct point**) malloc(3 * sizeof(struct point*));
    to_draw->sides[0] = generate_line_points(to_draw->vertex1, to_draw->vertex2, to_draw->num_points);
    to_draw->vertex3 = *get_vertex(to_draw->vertex1, to_draw->vertex2);
    to_draw->sides[1] = generate_line_points(to_draw->vertex2, to_draw->vertex3, to_draw->num_points);
    to_draw->sides[2] = generate_line_points(to_draw->vertex1, to_draw->vertex3, to_draw->num_points);
}

void free_triangle(struct triangle *to_draw){
    for (int i = 0; i < 3; i++) {
        free(to_draw->sides[i]);
    }
    free(to_draw->sides);
}

