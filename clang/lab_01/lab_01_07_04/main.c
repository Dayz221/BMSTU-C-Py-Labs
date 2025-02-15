#include <stdio.h>
#include <math.h>

#define INCORRECT_INPUT 1

double f(double x);
double s(double x, double eps);

int main()
{
    // Ввод входных данных
    double x;
    double eps;

    printf("Enter x and eps: ");
    if (scanf("%lf%lf", &x, &eps) != 2)
    {
        printf("Incorrect input!");
        return INCORRECT_INPUT;
    }

    // Результаты работы функций
    double f_result = f(x);
    double s_result = s(x, eps);

    // Подсчет абсолютной и относительной погрешностей
    double abs_delta = fabs(f_result - s_result);
    double rel_delta = abs_delta / f_result;

    // Вывод результата
    printf("Absolute delta: %.6f\n", abs_delta);
    printf("Relative delta: %.6f\n", rel_delta);
}

// Функция f(x) из условия
double f(double x)
{
    return 1. / pow(1 + x, 3);
}

// Функция s(x) из условия
double s(double x, double eps)
{
    double result = 1;
    double prev = -3 * x;
    int i = 2;

    while (fabs(prev) > eps)
    {
        result += prev;
        prev *= -(double)(i + 2) * x / i;
        i++;
    }

    return result;
}
