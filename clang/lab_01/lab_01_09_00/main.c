#include <stdio.h>
#include <stdint.h>
#include <math.h>

#define INCORRECT_INPUT -1
#define TOO_FEW_VALUES -2

double scan_sum();

int main()
{
    // Ввод входных данных
    double result;

    printf("Enter numbers:\n");
    result = scan_sum();

    if (result == INCORRECT_INPUT) {
        printf("Incorrect input!");
        return INCORRECT_INPUT;
    }
    else if (result == TOO_FEW_VALUES) {
        printf("Too few values!");
        return TOO_FEW_VALUES;
    }

    // Необходимые вычисления
    result = sqrt(result);

    // Вывод результата
    printf("g(x): %.6f", result);

    return 0;
}

double scan_sum()
{
    int i = 1;
    double val;
    double result = 0;

    while (1)
    {
        if (scanf("%lf", &val) != 1)
            return INCORRECT_INPUT;

        if (val < 0)
            break;

        result += val / i;
        i++;
    }

    return (i == 1) ? TOO_FEW_VALUES : result;
}