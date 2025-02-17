#include <stdio.h>
#include <math.h>

#define METERS_IN_CENTIMETER 0.01

int main()
{
    // Ввод входных данных
    double m; // Масса
    double t; // Обхват груди
    double h; // Высота

    printf("Enter h, t and m: ");
    scanf("%lf%lf%lf", &h, &t, &m);

    // Необходимые вычисления
    double m_normal;
    double bmi;

    m_normal = h * t / 240.;
    // h *= METERS_IN_CENTIMETER; // Перевод из сантиметров в метры
    bmi = m / (h * h) / (METERS_IN_CENTIMETER * METERS_IN_CENTIMETER);

    // Вывод результата
    printf("M normal: %.6lf\n", m_normal);
    printf("BMI: %.6lf\n", bmi);

    return 0;
}
