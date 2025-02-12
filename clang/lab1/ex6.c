#include <stdio.h>
#include <math.h>

#define EPS 1e-6

int main()
{
    // Ввод входных данных
    float xq, yq;
    float xr, yr;
    float xp, yp;
    int rc = 0;

    printf("Enter xq and yq: ");
    rc += scanf("%f%f", &xq, &yq);

    printf("Enter xr and yr: ");
    rc += scanf("%f%f", &xr, &yr);

    printf("Enter xp and yp: ");
    rc += scanf("%f%f", &xp, &yp);

    // Проверка на корректность ввода
    if (rc != 6) {
        printf("Incorrect input!");
        return 1;
    }

    // Необходимые вычисления и вывод результата
    printf("Result: %d", abs((yr - yq) * (xp - xq) - (xr - xq) * (yp - yq)) < EPS);

    return 0;
}