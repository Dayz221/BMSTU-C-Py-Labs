#include <stdio.h>

int main()
{
    // Ввод входных данных
    double a, b; // Основания трапеции
    double h;    // Высота трапеции

    printf("Enter a, b and h: ");
    scanf("%lf%lf%lf", &a, &b, &h);

    // Необходимые вычисления
    double p;    // Периметр трапеции
    double side; // Длина боковой стороны

    double delta = (a - b) / 2;
    side = sqrt(delta * delta + h * h);
    p = a + b + 2 * side;

    // Вывод результата
    printf("Result: %.6f\n", p);

    return 0;
}
