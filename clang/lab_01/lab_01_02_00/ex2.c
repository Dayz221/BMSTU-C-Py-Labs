#include <stdio.h>
#include <math.h>

int main()
{
    // Ввод входных данных
    float a, b; // Основания трапеции
    float h;    // Высота трапеции

    printf("Enter a: ");
    scanf("%f", &a);

    printf("Enter b: ");
    scanf("%f", &b);

    printf("Enter h: ");
    scanf("%f", &h);

    // Необходимые вычисления
    float p;    // Периметр трапеции
    float side; // Длина боковой стороны

    side = sqrt(pow((a - b) / 2, 2) + pow(h, 2));
    p = a + b + 2 * side;

    // Вывод результата
    printf("Result: %.6f\n", p);

    return 0;
}
