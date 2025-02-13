#include <stdio.h>
#include <math.h>

#define INCORRECT_INPUT 1

void printDividers(int num);

int main()
{
    // Ввод входных данных
    int number;

    printf("Enter number: ");

    // Проверка на корректность ввода
    if (scanf("%d", &number) != 1 || number <= 0)
    {
        printf("Incorrect input!");
        return INCORRECT_INPUT;
    }

    // Необходимые вычисления и вывод результата
    if (number != 1)
    {
        printf("Dividers: ");
        printDividers(number);
    }

    return 0;
}

void printDividers(int num)
{
    for (int i = 2; i < sqrt(num) + 1; i++)
    {
        while (num % i == 0)
        {
            printf("%d ", i);
            num /= i;
        }
    }

    if (num != 1)
        printf("%d", num);
}
