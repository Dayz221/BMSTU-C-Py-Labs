#include <stdio.h>
#include <math.h>

int main()
{
    // Ввод входных данных
    int number;

    printf("Enter number: ");

    // Проверка на корректность ввода
    if (scanf("%d", &number) != 1 || number <= 0)
    {
        printf("Incorrect input!");
        return 1;
    }

    // Необходимые вычисления и вывод результата
    printf("Dividers:");

    for (int i = 2; i < sqrt(number) + 1; i++)
    {
        while (number % i == 0)
        {
            printf(" %d", i);
            number /= i;
        }
    }

    if (number != 1)
        printf(" %d", number);

    return 0;
}