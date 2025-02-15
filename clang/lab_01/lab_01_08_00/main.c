#include <stdio.h>
#include <stdint.h>

#define INCORRECT_INPUT 1
#define ERROR_NEGATIVE_N 2
#define NUM_LEN_IN_BITS 32

void printBin(uint32_t num);

int main()
{
    // Ввод входных данных
    uint32_t a;
    int n;

    printf("Enter a and n: ");
    if (scanf("%d%d", &a, &n) != 2)
    {
        printf("Error: Incorrect input!");
        return INCORRECT_INPUT;
    }
    else if (n < 0)
    {
        printf("Error: n should be positive!");
        return ERROR_NEGATIVE_N;
    }

    // Необходимые вычисления
    n %= NUM_LEN_IN_BITS;
    uint32_t right_part = a & ~(~0 << n); // ~(~0 << n) - маска. Пример при n = 3, mask = 00...00111
    a >>= n;
    a |= right_part << (NUM_LEN_IN_BITS - n);

    // Вывод результата
    printBin(a);

    return 0;
}

// Функция вывода числа в 2-ой системе счисления
void printBin(uint32_t num)
{
    printf("Result: ");
    for (int i = 0; i < NUM_LEN_IN_BITS; i++)
        printf("%d", (num >> (NUM_LEN_IN_BITS - 1 - i)) & 01);
}