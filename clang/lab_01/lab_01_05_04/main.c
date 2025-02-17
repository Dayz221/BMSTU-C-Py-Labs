#include <stdio.h>
#include <math.h>

#define INCORRECT_INPUT 1
#define ERROR_NEGATIVE_NUMBER 2

void print_dividers(int num);

int main()
{
    // Ввод входных данных
    int number;

    printf("Enter number: ");

    // Проверка на корректность ввода
    if (scanf("%d", &number) != 1)
    {
        printf("Incorrect input!");
        return INCORRECT_INPUT;
    }
    else if (number <= 0)
    {
        printf("Number should be positive!");
        return ERROR_NEGATIVE_NUMBER;
    }

    // Необходимые вычисления и вывод результата
    printf("Dividers: ");
    if (number != 1)
        print_dividers(number);
    else
        printf("none");

    return 0;
}

void print_dividers(int num)
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