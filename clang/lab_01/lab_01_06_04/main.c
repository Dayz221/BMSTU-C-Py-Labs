#include <stdio.h>
#include <stdbool.h>
#include <math.h>

#define INCORRECT_INPUT 1
#define ZERO_LENGTH_SEGMENT 2
#define EPS 1e-6

short is_equal(double a, double b);
short is_on_line(double x0, double y0, double x1, double y1, double xp, double yp);

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
    else if (is_equal(xq, xr) && is_equal(yq, yr))
    {
        printf("A non-zero length segment is required!");
        return ZERO_LENGTH_SEGMENT;
    }

    // Необходимые вычисления и вывод результата
    printf("Result: %d", is_on_line(xq, yq, xr, yr, xp, yp));

    return 0;
}

// Функция для сравнения двух ЧПТ
short is_equal(double a, double b)
{
    double delta = a - b;
    return fabs(delta) < EPS;
}

// Функция проверки принадлежности точки прямой
short is_on_line(double x0, double y0, double x1, double y1, double xp, double yp)
{
    // Формула выведена из канонического уравнения прямой
    double xmin = (x0 > x1) ? x1 : x0;
    double xmax = (x0 > x1) ? x0 : x1;
    double ymin = (y0 > y1) ? y1 : y0;
    double ymax = (y0 > y1) ? y0 : y1;

    // (xp >= xmin && xp <= xmax) && (yp >= ymin && yp <= ymax) - Проверка, принадлежит ли точка прямоугольнику отрезка
    // is_equal((y1 - y0) * (xp - x0), (x1 - x0) * (yp - y0)) - Проверка, принадлежит ли точка прямой с направляющим вектором QR
    return (xp >= xmin && xp <= xmax) && (yp >= ymin && yp <= ymax) && is_equal((y1 - y0) * (xp - x0), (x1 - x0) * (yp - y0));
}
