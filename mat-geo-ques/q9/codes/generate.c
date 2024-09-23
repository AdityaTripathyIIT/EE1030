#include <stdio.h>
#include <stdlib.h>
#include <math.h>
struct point {
	double x;
	double y;
};
struct triangle {
	double len;
	struct point vertex1;
	struct point vertex2;
	struct point vertex3;
	int num_points;
	struct point **sides;
};
struct point *get_vertex(struct point point1, struct point point2) {
    
	double vec_x = point2.x - point1.x;
	double vec_y = point2.y - point1.y;
	double cos_val = sqrt(3) / 2;
	double sin_val = 0.5;
        struct point *vertex ;
	vertex -> x = cos_val * vec_x - sin_val * vec_y;  vertex -> y = (-1) * (cos_val) * vec_y + sin_val * vec_x;
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
void generate_triangle(struct triangle to_draw) {
    struct point *sides = (struct point*) malloc(3 * to_draw.num_points * sizeof(struct point));
    to_draw.sides[0] = generate_line_points(to_draw.vertex1, to_draw.vertex2, to_draw.num_points);
    to_draw.vertex3 = *get_vertex(to_draw.vertex1, to_draw.vertex2);
    to_draw.sides[1] = generate_line_points(to_draw.vertex3, to_draw.vertex2, to_draw.num_points);
    to_draw.sides[1] = generate_line_points(to_draw.vertex3, to_draw.vertex2, to_draw.num_points);

}
void free_triangle(struct triangle to_draw){
	free(to_draw.sides);
}
