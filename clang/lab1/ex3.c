#include <stdio.h>
#include <math.h>

int main()
{
    // Ввод входных данных
    float m; // Масса
    float t; // Обхват груди
    float h; // Высота

    printf("Enter ь: ");
    scanf("%f", &m);

    printf("Enter t: ");
    scanf("%f", &t);

    printf("Enter h: ");
    scanf("%f", &h);

    // Необходимые вычисления
    float m_normal;
    float bmi;

    m_normal = h * t / 240;
    bmi = m / pow(h, 2);

    // Вывод результата
    printf("M normal: %f\n", m_normal);
    printf("BMI: %f\n", bmi);

    return 0;
}