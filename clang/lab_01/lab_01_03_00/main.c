#include <stdio.h>
#include <math.h>

#define METERS_IN_CENTIMETER 0.01

int main()
{
    // Ввод входных данных
    double m; // Масса
    double t; // Обхват груди
    double h; // Высота

    printf("Enter m, t and h: ");
    scanf("%lf%lf%lf", &m, &t, &h);

    // Необходимые вычисления
    double m_normal;
    double bmi;

    m_normal = h * t / 240.;
    h *= METERS_IN_CENTIMETER; // Перевод из сантиметров в метры
    bmi = m / (h * h);

    // Вывод результата
    printf("M normal: %.6f\n", m_normal);
    printf("BMI: %.6f\n", bmi);

    return 0;
}
