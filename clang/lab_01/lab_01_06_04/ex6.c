#include <stdio.h>
#include <stdbool.h>

#define INCORRECT_INPUT 1
#define EPS 1e-6

_Bool isEqual(float a, float b);
_Bool isOnLine(float x0, float y0, float x1, float y1, float xp, float yp);

int main()
{
    // Ввод входных данных
    float xq, yq;
    float xr, yr;
    float xp, yp;

    printf("Enter xq, yq, xr, yr, xp, yp: ");

    // Проверка на корректность ввода
    if (scanf("%f%f%f%f%f%f", &xq, &yq, &xr, &yr, &xp, &yp) != 6)
    {
        printf("Incorrect input!");
        return INCORRECT_INPUT;
    }

    // Необходимые вычисления и вывод результата
    printf("Result: %d", isOnLine(xq, yq, xr, yr, xp, yp));

    return 0;
}

// Функция для сравнения двух ЧПТ
_Bool isEqual(float a, float b)
{
    float delta = a - b;
    return delta > -EPS && delta < EPS;
}

// Функция проверки принадлежности точки прямой
_Bool isOnLine(float x0, float y0, float x1, float y1, float xp, float yp)
{
    // Формула выведена из канонического уравнения прямой
    return isEqual((y1 - y0) * (xp - x0), (x1 - x0) * (yp - y0));
}
