#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Define the vertices of the tetrahedron
const float v1[] = {2.0, 3.0, 4.0};
const float v2[] = {-1.0, -2.0, 1.0};
const float v3[] = {5.0, 8.0, 7.0};

// Function to generate a random point within the tetrahedron
void generate_random_point(float* x, float* y, float* z) {
    float r1 = (float)rand() / RAND_MAX;
    float r2 = (float)rand() / RAND_MAX;
    float r3 = (float)rand() / RAND_MAX;

    if (r1 + r2 > 1) {
        r1 = 1 - r1;
        r2 = 1 - r2;
    }

    *x = v1[0] + r1 * (v2[0] - v1[0]) + r2 * (v3[0] - v1[0]);
    *y = v1[1] + r1 * (v2[1] - v1[1]) + r2 * (v3[1] - v1[1]);
    *z = v1[2] + r1 * (v2[2] - v1[2]) + r2 * (v3[2] - v1[2]);
}

int main() {
    FILE* file = fopen("points.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    srand(time(NULL)); // Seed the random number generator

    for (int i = 0; i < 1000; ++i) {
        float x, y, z;
        generate_random_point(&x, &y, &z);
        fprintf(file, "%f %f %f\n", x, y, z);
    }

    fclose(file);
    return 0;
}

