#include <stdio.h>
#include <stdint.h>
#include <math.h>

int main()
{
    // Ввод входных данных
    int i = 1;
    double val;
    double result = 0;

    printf("Enter numbers:\n");
    while (1)
    {
        scanf("%lf", &val);
        if (val < 0) break;

        result += val / i;
        i++;
    }

    // Необходимые вычисления
    result = sqrt(result);

    // Вывод результата
    printf("Result: %.6f", result);

    return 0;
}
