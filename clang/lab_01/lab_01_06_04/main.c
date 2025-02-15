#include <stdio.h>
#include <stdbool.h>
#include <math.h>

#define INCORRECT_INPUT 1
#define EPS 1e-6

_Bool isEqual(double a, double b);
_Bool isOnLine(double x0, double y0, double x1, double y1, double xp, double yp);

int main()
{
    // Ввод входных данных
    double xq, yq;
    double xr, yr;
    double xp, yp;

    printf("Enter xq, yq, xr, yr, xp, yp: ");

    // Проверка на корректность ввода
    if (scanf("%lf%lf%lf%lf%lf%lf", &xq, &yq, &xr, &yr, &xp, &yp) != 6)
    {
        printf("Incorrect input!");
        return INCORRECT_INPUT;
    }

    // Необходимые вычисления и вывод результата
    printf("Result: %d", isOnLine(xq, yq, xr, yr, xp, yp));

    return 0;
}

// Функция для сравнения двух ЧПТ
_Bool isEqual(double a, double b)
{
    double delta = a - b;
    return fabs(delta) < EPS;
}

// Функция проверки принадлежности точки прямой
_Bool isOnLine(double x0, double y0, double x1, double y1, double xp, double yp)
{
    // Формула выведена из канонического уравнения прямой
    return isEqual((y1 - y0) * (xp - x0), (x1 - x0) * (yp - y0));
}
