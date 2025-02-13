#include <stdio.h>
#include <math.h>

#define INCORRECT_INPUT 1

float f(float x);
float s(float x, float eps);

int main()
{
    // Ввод входных данных
    float x;
    float eps;

    printf("Enter x and eps: ");
    if (scanf("%f%f", &x, &eps) != 2)
    {
        printf("Incorrect input!");
        return INCORRECT_INPUT;
    }
}

float f(float x)
{
    return 1. / pow(1 + x, 3);
}

float s(float x, float eps)
{
}
